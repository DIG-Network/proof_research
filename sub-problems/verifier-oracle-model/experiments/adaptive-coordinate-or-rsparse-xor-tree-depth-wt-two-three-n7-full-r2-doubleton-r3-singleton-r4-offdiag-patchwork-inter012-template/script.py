#!/usr/bin/env python3
"""
n=7, shell {2,3}: test patchwork predicate for min_d==2 on

  coord + full r=2 + two r=3 XOR splits (i<=j) + one r=4 XOR split k

Diagonal i==j: Q = complement of T_i (known).

Off-diagonal i<j: stratify by s = |T_i ∩ T_j|:
  - s in {0,1}: pred iff Q == T_i △ T_j
  - s == 2: pred iff Q == (T_i minus T_j) ∪ ([7] \ (T_i ∪ T_j))

Exit 0 = PASS (full-grid biconditional).
Exit 1 = FAIL (counterexample).
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


def symdiff_masks(a: int, b: int) -> int:
    return a ^ b


def popc(m: int) -> int:
    return m.bit_count()


def patchwork_expected_quad(t_i: int, t_j: int) -> int | None:
    """Bitmask of vertices in Q predicted by patchwork (off-diagonal only)."""
    inter = t_i & t_j
    s = popc(inter)
    if s in (0, 1):
        return symdiff_masks(t_i, t_j)
    if s == 2:
        only_i = t_i & (FULL_MASK ^ t_j)
        union = t_i | t_j
        exterior = FULL_MASK ^ union
        return only_i | exterior
    return None


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

    viol_pred_but_not_d2: list[str] = []
    viol_d2_diag_not_comp: list[str] = []
    viol_d2_off_not_patch: list[str] = []
    viol_d2_off_bad_s: list[str] = []

    count_cells = 0
    count_d2 = 0
    count_d2_diag = 0
    count_d2_off = 0
    count_pred_diag = 0
    count_pred_off = 0

    t0 = time.perf_counter()
    for i in range(len(p3)):
        t_i = subset_mask(triples[i])
        for j in range(i, len(p3)):
            t_j = subset_mask(triples[j])
            for k in range(len(p4)):
                q_mask = subset_mask(quads[k])
                comp_i = (FULL_MASK ^ t_i) & FULL_MASK

                xor_lists = [p2, [p3[i], p3[j]], [p4[k]]]
                md, _ = mod.min_depth_for_language(
                    masks, coord, xor_lists, mod.N, LRU_CAP
                )
                count_cells += 1

                if i == j:
                    pred = q_mask == comp_i
                    if pred:
                        count_pred_diag += 1
                    if md == 2:
                        count_d2 += 1
                        count_d2_diag += 1
                        if not pred:
                            viol_d2_diag_not_comp.append(
                                f"diag i=j={i} k={k} md=2 but Q!=comp(T): "
                                f"T={triples[i]} Q={quads[k]}"
                            )
                    elif pred and md is not None and md >= 3:
                        viol_pred_but_not_d2.append(
                            f"diag i=j={i} k={k} pred(comp) but md={md}"
                        )
                else:
                    inter = popc(t_i & t_j)
                    exp = patchwork_expected_quad(t_i, t_j)
                    if exp is None:
                        viol_d2_off_bad_s.append(
                            f"off i={i} j={j} unexpected |∩|={inter} "
                            f"T_i={triples[i]} T_j={triples[j]}"
                        )
                        pred = False
                    else:
                        pred = q_mask == exp
                    if pred:
                        count_pred_off += 1
                    if md == 2:
                        count_d2 += 1
                        count_d2_off += 1
                        if exp is None or q_mask != exp:
                            viol_d2_off_not_patch.append(
                                f"off i={i} j={j} k={k} md=2 but Q!=patchwork: "
                                f"|∩|={inter} T_i={triples[i]} T_j={triples[j]} "
                                f"Q={quads[k]} exp_mask={exp if exp is not None else -1}"
                            )
                    elif pred and md is not None and md >= 3:
                        viol_pred_but_not_d2.append(
                            f"off i={i} j={j} k={k} pred(patchwork) but md={md}"
                        )

                if count_cells % 3000 == 0:
                    print(
                        f"progress {count_cells}/22050 i={i} j={j} k={k} md={md}",
                        flush=True,
                    )

    wall = time.perf_counter() - t0
    print(
        f"grid_done={count_cells} wall_sec={wall:.3f} "
        f"min_d2={count_d2} (diag={count_d2_diag} off={count_d2_off}) "
        f"pred_diag={count_pred_diag} pred_off={count_pred_off}",
        flush=True,
    )

    all_viol = (
        viol_pred_but_not_d2
        + viol_d2_diag_not_comp
        + viol_d2_off_not_patch
        + viol_d2_off_bad_s
    )
    if all_viol:
        for v in viol_pred_but_not_d2[:15]:
            print(f"VIOL_PRED: {v}", flush=True)
        for v in viol_d2_diag_not_comp[:15]:
            print(f"VIOL_D2_DIAG: {v}", flush=True)
        for v in viol_d2_off_bad_s[:15]:
            print(f"VIOL_OFF_S: {v}", flush=True)
        for v in viol_d2_off_not_patch[:15]:
            print(f"VIOL_D2_OFF_PATCH: {v}", flush=True)
        extra = len(all_viol) - 60
        if extra > 0:
            print(f"... and {extra} more violations", flush=True)
        print("FAIL: patchwork biconditional broken", flush=True)
        sys.exit(1)

    if count_d2_diag != 35:
        print(f"FAIL: expected 35 diagonal min_d=2, got {count_d2_diag}", flush=True)
        sys.exit(1)
    if count_d2_off != 1190:
        print(f"FAIL: expected 1190 off-diagonal min_d=2, got {count_d2_off}", flush=True)
        sys.exit(1)
    if count_pred_diag != 35 or count_pred_off != 1190:
        print(
            f"FAIL: predicate counts mismatch pred_diag={count_pred_diag} "
            f"pred_off={count_pred_off}",
            flush=True,
        )
        sys.exit(1)

    print(
        "PASS: full grid — diagonal min_d=2 iff complement; "
        "off-diagonal min_d=2 iff patchwork (symdiff if |∩|∈{0,1}, "
        "ordered wedge if |∩|=2)",
        flush=True,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
