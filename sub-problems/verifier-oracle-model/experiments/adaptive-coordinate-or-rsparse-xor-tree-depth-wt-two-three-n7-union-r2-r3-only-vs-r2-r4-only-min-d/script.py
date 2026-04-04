#!/usr/bin/env python3
"""
n=7 {2,3}: compare XOR unions

  (A) r in {2,3} only  — 21 + 35 = 56 splits
  (B) r in {2,4} only  — 21 + 35 = 56 splits

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py

Primary hypothesis: (A) has min_d >= 3 (full r=4 menu needed vs dropping it).
Exit 0 = PASS primary (min_d >= 3 for {2,3}).
Exit 1 = FAIL primary (min_d == 2 for {2,3}).
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


def _run_union(
    mod, rs: list[int], label: str
) -> tuple[int | None, int, float]:
    masks = mod.build_masks()
    coord = mod.build_coord_partition_masks(masks)
    xor_lists = [mod.build_r_xor_partition_masks(masks, r) for r in rs]
    total = sum(len(x) for x in xor_lists)
    t0 = time.perf_counter()
    md, _ = mod.min_depth_for_language(masks, coord, xor_lists, mod.N, LRU_CAP)
    dt = time.perf_counter() - t0
    print(
        f"{label} union_rs={rs} total_splits={total} min_d={md} "
        f"dp_sec={dt:.6f} lru_cap={LRU_CAP}",
        flush=True,
    )
    return md, total, dt


def main() -> None:
    mod = _load_parent()
    assert mod.N == N_EXPECT

    masks = mod.build_masks()
    coord = mod.build_coord_partition_masks(masks)
    full_par = mod.build_r_xor_partition_masks(masks, mod.N)
    md0, _ = mod.min_depth_for_language(masks, coord, [], mod.N, LRU_CAP)
    md_full, _ = mod.min_depth_for_language(masks, coord, [full_par], mod.N, LRU_CAP)
    print(f"baseline coord_only min_d={md0} coord_plus_full_xor min_d={md_full}", flush=True)
    if md_full != 1:
        print("FAIL: full-n-XOR baseline must be 1", flush=True)
        sys.exit(1)

    md_23, tot_23, _ = _run_union(mod, [2, 3], "case_A_r2_r3_only")
    md_24, tot_24, _ = _run_union(mod, [2, 4], "case_B_r2_r4_only")

    assert tot_23 == 56 and tot_24 == 56

    print(
        f"summary min_d_r2_r3_only={md_23} min_d_r2_r4_only={md_24}",
        flush=True,
    )

    if md_23 is None or md_23 < 3:
        print("FAIL: primary hypothesis falsified (expected min_d>=3 for {2,3} only)", flush=True)
        sys.exit(1)

    print("PASS: primary confirmed (min_d>=3 for union {2,3} only)", flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
