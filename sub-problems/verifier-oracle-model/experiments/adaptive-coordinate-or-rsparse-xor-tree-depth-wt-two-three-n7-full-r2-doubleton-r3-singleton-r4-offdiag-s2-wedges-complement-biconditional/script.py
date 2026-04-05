#!/usr/bin/env python3
r"""
n=7, shell {2,3}: biconditional on the s=2 off-diagonal stratum for W∨W_rev∨C.

Language: coord + full r=2 + two r=3 XOR splits (i<j in analysis) + one r=4 XOR split.

Restrict to distinct triple indices i<j with s = popc(T_i & T_j) == 2.

Define:
  W_ij = (T_i \ T_j) ∪ ([7] \ (T_i ∪ T_j))
  W_ji = (T_j \ T_i) ∪ ([7] \ (T_i ∪ T_j))
  C_ij = [7] \ (T_i ⊕ T_j)

Hypothesis on this stratum:

  min_d == 2  <=>  (Q == W_ij) or (Q == W_ji) or (Q == C_ij)

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


def pred_s2(t_i: int, t_j: int, q_mask: int) -> bool:
    w_ij = wedge_mask(t_i, t_j)
    w_ji = wedge_mask(t_j, t_i)
    c_ij = complement_symdiff_mask(t_i, t_j)
    return q_mask == w_ij or q_mask == w_ji or q_mask == c_ij


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
    count_s2 = 0
    count_s2_d2 = 0
    count_s2_pred = 0
    count_s2_pred_wij = 0
    count_s2_pred_wji = 0
    count_s2_pred_c = 0

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
                if s_inter != 2:
                    continue

                count_s2 += 1
                w_ij = wedge_mask(t_i, t_j)
                w_ji = wedge_mask(t_j, t_i)
                c_ij = complement_symdiff_mask(t_i, t_j)
                hit_wij = q_mask == w_ij
                hit_wji = q_mask == w_ji
                hit_c = q_mask == c_ij
                pred = hit_wij or hit_wji or hit_c
                if pred:
                    count_s2_pred += 1
                    if hit_wij:
                        count_s2_pred_wij += 1
                    if hit_wji:
                        count_s2_pred_wji += 1
                    if hit_c:
                        count_s2_pred_c += 1

                if md == 2:
                    count_s2_d2 += 1
                    if not pred:
                        viol_d2_not_pred.append(
                            f"i={i} j={j} k={k} md=2 s=2 pred=False "
                            f"T_i={triples[i]} T_j={triples[j]} Q={quads[k]} "
                            f"Wij={w_ij:07b} Wji={w_ji:07b} Cij={c_ij:07b} Qbits={q_mask:07b}"
                        )
                elif pred and md is not None and md != 2:
                    viol_pred_but_not_d2.append(
                        f"i={i} j={j} k={k} md={md} s=2 pred_triple "
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
        f"s2_cells={count_s2} s2_min_d2={count_s2_d2} s2_pred={count_s2_pred} "
        f"pred_wij={count_s2_pred_wij} pred_wji={count_s2_pred_wji} pred_c={count_s2_pred_c}",
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
            "FAIL: s=2 stratum biconditional broken for W∨W_rev∨C",
            flush=True,
        )
        sys.exit(1)

    print(
        "PASS: for i<j and |T_i∩T_j|=2, min_d=2 iff Q in {W_ij,W_ji,C_ij}",
        flush=True,
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
