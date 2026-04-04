#!/usr/bin/env python3
"""
Exhaustive scan at n=7, shell {2,3}:

  coord + full r=2 XOR menu + four r=3 XOR splits (unordered quadruple of triple indices).

C(7,3)=35 triples => C(35,4)=52360 unordered quadruples.
"""

from __future__ import annotations

import importlib.util
import itertools
import sys
import time
from pathlib import Path

PARENT = Path(__file__).resolve().parents[1] / (
    "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py"
)

LRU_CAP = 4_000_000
PROGRESS_EVERY = 5_000


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

    witnesses: list[tuple[int, int, int, int, float]] = []
    t_wall0 = time.perf_counter()
    ncomb = 0
    for i, j, k, ell in itertools.combinations(range(35), 4):
        ncomb += 1
        if ncomb % PROGRESS_EVERY == 0:
            print(f"progress quads_checked={ncomb}", flush=True)
        xor_lists = [p2, [p3[i], p3[j], p3[k], p3[ell]]]
        t0 = time.perf_counter()
        md, _ = mod.min_depth_for_language(masks, coord, xor_lists, n, LRU_CAP)
        dt = time.perf_counter() - t0
        if md == 2:
            witnesses.append((i, j, k, ell, dt))
    t_wall = time.perf_counter() - t_wall0

    print(f"quads_checked={ncomb} lru_cap={LRU_CAP} wall_sec={t_wall:.3f}", flush=True)
    print(f"witness_min_d2_count={len(witnesses)}", flush=True)
    for row in witnesses[:40]:
        i, j, k, ell, dt = row
        print(f"  witness i={i} j={j} k={k} ell={ell} dp_sec={dt:.4f}", flush=True)
    if len(witnesses) > 40:
        print(f"  ... {len(witnesses) - 40} more", flush=True)

    if witnesses:
        print("PASS", flush=True)
    else:
        print("FAIL", flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
