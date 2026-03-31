#!/usr/bin/env python3
"""
n=10, wt in {5,6} (462 masks). Mixed adaptive trees: coordinate OR pair-XNOR.

XNOR on bits = 1 iff equal. Branch 0 if XNOR=0 (bits differ), 1 if equal.
Partition {equal, unequal} is the same as XOR; only 0/1 labels swap vs 066.

Expected min_d = 5 (same as adaptive-coordinate-or-pair-xor-tree-depth-wt-five-vs-six).
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


def split_xnor(S: tuple[int, ...], i: int, j: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Branch 0: XNOR=0 (bits differ); branch 1: XNOR=1 (bits equal)."""
    S_diff = tuple(m for m in S if ((m >> i) & 1) != ((m >> j) & 1))
    S_eq = tuple(m for m in S if ((m >> i) & 1) == ((m >> j) & 1))
    return S_diff, S_eq


def split_xor(S: tuple[int, ...], i: int, j: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """066 convention: branch 0 if XOR=0 (equal), 1 if XOR=1 (differ)."""
    S_eq = tuple(m for m in S if (((m >> i) ^ (m >> j)) & 1) == 0)
    S_diff = tuple(m for m in S if (((m >> i) ^ (m >> j)) & 1) == 1)
    return S_eq, S_diff


def partitions_match_xor_xnor() -> None:
    full = tuple(m for m in range(1 << N) if popc(m) in (5, 6))
    for i in range(N):
        for j in range(i + 1, N):
            a0, a1 = split_xor(full, i, j)
            b0, b1 = split_xnor(full, i, j)
            assert set(a0) == set(b1) and set(a1) == set(b0), (i, j)


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
    partitions_match_xor_xnor()
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
                S0, S1 = split_xnor(S, i, j)
                if recurse_children(exists_tree, S0, S1, depth_remaining):
                    return True
        return False

    for d in range(1, 5):
        exists_tree.cache_clear()
        assert not exists_tree(full, d), f"unexpected feasible at d={d}"

    exists_tree.cache_clear()
    assert exists_tree(full, 5), "expected feasible at d=5 (same splits as XOR up to swap)"

    print("min_depth_found=5 (mixed coord + pair-XNOR)")
    print("STRICT_IMPROVEMENT min_d=5 < n=10")
    print("PASS")


if __name__ == "__main__":
    main()
