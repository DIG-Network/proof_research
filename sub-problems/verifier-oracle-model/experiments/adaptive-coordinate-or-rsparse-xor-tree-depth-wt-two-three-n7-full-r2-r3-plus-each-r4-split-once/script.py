#!/usr/bin/env python3
"""
n=7, shell {2,3}: coord + full r=2 XOR + full r=3 XOR + one r=4 XOR split at a time.

Scans all C(7,4)=35 quartic XOR partitions. Tallies how many yield min_d==2 vs min_d>=3.
Exit 0 if hypothesis confirmed (no min_d==2); exit 1 if any min_d==2 (falsified).

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py
"""

from __future__ import annotations

import importlib.util
import sys
import time
from pathlib import Path

PARENT = Path(__file__).resolve().parents[1] / (
    "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py"
)

LRU_CAP = 4_000_000
N_EXPECT = 7


def _load_parent():
    spec = importlib.util.spec_from_file_location("n7driver", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PARENT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    mod = _load_parent()
    assert mod.N == N_EXPECT

    masks = mod.build_masks()
    coord = mod.build_coord_partition_masks(masks)
    full_par = mod.build_r_xor_partition_masks(masks, mod.N)
    md0, _ = mod.min_depth_for_language(masks, coord, [], mod.N, LRU_CAP)
    md_full, _ = mod.min_depth_for_language(masks, coord, [full_par], mod.N, LRU_CAP)
    print(
        f"baseline coord_only min_d={md0} coord_plus_full_xor min_d={md_full}",
        flush=True,
    )
    if md_full != 1:
        print("FAIL: full-n-XOR baseline must be 1", flush=True)
        sys.exit(1)

    p2 = mod.build_r_xor_partition_masks(masks, 2)
    p3 = mod.build_r_xor_partition_masks(masks, 3)
    p4 = mod.build_r_xor_partition_masks(masks, 4)
    assert len(p2) == 21 and len(p3) == 35 and len(p4) == 35

    witnesses: list[tuple[int, float]] = []
    min_d3_count = 0
    t_wall0 = time.perf_counter()
    checked = 0
    for k in range(len(p4)):
        xor_lists = [p2, p3, [p4[k]]]
        total = len(p2) + len(p3) + 1
        t0 = time.perf_counter()
        md, _ = mod.min_depth_for_language(masks, coord, xor_lists, mod.N, LRU_CAP)
        dt = time.perf_counter() - t0
        checked = k + 1
        print(
            f"r4_index={k} total_splits={total} min_d={md} dp_sec={dt:.6f}",
            flush=True,
        )
        if md == 2:
            witnesses.append((k, dt))
        elif md is not None and md >= 3:
            min_d3_count += 1
    t_wall = time.perf_counter() - t_wall0

    print(
        f"r4_checked={checked} lru_cap={LRU_CAP} wall_sec={t_wall:.3f}",
        flush=True,
    )
    print(
        f"witness_min_d2_count={len(witnesses)} min_d_ge3_count={min_d3_count}",
        flush=True,
    )
    for idx, dt in witnesses[:40]:
        print(f"  witness r4_index={idx} dp_sec={dt:.6f}", flush=True)
    if len(witnesses) > 40:
        print(f"  ... {len(witnesses) - 40} more", flush=True)

    # Exit 0 = primary hypothesis confirmed (no singleton r=4 split achieves min_d=2).
    if witnesses:
        print(
            "FAIL: hypothesis falsified — every singleton r=4 augment yields min_d=2 "
            f"({len(witnesses)}/35)",
            flush=True,
        )
        sys.exit(1)
    print("PASS: primary confirmed (all 35 singleton r=4 augments keep min_d>=3)", flush=True)


if __name__ == "__main__":
    main()
