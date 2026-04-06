#!/usr/bin/env python3
r"""
n=8, shell {2,3,4}: random partial r=5 submenu (K=2 of 56 splits) — off-diagonal s012 structure scan.

Base language: coord + full r=2 + doubleton r=3 + singleton r=4 (same grid as partial r5/r6/r7 scans).

For each of NUM_TRIALS independent RNG draws (SEED), sample K_P5 distinct indices into the full
r=5 XOR split list (len=56), append those splits only, and aggregate on the s∈{0,1,2} stratum:

  - stratum_min_d2 count
  - wedge predicate hits (diagnostic)
  - biconditional violation counts

Hypothesis: some trial yields 0 < stratum_min_d2 < 107800.

Exit 0 if such a trial exists; exit 1 otherwise.
"""

from __future__ import annotations

import importlib.util
import random
import sys
import time
from itertools import combinations
from pathlib import Path

PARENT = Path(__file__).resolve().parents[1] / (
    "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8/script.py"
)

SEED = 0
NUM_TRIALS = 16
K_P5 = 2
LRU_CAP = 4_000_000
N_EXPECT = 8
FULL_MASK = (1 << N_EXPECT) - 1
STRATUM_TOTAL = 107_800


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


def run_one_trial(
    mod,
    masks: list[int],
    coord: list[tuple[int, int]],
    p2: list[tuple[int, int]],
    p3: list[tuple[int, int]],
    p4: list[tuple[int, int]],
    p5: list[tuple[int, int]],
    p5_idx: tuple[int, ...],
) -> tuple[int, int, int, int, float]:
    triples = list(combinations(range(N_EXPECT), 3))
    quads = list(combinations(range(N_EXPECT), 4))

    viol_d2_not_pred = 0
    viol_pred_but_not_d2 = 0
    count_stratum_d2 = 0
    count_stratum_pred = 0

    partial_p5 = [p5[i] for i in p5_idx]

    t0 = time.perf_counter()
    for i in range(len(p3)):
        for j in range(i, len(p3)):
            for k in range(len(p4)):
                xor_lists: list[list[tuple[int, int]]] = [
                    p2,
                    [p3[i], p3[j]],
                    [p4[k]],
                    partial_p5,
                ]

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
    assert len(p3) == 56 and len(p4) == 70 and len(p5) == 56

    if K_P5 <= 0 or K_P5 > len(p5):
        print(f"FAIL: need 0 < K_P5 <= {len(p5)}", flush=True)
        sys.exit(1)

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

    rng = random.Random(SEED)
    universe = list(range(len(p5)))

    print(
        "trial p5_indices stratum_min_d2 stratum_pred viol_d2_not_pred viol_pred_not_d2 wall_sec",
        flush=True,
    )
    found_proper = False
    total_wall = 0.0
    min_d2_over_trials = STRATUM_TOTAL + 1
    max_d2_over_trials = -1
    for t in range(1, NUM_TRIALS + 1):
        idx_tuple = tuple(sorted(rng.sample(universe, K_P5)))
        d2, pred_hits, v_d2, v_pd, wall = run_one_trial(
            mod, masks, coord, p2, p3, p4, p5, idx_tuple
        )
        total_wall += wall
        min_d2_over_trials = min(min_d2_over_trials, d2)
        max_d2_over_trials = max(max_d2_over_trials, d2)
        print(
            f"{t} {idx_tuple} {d2} {pred_hits} {v_d2} {v_pd} {wall:.3f}",
            flush=True,
        )
        if 0 < d2 < STRATUM_TOTAL:
            found_proper = True

    print(
        f"STRATUM_TOTAL={STRATUM_TOTAL} trials={NUM_TRIALS} k_p5={K_P5} seed={SEED} "
        f"proper_nonempty_proper={found_proper} total_wall_sec={total_wall:.3f} "
        f"min_stratum_d2_across_trials={min_d2_over_trials} "
        f"max_stratum_d2_across_trials={max_d2_over_trials}",
        flush=True,
    )
    if found_proper:
        print(
            "PASS: at least one partial r=5 K=2 draw yields 0<stratum_min_d2<107800",
            flush=True,
        )
        sys.exit(0)
    print(
        "FAIL: every trial yields stratum_min_d2 in {0,107800} on this stratum",
        flush=True,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
