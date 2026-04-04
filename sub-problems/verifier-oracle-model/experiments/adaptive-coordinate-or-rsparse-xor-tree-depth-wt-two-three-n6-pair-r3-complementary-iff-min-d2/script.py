#!/usr/bin/env python3
"""
Verify biconditional at n=6, shell {2,3}:

  min_d(coord + full r=2 + two r=3 splits) == 2  <=>  the two triples are disjoint
  (equivalently: complementary 3+3 partition of [6], since |triple|=3).

Reuses parent n=6 driver DP (same LRU cap as pair scan).
"""

from __future__ import annotations

import importlib.util
import itertools
import sys
import time
from pathlib import Path

PARENT = Path(__file__).resolve().parents[1] / (
    "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6/script.py"
)


def _load_parent():
    spec = importlib.util.spec_from_file_location("n6driver", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PARENT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    mod = _load_parent()
    N = mod.N
    lru_cap = 4_000_000

    masks = mod.build_masks()
    coord = mod.build_coord_partition_masks(masks)
    p2 = mod.build_r_xor_partition_masks(masks, 2)
    p3 = mod.build_r_xor_partition_masks(masks, 3)
    assert len(p3) == 20

    triples = list(itertools.combinations(range(N), 3))
    assert len(triples) == 20

    md0, _ = mod.min_depth_for_language(masks, coord, [], N, lru_cap)
    full_par = mod.build_r_xor_partition_masks(masks, N)
    md_full, _ = mod.min_depth_for_language(masks, coord, [full_par], N, lru_cap)
    print(f"baseline coord_only min_d={md0} coord_plus_full_xor min_d={md_full}", flush=True)
    if md_full != 1:
        print("FAIL: full-n-XOR baseline must be 1", flush=True)
        sys.exit(1)

    violations: list[tuple[int, int, bool, int]] = []
    t_wall0 = time.perf_counter()
    for i, j in itertools.combinations(range(20), 2):
        disjoint = not (set(triples[i]) & set(triples[j]))
        xor_lists = [p2, [p3[i], p3[j]]]
        md, _ = mod.min_depth_for_language(masks, coord, xor_lists, N, lru_cap)
        pred_two = disjoint
        actual_two = md == 2
        if pred_two != actual_two:
            violations.append((i, j, disjoint, md))
    t_wall = time.perf_counter() - t_wall0

    print(f"pairs_checked=190 wall_sec={t_wall:.3f}", flush=True)
    print(f"violations={len(violations)}", flush=True)
    for row in violations[:20]:
        print(f"  i={row[0]} j={row[1]} disjoint={row[2]} min_d={row[3]}", flush=True)
    if len(violations) > 20:
        print(f"  ... {len(violations) - 20} more", flush=True)

    if violations:
        print("FAIL", flush=True)
        sys.exit(1)
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
