#!/usr/bin/env python3
"""
Scan all C(20,2)=190 pairs of r=3 XOR splits at n=6, shell {2,3}, with full r=2 menu.

Uses the parent n=6 driver for masks, partitions, and min_depth DP.
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

    md0, _ = mod.min_depth_for_language(masks, coord, [], N, lru_cap)
    full_par = mod.build_r_xor_partition_masks(masks, N)
    md_full, _ = mod.min_depth_for_language(masks, coord, [full_par], N, lru_cap)
    print(f"baseline coord_only min_d={md0} coord_plus_full_xor min_d={md_full}", flush=True)
    if md_full != 1:
        print("FAIL: full-n-XOR baseline must be 1", flush=True)
        sys.exit(1)

    witnesses: list[tuple[int, int, float]] = []
    t_wall0 = time.perf_counter()
    for i, j in itertools.combinations(range(20), 2):
        xor_lists = [p2, [p3[i], p3[j]]]
        t0 = time.perf_counter()
        md, _ = mod.min_depth_for_language(masks, coord, xor_lists, N, lru_cap)
        dt = time.perf_counter() - t0
        if md == 2:
            witnesses.append((i, j, dt))
    t_wall = time.perf_counter() - t_wall0

    print(f"pairs_scanned=190 wall_sec={t_wall:.3f}", flush=True)
    print(f"witness_count={len(witnesses)} (pairs with min_d=2)", flush=True)
    for i, j, dt in witnesses[:25]:
        print(f"  witness i={i} j={j} dp_sec={dt:.4f}", flush=True)
    if len(witnesses) > 25:
        print(f"  ... {len(witnesses) - 25} more", flush=True)

    if witnesses:
        print("PASS", flush=True)
    else:
        print("FAIL", flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
