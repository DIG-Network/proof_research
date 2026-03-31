#!/usr/bin/env python3
"""
Adaptive decision trees on x in {0,1}^N; domain popcount(x) in {T-1, T}.

Internal nodes: branch on x_i AND x_j for i < j (pairwise AND oracle).

Coordinate-only baseline (adaptive-coordinate-tree-depth-wt-five-vs-six): for (N,T)=(10,6),
worst-case depth = N.

Exhaustive minimum depth via memoized backtracking (tractable for small N only).

Usage:
  python script.py                    # default: (5,3) and (6,4)
  python script.py --n 6 --t 4        # single instance
"""

from __future__ import annotations

import argparse
import sys
from functools import lru_cache


def popc(m: int) -> int:
    return m.bit_count()


def pure(S: tuple[int, ...]) -> bool:
    return len({popc(m) for m in S}) <= 1


def split_and(
    S: tuple[int, ...], n: int, i: int, j: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    S0 = tuple(m for m in S if (((m >> i) & 1) & ((m >> j) & 1)) == 0)
    S1 = tuple(m for m in S if (((m >> i) & 1) & ((m >> j) & 1)) == 1)
    return S0, S1


def min_depth_pairwise_and(n: int, t: int) -> tuple[int, int]:
    """Return (min_depth, |domain|)."""
    lo, hi = t - 1, t
    full = tuple(m for m in range(1 << n) if popc(m) in (lo, hi))
    if not full:
        raise ValueError("empty domain")

    @lru_cache(maxsize=None)
    def exists_tree(S: tuple[int, ...], depth_remaining: int) -> bool:
        if pure(S):
            return True
        if depth_remaining <= 0:
            return False
        for i in range(n):
            for j in range(i + 1, n):
                S0, S1 = split_and(S, n, i, j)
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

    for d in range(1, n + 8):
        exists_tree.cache_clear()
        if exists_tree(full, d):
            return d, len(full)
    raise RuntimeError("min depth not found in search range")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=None)
    p.add_argument("--t", type=int, default=None)
    args = p.parse_args()

    if args.n is not None:
        if args.t is None:
            print("need --t with --n", file=sys.stderr)
            sys.exit(2)
        d, sz = min_depth_pairwise_and(args.n, args.t)
        print(f"(n,t)=({args.n},{args.t}) domain={sz} min_pairwise_and_depth={d}")
        print("PASS")
        return

    for n, t in ((5, 3), (6, 4)):
        d, sz = min_depth_pairwise_and(n, t)
        cmp_n = ">" if d > n else ("=" if d == n else "<")
        print(
            f"(n,t)=({n},{t}) domain={sz} min_pairwise_and_depth={d} "
            f"(vs coordinate worst-case depth {n}: AND is {cmp_n} n)"
        )

    print("PASS")


if __name__ == "__main__":
    main()
