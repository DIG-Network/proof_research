#!/usr/bin/env python3
r"""
n=8, shell {2,3,4}: structure scan on the off-diagonal s=|T_i∩T_j| in {0,1,2} grid.

Base language: coord + full r=2 + doubleton r=3 + singleton r=4 (same as wedge ports).

For each *strict* nonempty subset of the full r=5, r=6, r=7 XOR menus (6 masks),
recompute min_d on all 111_720 coarse cells and aggregate on the s∈{0,1,2} stratum:

  - stratum_min_d2 count
  - wedge predicate hits (Q in {W_ij,W_ji})
  - biconditional violation counts (for diagnostics)

Hypothesis (see hypothesis.md): some mask has 0 < stratum_min_d2 < 107800.

Exit 0 if such a mask exists; exit 1 if every mask yields stratum_min_d2 in {0,107800}.
"""

from __future__ import annotations

import importlib.util
import sys
import time
from itertools import combinations
from pathlib import Path

PARENT = Path(__file__).resolve().parents[1] / (
    "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8/script.py"
)

LRU_CAP = 4_000_000
N_EXPECT = 8
FULL_MASK = (1 << N_EXPECT) - 1

# bit0=r5, bit1=r6, bit2=r7; exclude 0 (no high menus) and 7 (full triple) for strict-subset scan
STRICT_SUBSET_MASKS = [m for m in range(1, 7) if m != 7]
assert STRICT_SUBSET_MASKS == [1, 2, 3, 4, 5, 6]


def _load_parent():
    spec = importlib.util.spec_from_file_location("n8driver", PARENT)
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


def mask_label(m: int) -> str:
    parts = []
    if m & 1:
        parts.append("r5")
    if m & 2:
        parts.append("r6")
    if m & 4:
        parts.append("r7")
    return "+".join(parts) if parts else "none"


def run_one_high_mask(
    mod,
    masks: list[int],
    coord: list[tuple[int, int]],
    p2: list[tuple[int, int]],
    p3: list[tuple[int, int]],
    p4: list[tuple[int, int]],
    p5: list[tuple[int, int]],
    p6: list[tuple[int, int]],
    p7: list[tuple[int, int]],
    high_mask: int,
) -> tuple[int, int, int, int, float]:
    triples = list(combinations(range(N_EXPECT), 3))
    quads = list(combinations(range(N_EXPECT), 4))

    viol_d2_not_pred = 0
    viol_pred_but_not_d2 = 0
    count_stratum = 0
    count_stratum_d2 = 0
    count_stratum_pred = 0

    t0 = time.perf_counter()
    for i in range(len(p3)):
        for j in range(i, len(p3)):
            for k in range(len(p4)):
                xor_lists: list[list[tuple[int, int]]] = [
                    p2,
                    [p3[i], p3[j]],
                    [p4[k]],
                ]
                if high_mask & 1:
                    xor_lists.append(p5)
                if high_mask & 2:
                    xor_lists.append(p6)
                if high_mask & 4:
                    xor_lists.append(p7)

                md, _ = mod.min_depth_for_language(
                    masks, coord, xor_lists, mod.N, LRU_CAP
                )

                if i >= j:
                    continue

                t_i = subset_mask(triples[i])
                t_j = subset_mask(triples[j])
                q_mask = subset_mask(quads[k])

                s_inter = popc(t_i & t_j)
                if s_inter not in (0, 1, 2):
                    continue

                count_stratum += 1
                w_ij = wedge_mask(t_i, t_j)
                w_ji = wedge_mask(t_j, t_i)
                pred = (q_mask == w_ij) or (q_mask == w_ji)
                if pred:
                    count_stratum_pred += 1

                if md == 2:
                    count_stratum_d2 += 1
                    if not pred:
                        viol_d2_not_pred += 1
                elif pred and md is not None and md != 2:
                    viol_pred_but_not_d2 += 1

                if (i * len(p3) * len(p4) + j * len(p4) + k) % 8000 == 0:
                    print(
                        f"  progress high_mask={high_mask:#b} cell={i},{j},{k} md={md}",
                        flush=True,
                    )

    wall = time.perf_counter() - t0
    return (
        count_stratum_d2,
        count_stratum_pred,
        viol_d2_not_pred,
        viol_pred_but_not_d2,
        wall,
    )


def main() -> None:
    mod = _load_parent()
    assert mod.N == N_EXPECT

    masks = mod.build_masks()
    coord = mod.build_coord_partition_masks(masks)
    p2 = mod.build_r_xor_partition_masks(masks, 2)
    p3 = mod.build_r_xor_partition_masks(masks, 3)
    p4 = mod.build_r_xor_partition_masks(masks, 4)
    p5 = mod.build_r_xor_partition_masks(masks, 5)
    p6 = mod.build_r_xor_partition_masks(masks, 6)
    p7 = mod.build_r_xor_partition_masks(masks, 7)
    assert len(p3) == 56 and len(p4) == 70
    assert len(p5) == 56 and len(p6) == 28 and len(p7) == 8

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

    print("high_maskbits label stratum_min_d2 stratum_pred viol_d2_not_pred viol_pred_not_d2 wall_sec", flush=True)
    found_proper = False
    for hm in STRICT_SUBSET_MASKS:
        d2, pred_hits, v_d2, v_pd, wall = run_one_high_mask(
            mod, masks, coord, p2, p3, p4, p5, p6, p7, hm
        )
        label = mask_label(hm)
        print(
            f"{hm:#b} {label} {d2} {pred_hits} {v_d2} {v_pd} {wall:.3f}",
            flush=True,
        )
        if 0 < d2 < 107_800:
            found_proper = True

    print(f"STRATUM_TOTAL=107800 proper_nonempty_proper={found_proper}", flush=True)
    if found_proper:
        print(
            "PASS: at least one strict subset of {r5,r6,r7} yields 0<stratum_min_d2<107800",
            flush=True,
        )
        sys.exit(0)
    print(
        "FAIL: every strict subset yields stratum_min_d2 in {0,107800} on this stratum",
        flush=True,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
