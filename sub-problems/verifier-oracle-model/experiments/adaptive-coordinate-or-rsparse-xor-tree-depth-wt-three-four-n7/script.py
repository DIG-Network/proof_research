#!/usr/bin/env python3
"""
n=7, popcount in {3,4} (C(7,3)+C(7,4)=70 masks). Majority toy t=4, n=2t-1.

For each r in {2,3,4}: adaptive trees, internal nodes are coordinate x_i OR
r-sparse XOR (all lexicographic r-tuples). Memoized exists_tree(bits, d).

Compare min_d across r; note r=4 XOR on 7 bits is NOT full 7-parity, but
coord + {all 4-XORs} may still reach min_d=1 if some split is shell-pure.

Also run coord-only baseline and coord + single full parity gate (one 7-XOR).
"""

from __future__ import annotations

import sys
import time
from functools import lru_cache
from itertools import combinations

N = 7
SHELLS = (3, 4)


def popc(m: int) -> int:
    return m.bit_count()


def build_masks() -> list[int]:
    masks = [m for m in range(1 << N) if popc(m) in SHELLS]
    assert len(masks) == 70
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
    dom = len(masks)
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
    masks = build_masks()
    coord_parts = build_coord_partition_masks(masks)

    # Baseline: coordinates only
    md0, log0 = min_depth_for_language(masks, coord_parts, [], N)
    print(f"coord_only min_d={md0} (d_max={N})")
    for d, ok, sec in log0:
        print(f"  d={d} feasible={ok} sec={sec:.4f}")

    # Full 7-bit parity as ONE extra gate (like breakthrough 092 language)
    full_par_parts = build_r_xor_partition_masks(masks, N)
    assert len(full_par_parts) == 1
    md_full, log_full = min_depth_for_language(
        masks, coord_parts, [full_par_parts], N
    )
    print(f"coord_plus_full_{N}xor min_d={md_full}")
    for d, ok, sec in log_full:
        print(f"  d={d} feasible={ok} sec={sec:.4f}")

    for r in (2, 3, 4):
        xp = build_r_xor_partition_masks(masks, r)
        md, lg = min_depth_for_language(masks, coord_parts, [xp], N)
        print(
            f"coord_plus_{r}xor count={len(xp)} min_d={md}"
        )
        for d, ok, sec in lg:
            print(f"  d={d} feasible={ok} sec={sec:.4f}")

    # Combined language: coord + pair + triple + quad simultaneously (rich library)
    p2 = build_r_xor_partition_masks(masks, 2)
    p3 = build_r_xor_partition_masks(masks, 3)
    p4 = build_r_xor_partition_masks(masks, 4)
    md_all, log_all = min_depth_for_language(
        masks, coord_parts, [p2, p3, p4], N
    )
    print(f"coord_plus_pair_plus_triple_plus_quad min_d={md_all}")
    for d, ok, sec in log_all:
        print(f"  d={d} feasible={ok} sec={sec:.4f}")

    if md0 is None or md_full is None:
        print("FAIL", flush=True)
        sys.exit(1)
    if md_full != 1:
        print("UNEXPECTED: full parity should separate odd/even shells at d=1")
        print("FAIL", flush=True)
        sys.exit(1)

    print("PASS", flush=True)


if __name__ == "__main__":
    main()
