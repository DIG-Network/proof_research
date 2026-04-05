#!/usr/bin/env python3
r"""
n=7, shell {2,3}: global off-diagonal biconditional for a stratified |∩|-predicate.

Language: coord + full r=2 + two r=3 XOR splits (i<j in analysis) + one r=4 XOR split.

For distinct triple indices i<j, let s = popc(T_i & T_j) in {0,1,2}.

Define:
  W_ij = (T_i \ T_j) ∪ ([7] \ (T_i ∪ T_j))
  W_ji = (T_j \ T_i) ∪ ([7] \ (T_i ∪ T_j))
  C_ij = [7] \ (T_i ⊕ T_j)

Stratified predicate P(i,j,Q):
  - if s in {0,1}: (Q == W_ij) or (Q == W_ji)
  - if s == 2:     (Q == W_ij) or (Q == C_ij)

Hypothesis (global off-diagonal): min_d == 2  <=>  P(i,j,Q).

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


def popc(m: int) -> int:
    return m.bit_count()


def wedge_mask(t_a: int, t_b: int) -> int:
    only_a = t_a & (FULL_MASK ^ t_b)
    union = t_a | t_b
    exterior = FULL_MASK ^ union
    return only_a | exterior


def complement_symdiff_mask(t_i: int, t_j: int) -> int:
    return FULL_MASK ^ (t_i ^ t_j)


def stratified_pred(t_i: int, t_j: int, q_mask: int) -> bool:
    s_inter = popc(t_i & t_j)
    w_ij = wedge_mask(t_i, t_j)
    w_ji = wedge_mask(t_j, t_i)
    if s_inter in (0, 1):
        return q_mask == w_ij or q_mask == w_ji
    if s_inter == 2:
        c_ij = complement_symdiff_mask(t_i, t_j)
        return q_mask == w_ij or q_mask == c_ij
    raise AssertionError(f"unexpected |∩|={s_inter} for distinct 3-subsets of [7]")


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

    viol_d2_not_pred: list[str] = []
    viol_pred_but_not_d2: list[str] = []

    count_cells_total = 0
    count_offdiag = 0
    count_offdiag_s01 = 0
    count_offdiag_s2 = 0
    count_offdiag_d2 = 0
    count_offdiag_pred = 0

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

                count_offdiag += 1
                s_inter = popc(t_i & t_j)
                if s_inter in (0, 1):
                    count_offdiag_s01 += 1
                elif s_inter == 2:
                    count_offdiag_s2 += 1
                else:
                    raise AssertionError(f"unexpected s={s_inter} for i<j")

                pred = stratified_pred(t_i, t_j, q_mask)
                if pred:
                    count_offdiag_pred += 1

                if md == 2:
                    count_offdiag_d2 += 1
                    if not pred:
                        w_ij = wedge_mask(t_i, t_j)
                        w_ji = wedge_mask(t_j, t_i)
                        c_ij = complement_symdiff_mask(t_i, t_j)
                        viol_d2_not_pred.append(
                            f"i={i} j={j} k={k} md=2 s={s_inter} strat_pred=False "
                            f"T_i={triples[i]} T_j={triples[j]} Q={quads[k]} "
                            f"Wij={w_ij:07b} Wji={w_ji:07b} Cij={c_ij:07b} Qbits={q_mask:07b}"
                        )
                elif pred and md is not None and md != 2:
                    viol_pred_but_not_d2.append(
                        f"i={i} j={j} k={k} md={md} s={s_inter} strat_pred=True "
                        f"T_i={triples[i]} T_j={triples[j]} Q={quads[k]}"
                    )

                if count_cells_total % 3000 == 0:
                    print(
                        f"progress {count_cells_total}/22050 i={i} j={j} k={k} md={md}",
                        flush=True,
                    )

    wall = time.perf_counter() - t0
    print(
        f"grid_done={count_cells_total} wall_sec={wall:.3f} "
        f"offdiag_cells={count_offdiag} (s01={count_offdiag_s01} s2={count_offdiag_s2}) "
        f"offdiag_min_d2={count_offdiag_d2} offdiag_pred={count_offdiag_pred}",
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
            "FAIL: stratified |∩| predicate biconditional broken on off-diagonal grid",
            flush=True,
        )
        sys.exit(1)

    print(
        "PASS: off-diagonal min_d=2 iff stratified predicate (s01 wedge∨rev; s2 wedge∨C)",
        flush=True,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
