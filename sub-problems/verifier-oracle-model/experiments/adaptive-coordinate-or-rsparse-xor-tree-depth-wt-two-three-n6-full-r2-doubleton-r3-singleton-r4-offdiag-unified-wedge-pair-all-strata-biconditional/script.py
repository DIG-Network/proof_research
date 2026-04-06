#!/usr/bin/env python3
r"""
n=6, shell {2,3,4}: biconditional on all off-diagonal strata s=|T_i∩T_j| in {0,1,2}
using only the ordered wedge pair W_ij ∨ W_ji (no C_ij branch).

Language: coord + full r=2 + two r=3 XOR splits (i<j) + one r=4 XOR split.

For i<j with s = popc(T_i & T_j) in {0,1,2}:

  W_ij = (T_i \ T_j) ∪ ([6] \ (T_i ∪ T_j))
  W_ji = (T_j \ T_i) ∪ ([6] \ (T_i ∪ T_j))

Hypothesis:

  min_d == 2  <=>  (Q_mask == W_ij) or (Q_mask == W_ji)

Exit 0 = PASS; exit 1 = FAIL.
"""

from __future__ import annotations

import importlib.util
import sys
import time
from itertools import combinations
from pathlib import Path

PARENT = Path(__file__).resolve().parents[1] / (
    "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6/script.py"
)

LRU_CAP = 4_000_000
N_EXPECT = 6
FULL_MASK = (1 << N_EXPECT) - 1


def _load_parent():
    spec = importlib.util.spec_from_file_location("n6driver", PARENT)
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


def popc(m: int) -> int:
    return m.bit_count()


def wedge_mask(t_a: int, t_b: int) -> int:
    only_a = t_a & (FULL_MASK ^ t_b)
    union = t_a | t_b
    exterior = FULL_MASK ^ union
    return only_a | exterior


def main() -> None:
    mod = _load_parent()
    assert mod.N == N_EXPECT

    masks = mod.build_masks()
    coord = mod.build_coord_partition_masks(masks)
    p2 = mod.build_r_xor_partition_masks(masks, 2)
    p3 = mod.build_r_xor_partition_masks(masks, 3)
    p4 = mod.build_r_xor_partition_masks(masks, 4)
    assert len(p3) == 20 and len(p4) == 15

    triples = list(combinations(range(N_EXPECT), 3))
    quads = list(combinations(range(N_EXPECT), 4))
    assert len(triples) == 20 and len(quads) == 15

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

    viol_d2_not_pred: list[str] = []
    viol_pred_but_not_d2: list[str] = []

    count_cells_total = 0
    count_stratum = 0
    count_s0 = count_s1 = count_s2 = 0
    count_stratum_d2 = 0
    count_stratum_pred = 0
    count_pred_wij = count_pred_wji = 0

    t0 = time.perf_counter()
    for i in range(len(p3)):
        t_i = subset_mask(triples[i])
        for j in range(i, len(p3)):
            t_j = subset_mask(triples[j])
            for k in range(len(p4)):
                q_mask = subset_mask(quads[k])
                xor_lists = [p2, [p3[i], p3[j]], [p4[k]]]
                md, _ = mod.min_depth_for_language(
                    masks, coord, xor_lists, mod.N, LRU_CAP
                )
                count_cells_total += 1

                if i >= j:
                    continue

                s_inter = popc(t_i & t_j)
                if s_inter not in (0, 1, 2):
                    continue

                count_stratum += 1
                if s_inter == 0:
                    count_s0 += 1
                elif s_inter == 1:
                    count_s1 += 1
                else:
                    count_s2 += 1

                w_ij = wedge_mask(t_i, t_j)
                w_ji = wedge_mask(t_j, t_i)
                hit_ij = q_mask == w_ij
                hit_ji = q_mask == w_ji
                pred = hit_ij or hit_ji
                if pred:
                    count_stratum_pred += 1
                    if hit_ij:
                        count_pred_wij += 1
                    if hit_ji:
                        count_pred_wji += 1

                if md == 2:
                    count_stratum_d2 += 1
                    if not pred:
                        viol_d2_not_pred.append(
                            f"i={i} j={j} k={k} md=2 s={s_inter} Q not in {{W_ij,W_ji}} "
                            f"T_i={triples[i]} T_j={triples[j]} Q={quads[k]} "
                            f"Wij={w_ij:06b} Wji={w_ji:06b} Qbits={q_mask:06b}"
                        )
                elif pred and md is not None and md != 2:
                    viol_pred_but_not_d2.append(
                        f"i={i} j={j} k={k} md={md} s={s_inter} pred_wedges "
                        f"T_i={triples[i]} T_j={triples[j]} Q={quads[k]}"
                    )

                if count_cells_total % 1500 == 0:
                    print(
                        f"progress {count_cells_total}/3150 i={i} j={j} k={k} md={md}",
                        flush=True,
                    )

    wall = time.perf_counter() - t0
    print(
        f"grid_done={count_cells_total} wall_sec={wall:.3f} "
        f"offdiag_s012_cells={count_stratum} (s0={count_s0} s1={count_s1} s2={count_s2}) "
        f"stratum_min_d2={count_stratum_d2} stratum_pred={count_stratum_pred} "
        f"pred_wij={count_pred_wij} pred_wji={count_pred_wji}",
        flush=True,
    )

    all_viol = viol_d2_not_pred + viol_pred_but_not_d2
    print(
        f"viol_counts d2_not_pred={len(viol_d2_not_pred)} "
        f"pred_not_d2={len(viol_pred_but_not_d2)} total={len(all_viol)}",
        flush=True,
    )
    if all_viol:
        for v in viol_d2_not_pred[:20]:
            print(f"VIOL_D2_NOT_PRED: {v}", flush=True)
        for v in viol_pred_but_not_d2[:20]:
            print(f"VIOL_PRED_NOT_D2: {v}", flush=True)
        extra = len(all_viol) - 40
        if extra > 0:
            print(f"... and {extra} more violations", flush=True)
        print(
            "FAIL: unified W_ij∨W_ji biconditional broken on off-diagonal s in {0,1,2}",
            flush=True,
        )
        sys.exit(1)

    print(
        "PASS: for i<j and |T_i∩T_j| in {0,1,2}, min_d=2 iff Q in {W_ij,W_ji}",
        flush=True,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
