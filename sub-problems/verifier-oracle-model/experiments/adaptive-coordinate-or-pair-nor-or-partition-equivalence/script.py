#!/usr/bin/env python3
"""
n=10, wt in {5,6} (462 masks). Show mixed coord + pair-NOR equals mixed coord + pair-OR
as a *split language*: for each pair (i,j), NOR(branch 0 = NOR=0) induces the same
unordered bipartition as OR(branch 0 = OR=0), with 0/1 children swapped.

Then exists_tree(bits,d) is identical for OR-mixed vs NOR-mixed (recurse_children_bits
symmetric in the two children). Hence min depth matches Entry 082 (min_d=10).

Script checks:
  (1) per-pair mask swap NOR == (OR_b1, OR_b0)
  (2) for small d, brute memoized feasible(full,d) matches for OR_parts vs NOR_parts
"""

from __future__ import annotations

import argparse
import sys
import time
from functools import lru_cache

N = 10
DOMAIN_SIZE = 462


def popc(m: int) -> int:
    return m.bit_count()


def build_masks() -> list[int]:
    masks = [m for m in range(1 << N) if popc(m) in (5, 6)]
    assert len(masks) == DOMAIN_SIZE
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


def build_or_partition_masks(masks: list[int]) -> list[tuple[int, int]]:
    """(x_i OR x_j = 0, = 1) over domain indices."""
    out: list[tuple[int, int]] = []
    for i in range(N):
        for j in range(i + 1, N):
            b0 = 0
            b1 = 0
            for k, m in enumerate(masks):
                if (((m >> i) & 1) | ((m >> j) & 1)) & 1:
                    b1 |= 1 << k
                else:
                    b0 |= 1 << k
            out.append((b0, b1))
    return out


def build_nor_partition_masks(masks: list[int]) -> list[tuple[int, int]]:
    """Branch 0 when NOR(x_i,x_j)=0; i.e. at least one of (x_i,x_j) is 1."""
    out: list[tuple[int, int]] = []
    for i in range(N):
        for j in range(i + 1, N):
            b_nor0 = 0
            for k, m in enumerate(masks):
                xi = (m >> i) & 1
                xj = (m >> j) & 1
                nor_out = 1 ^ (xi | xj)  # NOR = NOT OR
                if nor_out == 0:
                    b_nor0 |= 1 << k
            full = (1 << DOMAIN_SIZE) - 1
            b_nor1 = full ^ b_nor0
            out.append((b_nor0, b_nor1))
    return out


def split_coord_bits(bits: int, coord_parts: list[tuple[int, int]], i: int) -> tuple[int, int]:
    c0, c1 = coord_parts[i]
    return bits & c0, bits & c1


def split_pair_bits(bits: int, pair_parts: list[tuple[int, int]], pair_idx: int) -> tuple[int, int]:
    c0, c1 = pair_parts[pair_idx]
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


def feasible_at_depth(
    masks: list[int],
    coord_parts: list[tuple[int, int]],
    pair_parts: list[tuple[int, int]],
    d: int,
) -> bool:
    full_bits = (1 << DOMAIN_SIZE) - 1

    @lru_cache(maxsize=None)
    def exists_tree(bits: int, depth_remaining: int) -> bool:
        if pure_bits(bits, masks):
            return True
        if depth_remaining <= 0:
            return False
        for i in range(N):
            b0, b1 = split_coord_bits(bits, coord_parts, i)
            if recurse_children_bits(exists_tree, b0, b1, depth_remaining):
                return True
        for pi in range(len(pair_parts)):
            b0, b1 = split_pair_bits(bits, pair_parts, pi)
            if recurse_children_bits(exists_tree, b0, b1, depth_remaining):
                return True
        return False

    return exists_tree(full_bits, d)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--crosscheck-max-d",
        type=int,
        default=5,
        metavar="D",
        help="For each d in 1..D, assert OR vs NOR feasible(full,d) agree (default 5; d=6+ is heavy).",
    )
    p.add_argument(
        "--partition-only",
        action="store_true",
        help="Only verify NOR masks are swapped OR masks; skip DP crosscheck.",
    )
    args = p.parse_args()

    masks = build_masks()
    coord = build_coord_partition_masks(masks)
    or_parts = build_or_partition_masks(masks)
    nor_parts = build_nor_partition_masks(masks)

    assert len(or_parts) == len(nor_parts) == N * (N - 1) // 2

    full = (1 << DOMAIN_SIZE) - 1
    for pi, ((ob0, ob1), (nb0, nb1)) in enumerate(zip(or_parts, nor_parts, strict=True)):
        if (nb0, nb1) != (ob1, ob0):
            print(f"partition_mismatch pair_idx={pi}", flush=True)
            print("FAIL", flush=True)
            sys.exit(1)
        if (ob0 | ob1) != full or (ob0 & ob1) != 0:
            print(f"or_parts not a partition idx={pi}", flush=True)
            print("FAIL", flush=True)
            sys.exit(1)

    print("partition_swap_ok all_pairs NOR=(OR_side1, OR_side0)", flush=True)

    if args.partition_only:
        print(
            "Skipping DP (--partition-only); min_d claim follows from swap + Entry 082.",
            flush=True,
        )
        print("PASS", flush=True)
        return

    dmax = max(0, min(args.crosscheck_max_d, N))
    for d in range(1, dmax + 1):
        t0 = time.perf_counter()
        ok_or = feasible_at_depth(masks, coord, or_parts, d)
        t1 = time.perf_counter()
        ok_nor = feasible_at_depth(masks, coord, nor_parts, d)
        t2 = time.perf_counter()
        if ok_or != ok_nor:
            print(f"d={d} mismatch OR={ok_or} NOR={ok_nor}", flush=True)
            print("FAIL", flush=True)
            sys.exit(1)
        print(
            f"d={d} OR_feasible={ok_or} NOR_feasible={ok_nor} "
            f"sec_or={t1 - t0:.3f} sec_nor={t2 - t1:.3f}",
            flush=True,
        )

    print(
        "Reduction: mixed NOR language == mixed OR language on this domain; "
        f"min_d = 10 by Entry 082 (pair-or-coord-mixed-min-depth-ten-certified).",
        flush=True,
    )
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
