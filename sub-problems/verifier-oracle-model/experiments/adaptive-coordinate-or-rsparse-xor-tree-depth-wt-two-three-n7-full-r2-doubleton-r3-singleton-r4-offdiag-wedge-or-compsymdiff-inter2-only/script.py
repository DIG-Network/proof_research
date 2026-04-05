#!/usr/bin/env python3
r"""
n=7, shell {2,3}: test two-chart disjunction for off-diagonal |T_i∩T_j|==2.

Language: coord + full r=2 + two r=3 XOR splits (i<j only in analysis) + one r=4 XOR split.

For i<j with s=popc(T_i & T_j)==2, define:
  W = (T_i \ T_j) ∪ ([7] \ (T_i ∪ T_j))   # ordered wedge
  C = FULL_MASK ^ (T_i ⊕ T_j)             # complement of symmetric difference

Hypothesis (stratum-only): min_d==2  <=>  Q in {W, C}.

Exit 0 = PASS (biconditional holds on s=2 stratum).
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


def wedge_mask(t_i: int, t_j: int) -> int:
    only_i = t_i & (FULL_MASK ^ t_j)
    union = t_i | t_j
    exterior = FULL_MASK ^ union
    return only_i | exterior


def complement_symdiff_mask(t_i: int, t_j: int) -> int:
    return FULL_MASK ^ symdiff_masks(t_i, t_j)


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

    viol_d2_not_in_charts: list[str] = []
    viol_chart_but_not_d2: list[str] = []

    count_cells_total = 0
    count_stratum_s2 = 0  # i<j and |∩|==2
    count_stratum_d2 = 0
    count_stratum_pred = 0  # Q in {W,C}

    t0 = time.perf_counter()
    for i in range(len(p3)):
        t_i = subset_mask(triples[i])
        for j in range(i, len(p3)):
            t_j = subset_mask(triples[j])
            s_inter = popc(t_i & t_j)
            for k in range(len(p4)):
                q_mask = subset_mask(quads[k])
                xor_lists = [p2, [p3[i], p3[j]], [p4[k]]]
                md, _ = mod.min_depth_for_language(
                    masks, coord, xor_lists, mod.N, LRU_CAP
                )
                count_cells_total += 1

                if i >= j:
                    continue
                if s_inter != 2:
                    continue

                count_stratum_s2 += 1
                w = wedge_mask(t_i, t_j)
                c = complement_symdiff_mask(t_i, t_j)
                pred = q_mask == w or q_mask == c
                if pred:
                    count_stratum_pred += 1
                if md == 2:
                    count_stratum_d2 += 1

                if md == 2 and not pred:
                    viol_d2_not_in_charts.append(
                        f"i={i} j={j} k={k} md=2 s=2 Q={quads[k]} "
                        f"T_i={triples[i]} T_j={triples[j]} "
                        f"Wbits={w:07b} Cbits={c:07b} Qbits={q_mask:07b}"
                    )
                elif pred and md is not None and md != 2:
                    viol_chart_but_not_d2.append(
                        f"i={i} j={j} k={k} md={md} s=2 pred_chart Q={quads[k]} "
                        f"T_i={triples[i]} T_j={triples[j]}"
                    )

                if count_cells_total % 3000 == 0:
                    print(
                        f"progress {count_cells_total}/22050 i={i} j={j} k={k} md={md}",
                        flush=True,
                    )

    wall = time.perf_counter() - t0
    print(
        f"grid_done={count_cells_total} wall_sec={wall:.3f} "
        f"stratum_s2_cells={count_stratum_s2} "
        f"stratum_min_d2={count_stratum_d2} stratum_pred={count_stratum_pred}",
        flush=True,
    )

    all_viol = viol_d2_not_in_charts + viol_chart_but_not_d2
    if all_viol:
        for v in viol_d2_not_in_charts[:20]:
            print(f"VIOL_D2_NOT_CHART: {v}", flush=True)
        for v in viol_chart_but_not_d2[:20]:
            print(f"VIOL_CHART_NOT_D2: {v}", flush=True)
        extra = len(all_viol) - 40
        if extra > 0:
            print(f"... and {extra} more violations", flush=True)
        print("FAIL: wedge ∪ complement(symdiff) biconditional broken on s=2", flush=True)
        sys.exit(1)

    print(
        "PASS: for i<j and |T_i∩T_j|=2, min_d=2 iff Q is wedge or complement(symdiff)",
        flush=True,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
