#!/usr/bin/env python3
r"""
n=7, shell {2,3,4}: diagonal i==j slice of the doubleton-triple + singleton-quartic grid.

Language: coord + full r=2 + duplicate r=3 XOR splits (same triple T_i twice) + one r=4 XOR split.

Hypothesis (biconditional on all 35×35 diagonal cells):

  min_d == 2  <=>  Q_mask == complement(T_i) on [7]

Exit 0 = PASS; exit 1 = FAIL.
"""

from __future__ import annotations

import importlib.util
import sys
import time
from itertools import combinations
from pathlib import Path

PARENT = Path(__file__).resolve().parents[1] / (
    "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py"
)

LRU_CAP = 4_000_000
N_EXPECT = 7
FULL_MASK = (1 << N_EXPECT) - 1


def _load_parent():
    spec = importlib.util.spec_from_file_location("n7driver", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PARENT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def subset_mask(idxs: tuple[int, ...]) -> int:
    m = 0
    for i in idxs:
        m |= 1 << i
    return m


def main() -> None:
    mod = _load_parent()
    assert mod.N == N_EXPECT

    masks = mod.build_masks()
    coord = mod.build_coord_partition_masks(masks)
    p2 = mod.build_r_xor_partition_masks(masks, 2)
    p3 = mod.build_r_xor_partition_masks(masks, 3)
    p4 = mod.build_r_xor_partition_masks(masks, 4)
    assert len(p3) == 35 and len(p4) == 35

    triples = list(combinations(range(N_EXPECT), 3))
    quads = list(combinations(range(N_EXPECT), 4))
    assert len(triples) == 35 and len(quads) == 35

    md_full, _ = mod.min_depth_for_language(
        masks,
        coord,
        [mod.build_r_xor_partition_masks(masks, mod.N)],
        mod.N,
        LRU_CAP,
    )
    if md_full != 1:
        print("FAIL: full-n-XOR baseline must be 1", flush=True)
        sys.exit(1)

    viol_d2_not_comp: list[str] = []
    viol_comp_not_d2: list[str] = []

    count_cells = 0
    count_d2 = 0
    count_pred = 0

    t0 = time.perf_counter()
    for i in range(len(p3)):
        t_i = subset_mask(triples[i])
        comp_i = FULL_MASK ^ t_i
        for k in range(len(p4)):
            q_mask = subset_mask(quads[k])
            xor_lists = [p2, [p3[i], p3[i]], [p4[k]]]
            md, _ = mod.min_depth_for_language(
                masks, coord, xor_lists, mod.N, LRU_CAP
            )
            count_cells += 1

            pred = q_mask == comp_i
            if pred:
                count_pred += 1

            if md == 2:
                count_d2 += 1
                if not pred:
                    viol_d2_not_comp.append(
                        f"diag i={i} k={k} md=2 but Q!=comp(T): "
                        f"T={triples[i]} Q={quads[k]} "
                        f"Qbits={q_mask:07b} comp={comp_i:07b}"
                    )
            elif pred and md is not None and md != 2:
                viol_comp_not_d2.append(
                    f"diag i={i} k={k} pred(comp) but md={md} "
                    f"T={triples[i]} Q={quads[k]}"
                )

            if count_cells % 400 == 0:
                print(
                    f"progress {count_cells}/1225 i={i} k={k} md={md}",
                    flush=True,
                )

    wall = time.perf_counter() - t0
    print(
        f"grid_done={count_cells} wall_sec={wall:.3f} "
        f"diag_cells={count_cells} min_d2={count_d2} pred_comp={count_pred}",
        flush=True,
    )

    all_viol = viol_d2_not_comp + viol_comp_not_d2
    print(
        f"viol_counts d2_not_comp={len(viol_d2_not_comp)} "
        f"comp_not_d2={len(viol_comp_not_d2)} total={len(all_viol)}",
        flush=True,
    )
    if all_viol:
        for v in viol_d2_not_comp[:25]:
            print(f"VIOL_D2_NOT_COMP: {v}", flush=True)
        for v in viol_comp_not_d2[:25]:
            print(f"VIOL_COMP_NOT_D2: {v}", flush=True)
        extra = len(all_viol) - 50
        if extra > 0:
            print(f"... and {extra} more violations", flush=True)
        print(
            "FAIL: diagonal i=j min_d=2 iff Q=complement(T_i) broken",
            flush=True,
        )
        sys.exit(1)

    if count_d2 != count_pred:
        print(
            f"FAIL: internal mismatch d2={count_d2} pred={count_pred}",
            flush=True,
        )
        sys.exit(1)

    print(
        "PASS: for i=j, min_d=2 iff quartic Q is complement of triple T_i",
        flush=True,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
