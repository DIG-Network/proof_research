#!/usr/bin/env python3
"""
exists_tree(full, 4) vs exists_tree(full, 5) for n=10, wt in {5,6}, mixed coord + pair-XOR.

PASS if depth 4 infeasible and depth 5 feasible (matches 066 min-depth certificate).
"""

from __future__ import annotations

import sys
from functools import lru_cache

N = 10


def popc(m: int) -> int:
    return m.bit_count()


def pure(S: tuple[int, ...]) -> bool:
    return len({popc(m) for m in S}) <= 1


def split_coord(S: tuple[int, ...], i: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    S0 = tuple(m for m in S if ((m >> i) & 1) == 0)
    S1 = tuple(m for m in S if ((m >> i) & 1) == 1)
    return S0, S1


def split_xor(S: tuple[int, ...], i: int, j: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    S0 = tuple(m for m in S if (((m >> i) ^ (m >> j)) & 1) == 0)
    S1 = tuple(m for m in S if (((m >> i) ^ (m >> j)) & 1) == 1)
    return S0, S1


def recurse_children(
    exists_fn, S0: tuple[int, ...], S1: tuple[int, ...], depth_remaining: int
) -> bool:
    if not S0:
        return exists_fn(S1, depth_remaining - 1)
    if not S1:
        return exists_fn(S0, depth_remaining - 1)
    return exists_fn(S0, depth_remaining - 1) and exists_fn(S1, depth_remaining - 1)


@lru_cache(maxsize=None)
def exists_tree(S: tuple[int, ...], depth_remaining: int) -> bool:
    if pure(S):
        return True
    if depth_remaining <= 0:
        return False
    for i in range(N):
        S0, S1 = split_coord(S, i)
        if recurse_children(exists_tree, S0, S1, depth_remaining):
            return True
    for i in range(N):
        for j in range(i + 1, N):
            S0, S1 = split_xor(S, i, j)
            if recurse_children(exists_tree, S0, S1, depth_remaining):
                return True
    return False


def main() -> None:
    full = tuple(m for m in range(1 << N) if popc(m) in (5, 6))
    assert len(full) == 462

    e4 = exists_tree(full, 4)
    e5 = exists_tree(full, 5)
    print(f"exists_tree_full_d4={e4}")
    print(f"exists_tree_full_d5={e5}")

    if e4:
        print("UNEXPECTED_D4_FEASIBLE")
        print("FAIL")
        sys.exit(1)
    if not e5:
        print("UNEXPECTED_D5_INFEASIBLE")
        print("FAIL")
        sys.exit(1)

    print("D4_INFEASIBLE_D5_FEASIBLE")
    print("PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
