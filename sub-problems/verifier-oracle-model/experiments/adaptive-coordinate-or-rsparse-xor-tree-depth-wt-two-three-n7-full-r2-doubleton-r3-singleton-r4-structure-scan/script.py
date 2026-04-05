#!/usr/bin/env python3
"""
n=7, shell {2,3}: scan languages

  coord + full r=2 + two r=3 XOR splits (unordered pair of indices, repetition allowed)
            + one r=4 XOR split

Grid size: C(35+1,2) * 35 = 630 * 35 = 22050 cells.

Reports distribution of min_d and whether any cell with distinct triple indices (i<j)
achieves min_d==2.

Exit 0 = PASS (scan completed, baselines OK).
Exit 1 = FAIL (baseline or runtime error).
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
    p2 = mod.build_r_xor_partition_masks(masks, 2)
    p3 = mod.build_r_xor_partition_masks(masks, 3)
    p4 = mod.build_r_xor_partition_masks(masks, 4)
    assert len(p3) == 35 and len(p4) == 35

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

    # Count min_d frequencies
    freq: dict[int | None, int] = {}
    d2_distinct = 0  # i<j and md==2
    d2_duplicate = 0  # i==j and md==2
    d2_total = 0
    sample_distinct_d2: list[str] = []

    t0 = time.perf_counter()
    total = 0
    for i in range(len(p3)):
        for j in range(i, len(p3)):
            for k in range(len(p4)):
                xor_lists = [p2, [p3[i], p3[j]], [p4[k]]]
                md, _ = mod.min_depth_for_language(
                    masks, coord, xor_lists, mod.N, LRU_CAP
                )
                freq[md] = freq.get(md, 0) + 1
                total += 1
                if md == 2:
                    d2_total += 1
                    if i < j:
                        d2_distinct += 1
                        if len(sample_distinct_d2) < 8:
                            sample_distinct_d2.append(
                                f"i={i} j={j} k={k} md={md}"
                            )
                    else:
                        d2_duplicate += 1

                if total % 3000 == 0:
                    print(f"progress {total}/22050 last_i={i} j={j} k={k} md={md}", flush=True)

    wall = time.perf_counter() - t0
    print(f"grid_done={total} wall_sec={wall:.3f}", flush=True)
    print("min_d histogram:", flush=True)
    for key in sorted((x for x in freq if x is not None), key=lambda x: int(x)):  # type: ignore[arg-type, return-value]
        print(f"  min_d={key}: {freq[key]}", flush=True)
    if None in freq:
        print(f"  min_d=None: {freq[None]}", flush=True)

    print(
        f"min_d==2 total={d2_total} duplicate_diag i==j count={d2_duplicate} "
        f"distinct_pair i<j count={d2_distinct}",
        flush=True,
    )
    if d2_distinct:
        print("samples distinct-pair min_d==2:", flush=True)
        for s in sample_distinct_d2:
            print(f"  {s}", flush=True)

    print("PASS", flush=True)


if __name__ == "__main__":
    main()
