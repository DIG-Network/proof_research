#!/usr/bin/env python3
"""
n=7, shell {2,3}: coord + full r=2 XOR + one r=3 XOR + one r=4 XOR (grid scan).

Enumerates all 35×35 pairs of (r3_index, r4_index). Tallies min_d==2 vs min_d>=3.

Exit 0 = PASS (exists at least one pair with min_d>=3).
Exit 1 = FAIL (all 1225 pairs have min_d==2).

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

    witnesses_ge3: list[tuple[int, int, int, float]] = []
    count_d2 = 0
    t_wall0 = time.perf_counter()
    total = len(p3) * len(p4)
    done = 0
    for i in range(len(p3)):
        for j in range(len(p4)):
            xor_lists = [p2, [p3[i]], [p4[j]]]
            n_splits = len(p2) + 1 + 1
            t0 = time.perf_counter()
            md, _ = mod.min_depth_for_language(masks, coord, xor_lists, mod.N, LRU_CAP)
            dt = time.perf_counter() - t0
            done += 1
            if md == 2:
                count_d2 += 1
            elif md is not None and md >= 3:
                witnesses_ge3.append((i, j, md, dt))
            if done % 200 == 0 or done == total:
                print(
                    f"progress {done}/{total} r3_idx={i} r4_idx={j} "
                    f"min_d={md} dp_sec={dt:.6f}",
                    flush=True,
                )

    t_wall = time.perf_counter() - t_wall0
    print(
        f"grid_done={total} lru_cap={LRU_CAP} wall_sec={t_wall:.3f}",
        flush=True,
    )
    print(
        f"min_d_eq2_count={count_d2} min_d_ge3_count={len(witnesses_ge3)}",
        flush=True,
    )
    for i, j, md, dt in witnesses_ge3[:50]:
        print(
            f"  witness_ge3 r3_index={i} r4_index={j} min_d={md} dp_sec={dt:.6f}",
            flush=True,
        )
    if len(witnesses_ge3) > 50:
        print(f"  ... {len(witnesses_ge3) - 50} more", flush=True)

    if witnesses_ge3:
        print(
            "PASS: at least one (r3,r4) pair achieves min_d>=3 "
            f"({len(witnesses_ge3)}/{total})",
            flush=True,
        )
        sys.exit(0)
    print(
        "FAIL: hypothesis falsified — every singleton r3 + singleton r4 grid cell "
        f"has min_d=2 ({count_d2}/{total})",
        flush=True,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
