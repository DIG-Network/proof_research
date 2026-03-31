#!/usr/bin/env python3
"""
1) Lemma check: complement w -> n-w swaps {T-1, T} iff n = 2T - 1 (for 1 <= T-1 < T <= n).

2) Regression: xor_pairwise_impossible(n,T) == (n == 2*T - 1) for a grid.

3) XOR min-depth backtracking (copy of 049 logic):
   - When impossible flag: expect no tree within max_d (search returns False for all d).
   - When possible and n <= N_SEARCH: expect some tree within max_d.

See adaptive-pairwise-or-xor-tree-depth-wt-shells for context (049).
"""

from __future__ import annotations

from functools import lru_cache


def popc(m: int) -> int:
    return m.bit_count()


def pure(S: tuple[int, ...]) -> bool:
    return len({popc(m) for m in S}) <= 1


def xor_pairwise_impossible(n: int, t: int) -> bool:
    return n == 2 * t - 1


def complement_swaps_two_shells(n: int, t: int) -> bool:
    """True iff w -> n-w maps {t-1, t} to itself as a swap (not identity on both)."""
    if not (1 <= t - 1 < t <= n):
        return False
    a, b = t - 1, t
    na, nb = n - a, n - b
    return {na, nb} == {a, b} and na != a


def split_xor(
    S: tuple[int, ...], i: int, j: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    S0 = tuple(m for m in S if ((((m >> i) & 1) ^ ((m >> j) & 1)) & 1) == 0)
    S1 = tuple(m for m in S if ((((m >> i) & 1) ^ ((m >> j) & 1)) & 1) == 1)
    return S0, S1


def xor_tree_exists_within(S: tuple[int, ...], n: int, max_d: int) -> bool:
    @lru_cache(maxsize=None)
    def exists_tree(Tset: tuple[int, ...], depth_remaining: int) -> bool:
        if pure(Tset):
            return True
        if depth_remaining <= 0:
            return False
        for i in range(n):
            for j in range(i + 1, n):
                S0, S1 = split_xor(Tset, i, j)
                if not S0:
                    if exists_tree(S1, depth_remaining - 1):
                        return True
                elif not S1:
                    if exists_tree(S0, depth_remaining - 1):
                        return True
                else:
                    if exists_tree(S0, depth_remaining - 1) and exists_tree(
                        S1, depth_remaining - 1
                    ):
                        return True
        return False

    for d in range(1, max_d + 1):
        exists_tree.cache_clear()
        if exists_tree(S, d):
            return True
    return False


def main() -> None:
    # Lemma: swap iff n = 2t - 1
    for n in range(3, 25):
        for t in range(2, n + 1):
            if not (1 <= t - 1 < t <= n):
                continue
            swap = complement_swaps_two_shells(n, t)
            formula = n == 2 * t - 1
            assert swap == formula, (n, t, swap, formula)

    # Flag matches formula
    for n in range(2, 20):
        for t in range(2, n + 1):
            if t - 1 < 0:
                continue
            assert xor_pairwise_impossible(n, t) == (n == 2 * t - 1)

    max_d = 80
    n_search_max = 6

    for n in range(3, n_search_max + 1):
        for t in range(2, n + 1):
            lo, hi = t - 1, t
            full = tuple(m for m in range(1 << n) if popc(m) in (lo, hi))
            if not full:
                continue
            imp = xor_pairwise_impossible(n, t)
            ok = xor_tree_exists_within(full, n, max_d)
            if imp:
                assert not ok, f"expected no XOR tree (n,t)=({n},{t})"
            else:
                assert ok, f"expected XOR tree within depth {max_d} (n,t)=({n},{t})"

    print("PASS: lemma OK; flag matches n==2t-1; XOR tree exists iff not impossible for n<=6")

    # Spot-check impossible case on tiny universe (fast): n=5,t=3, domain 2^5=32
    n, t = 5, 3
    assert xor_pairwise_impossible(n, t)
    full = tuple(m for m in range(1 << n) if popc(m) in (t - 1, t))
    assert not xor_tree_exists_within(full, n, max_d=100)
    print(f"  spot: (n,t)=({n},{t}) impossible -> no tree through depth 100")


if __name__ == "__main__":
    main()
