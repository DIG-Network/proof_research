#!/usr/bin/env python3
"""
n=10, domain: all x in {0,1}^10 with popcount in {5,6} (462 masks).

Adaptive binary decision trees. Each internal node is either:
  - coordinate: branch on bit x_i
  - pair XOR: branch on x_i XOR x_j (i < j)

Leaves must be pure (all same popcount). Memoized existence test exists_tree(S, d).

Reports minimum d with a perfect separator tree; compares to coordinate-only (known n=10).
"""

from __future__ import annotations

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
    exists_tree_fn, S0: tuple[int, ...], S1: tuple[int, ...], depth_remaining: int
) -> bool:
    if not S0:
        return exists_tree_fn(S1, depth_remaining - 1)
    if not S1:
        return exists_tree_fn(S0, depth_remaining - 1)
    return exists_tree_fn(S0, depth_remaining - 1) and exists_tree_fn(
        S1, depth_remaining - 1
    )


def main() -> None:
    full = tuple(m for m in range(1 << N) if popc(m) in (5, 6))
    assert len(full) == 462

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

    min_d = None
    for d in range(1, N + 1):
        exists_tree.cache_clear()
        if exists_tree(full, d):
            min_d = d
            print(f"min_depth_found={d}")
            break

    if min_d is None:
        print("NO_TREE_UP_TO_N")
        print("FAIL")
        return

    if min_d >= N:
        print(f"min_depth_equals_n={N} (no improvement over coordinate-only 045)")
        print("PASS")
        return

    print(f"STRICT_IMPROVEMENT min_d={min_d} < n={N}")
    print("PASS")


if __name__ == "__main__":
    main()
