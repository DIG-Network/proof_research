#!/usr/bin/env python3
"""
n=9, popcount in {4,5} (C(9,4)+C(9,5)=252 masks). Majority t=5, n=2t-1.

Same DP as n=8 experiment (096): coord + r-sparse XOR, full n-XOR, unions.
"""

from __future__ import annotations

import argparse
import sys
import time
from functools import lru_cache
from itertools import combinations

N = 9
SHELLS = (4, 5)


def popc(m: int) -> int:
    return m.bit_count()


def build_masks() -> list[int]:
    masks = [m for m in range(1 << N) if popc(m) in SHELLS]
    assert len(masks) == 252
    return masks


def _lowbit_index(lsb: int) -> int:
    return lsb.bit_length() - 1


def pure_bits(bits: int, masks: list[int]) -> bool:
    if bits == 0:
        return True
    first_w: int | None = None
    b = bits
    while b:
        lsb = b & -b
        k = _lowbit_index(lsb)
        w = popc(masks[k])
        if first_w is None:
            first_w = w
        elif w != first_w:
            return False
        b ^= lsb
    return True


def build_coord_partition_masks(masks: list[int]) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for i in range(N):
        b0 = 0
        b1 = 0
        for k, m in enumerate(masks):
            if (m >> i) & 1:
                b1 |= 1 << k
            else:
                b0 |= 1 << k
        out.append((b0, b1))
    return out


def build_r_xor_partition_masks(masks: list[int], r: int) -> list[tuple[int, int]]:
    dom = len(masks)
    full = (1 << dom) - 1
    out: list[tuple[int, int]] = []
    for idxs in combinations(range(N), r):
        b0 = 0
        for ki, mm in enumerate(masks):
            p = 0
            for i in idxs:
                p ^= (mm >> i) & 1
            if p == 0:
                b0 |= 1 << ki
        b1 = full ^ b0
        out.append((b0, b1))
    return out


def split_bits(bits: int, parts: list[tuple[int, int]], pi: int) -> tuple[int, int]:
    c0, c1 = parts[pi]
    return bits & c0, bits & c1


def recurse_children_bits(
    exists_fn, b0: int, b1: int, depth_remaining: int
) -> bool:
    if b0 == 0:
        return exists_fn(b1, depth_remaining - 1)
    if b1 == 0:
        return exists_fn(b0, depth_remaining - 1)
    return exists_fn(b0, depth_remaining - 1) and exists_fn(
        b1, depth_remaining - 1
    )


def min_depth_for_language(
    masks: list[int],
    coord_parts: list[tuple[int, int]],
    xor_parts_list: list[list[tuple[int, int]]],
    d_max: int,
) -> tuple[int | None, list[tuple[int, bool, float]]]:
    dom = len(masks)
    full_bits = (1 << dom) - 1
    log: list[tuple[int, bool, float]] = []

    @lru_cache(maxsize=None)
    def exists_tree(bits: int, depth_remaining: int) -> bool:
        if pure_bits(bits, masks):
            return True
        if depth_remaining <= 0:
            return False
        for i in range(N):
            b0, b1 = split_bits(bits, coord_parts, i)
            if recurse_children_bits(exists_tree, b0, b1, depth_remaining):
                return True
        for xor_parts in xor_parts_list:
            for pi in range(len(xor_parts)):
                b0, b1 = split_bits(bits, xor_parts, pi)
                if recurse_children_bits(exists_tree, b0, b1, depth_remaining):
                    return True
        return False

    min_d: int | None = None
    for d in range(1, d_max + 1):
        exists_tree.cache_clear()
        t0 = time.perf_counter()
        ok = exists_tree(full_bits, d)
        elapsed = time.perf_counter() - t0
        log.append((d, ok, elapsed))
        if ok:
            min_d = d
            break
    return min_d, log


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--r-max",
        type=int,
        default=8,
        help="max r for single-arity sweep (default 8, excludes full n)",
    )
    args = p.parse_args()
    r_max = min(args.r_max, N - 1)

    masks = build_masks()
    coord_parts = build_coord_partition_masks(masks)

    md0, log0 = min_depth_for_language(masks, coord_parts, [], N)
    print(f"coord_only min_d={md0} (d_max={N})")
    for d, ok, sec in log0:
        print(f"  d={d} feasible={ok} sec={sec:.4f}")

    full_par_parts = build_r_xor_partition_masks(masks, N)
    assert len(full_par_parts) == 1
    md_full, log_full = min_depth_for_language(
        masks, coord_parts, [full_par_parts], N
    )
    print(f"coord_plus_full_{N}xor min_d={md_full}")
    for d, ok, sec in log_full:
        print(f"  d={d} feasible={ok} sec={sec:.4f}")

    for r in range(2, r_max + 1):
        t0 = time.perf_counter()
        xp = build_r_xor_partition_masks(masks, r)
        t1 = time.perf_counter()
        md, lg = min_depth_for_language(masks, coord_parts, [xp], N)
        t2 = time.perf_counter()
        print(
            f"coord_plus_{r}xor count={len(xp)} min_d={md} "
            f"build_sec={t1-t0:.3f} dp_sec={t2-t1:.3f}"
        )
        for d, ok, sec in lg:
            print(f"  d={d} feasible={ok} sec={sec:.4f}")

    parts_by_r = {r: build_r_xor_partition_masks(masks, r) for r in range(2, r_max + 1)}
    p2, p3, p4 = parts_by_r[2], parts_by_r[3], parts_by_r[4]
    md_234, _ = min_depth_for_language(masks, coord_parts, [p2, p3, p4], N)
    print(f"coord_plus_r2_r3_r4 min_d={md_234}")

    if r_max >= 5:
        md_2345, _ = min_depth_for_language(
            masks, coord_parts, [p2, p3, p4, parts_by_r[5]], N
        )
        print(f"coord_plus_r2_through_r5 min_d={md_2345}")

    if r_max >= 8:
        md_all, _ = min_depth_for_language(
            masks,
            coord_parts,
            [parts_by_r[r] for r in range(2, 9)],
            N,
        )
        print(f"coord_plus_r2_through_r8 min_d={md_all}")

    if md0 is None or md_full is None or md_full != 1:
        print("FAIL", flush=True)
        sys.exit(1)

    print("PASS", flush=True)


if __name__ == "__main__":
    main()
