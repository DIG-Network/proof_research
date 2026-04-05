#!/usr/bin/env python3
"""
n=7, shell {2,3}: verify on the full 35×35 grid that

  min_d == 2  <=>  r4 subset is the complement of r3 subset

for coord + full r=2 + one r=3 + one r=4.

Exit 0 = PASS (all checks OK).
Exit 1 = FAIL (counterexample found).

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py
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

    viol_a: list[str] = []
    viol_b: list[str] = []
    viol_c: list[str] = []
    count_d2 = 0
    count_comp = 0
    t0 = time.perf_counter()
    total = len(p3) * len(p4)
    done = 0
    for i in range(len(p3)):
        t_mask = subset_mask(triples[i])
        for j in range(len(p4)):
            q_mask = subset_mask(quads[j])
            comp = (FULL_MASK ^ t_mask) & FULL_MASK
            is_comp = q_mask == comp

            xor_lists = [p2, [p3[i]], [p4[j]]]
            md, _ = mod.min_depth_for_language(masks, coord, xor_lists, mod.N, LRU_CAP)
            done += 1

            if is_comp:
                count_comp += 1
            if md == 2:
                count_d2 += 1
                if not is_comp:
                    viol_a.append(
                        f"min_d=2 but not complement: i={i} j={j} "
                        f"T={triples[i]} Q={quads[j]}"
                    )
            elif md is not None and md >= 3:
                if is_comp:
                    viol_c.append(
                        f"min_d>=3 but complement: i={i} j={j} "
                        f"T={triples[i]} Q={quads[j]} md={md}"
                    )
            if is_comp and md != 2:
                viol_b.append(
                    f"complement pair but min_d!=2: i={i} j={j} "
                    f"T={triples[i]} Q={quads[j]} md={md}"
                )

            if done % 200 == 0 or done == total:
                print(f"progress {done}/{total} i={i} j={j} md={md}", flush=True)

    wall = time.perf_counter() - t0
    print(f"grid_done={total} complement_pairs={count_comp} min_d2_cells={count_d2} wall_sec={wall:.3f}", flush=True)

    if viol_a or viol_b or viol_c:
        for v in viol_a[:20]:
            print(f"VIOL_A: {v}", flush=True)
        for v in viol_b[:20]:
            print(f"VIOL_B: {v}", flush=True)
        for v in viol_c[:20]:
            print(f"VIOL_C: {v}", flush=True)
        extra = len(viol_a) + len(viol_b) + len(viol_c) - 60
        if extra > 0:
            print(f"... and {extra} more violations", flush=True)
        print("FAIL: complement iff characterization broken", flush=True)
        sys.exit(1)

    if count_comp != 35 or count_d2 != 35:
        print(
            f"FAIL: expected 35 complement pairs and 35 min_d=2 cells, "
            f"got comp={count_comp} d2={count_d2}",
            flush=True,
        )
        sys.exit(1)

    print(
        "PASS: on full 35×35 grid, min_d=2 iff r4 subset is complement of r3 subset "
        f"({count_d2} cells)",
        flush=True,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
