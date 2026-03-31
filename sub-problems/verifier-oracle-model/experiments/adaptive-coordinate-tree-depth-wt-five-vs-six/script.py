#!/usr/bin/env python3
"""
Decision trees that only read individual coordinates (bits) of x in {0,1}^n.

Domain restricted to Hamming weight 5 OR 6 (n=10, t=6 toy: distinguish one-below
quorum vs quorum by exact weight).

Backtracking with memoization: exists(S, d) = some depth-d tree separates all
masks in S into leaves that are pure (single weight class).

Key fact: if x (wt 5) and y (wt 6) differ only at index j, they give identical
answers on every query i != j, so any tree must eventually query j on their
shared path — hence worst-case depth >= n (need all coordinates).
"""

from __future__ import annotations

from functools import lru_cache

N = 10


def popc(m: int) -> int:
    return m.bit_count()


def pure(S: tuple[int, ...]) -> bool:
    wts = {popc(m) for m in S}
    return len(wts) <= 1


def split(S: tuple[int, ...], i: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    S0 = tuple(m for m in S if ((m >> i) & 1) == 0)
    S1 = tuple(m for m in S if ((m >> i) & 1) == 1)
    return S0, S1


@lru_cache(maxsize=None)
def exists_tree(S: tuple[int, ...], depth_remaining: int) -> bool:
    if pure(S):
        return True
    if depth_remaining <= 0:
        return False
    for i in range(N):
        S0, S1 = split(S, i)
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


def main() -> None:
    full = tuple(m for m in range(1 << N) if popc(m) in (5, 6))
    assert len(full) == 462

    for d in range(1, N + 1):
        ok = exists_tree(full, d)
        print(f"depth_cap={d} exists_perfect_tree={ok}")

    if exists_tree(full, N - 1):
        print("FAIL: expected no tree of depth n-1")
        raise SystemExit(1)
    if not exists_tree(full, N):
        print("FAIL: expected identity queries work at depth n")
        raise SystemExit(1)

    print("PASS")
    print("  min worst-case depth (coordinate queries only) = n = 10 on wt in {5,6}")


if __name__ == "__main__":
    main()
