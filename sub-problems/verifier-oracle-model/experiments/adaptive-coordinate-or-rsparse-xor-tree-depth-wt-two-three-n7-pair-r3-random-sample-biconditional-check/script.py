#!/usr/bin/env python3
"""
n=7, shell {2,3}: random sample of unordered pairs of r=3 XOR splits.

Tests biconditional (same shape as n=6 exhaustive check):
  min_d(coord + full r=2 + two chosen r=3 splits) == 2  <=>  the two triples are disjoint.

C(7,3)=35 triples => C(35,2)=595 pairs; we sample SAMPLE_PAIRS with RNG seed SEED
for cron-friendly wall time (not an exhaustive 595 proof).
"""

from __future__ import annotations

import importlib.util
import itertools
import random
import sys
import time
from pathlib import Path

PARENT = Path(__file__).resolve().parents[1] / (
    "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py"
)

SEED = 0
SAMPLE_PAIRS = 200
LRU_CAP = 4_000_000


def _load_parent():
    spec = importlib.util.spec_from_file_location("n7driver", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PARENT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    mod = _load_parent()
    n = mod.N
    assert n == 7

    masks = mod.build_masks()
    coord = mod.build_coord_partition_masks(masks)
    p2 = mod.build_r_xor_partition_masks(masks, 2)
    p3 = mod.build_r_xor_partition_masks(masks, 3)
    assert len(p3) == 35

    triples = list(itertools.combinations(range(n), 3))
    assert len(triples) == 35

    md0, _ = mod.min_depth_for_language(masks, coord, [], n, LRU_CAP)
    full_par = mod.build_r_xor_partition_masks(masks, n)
    md_full, _ = mod.min_depth_for_language(masks, coord, [full_par], n, LRU_CAP)
    print(
        f"baseline coord_only min_d={md0} coord_plus_full_xor min_d={md_full}",
        flush=True,
    )
    if md_full != 1:
        print("FAIL: full-n-XOR baseline must be 1", flush=True)
        sys.exit(1)

    all_pairs = list(itertools.combinations(range(35), 2))
    assert len(all_pairs) == 595
    rng = random.Random(SEED)
    k = min(SAMPLE_PAIRS, len(all_pairs))
    sampled = rng.sample(all_pairs, k)

    violations: list[tuple[int, int, bool, int]] = []
    t_wall0 = time.perf_counter()
    for i, j in sampled:
        disjoint = not (set(triples[i]) & set(triples[j]))
        xor_lists = [p2, [p3[i], p3[j]]]
        md, _ = mod.min_depth_for_language(masks, coord, xor_lists, n, LRU_CAP)
        pred_two = disjoint
        actual_two = md == 2
        if pred_two != actual_two:
            violations.append((i, j, disjoint, md if md is not None else -1))
    t_wall = time.perf_counter() - t_wall0

    print(f"seed={SEED} sample_pairs={k} total_universe=595 wall_sec={t_wall:.3f}", flush=True)
    print(f"violations={len(violations)}", flush=True)
    for row in violations[:30]:
        print(
            f"  i={row[0]} j={row[1]} disjoint={row[2]} min_d={row[3]}",
            flush=True,
        )
    if len(violations) > 30:
        print(f"  ... {len(violations) - 30} more", flush=True)

    if violations:
        print("FAIL", flush=True)
        sys.exit(1)
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
