#!/usr/bin/env python3
"""
Minimum-depth adaptive decision trees separating popcount in {T-1, T} on {0,1}^n.

Allowed internal queries (choose i < j):
  - OR:  branch on (x_i | x_j) & 1
  - XOR: branch on (x_i ^ x_j) & 1

XOR impossibility: if n = 2T - 1, complement x ↦ x ⊕ (1,...,1) swaps weights T-1 and T,
and every pair-XOR answer is invariant under complement — no perfect XOR-only tree exists.

Compare: adaptive-pairwise-and-tree-depth-wt-five-vs-six (AND); adaptive-coordinate-tree-depth.

Usage:
  python script.py
  python script.py --op or --n 6 --t 4
  python script.py --op xor --n 6 --t 4
"""

from __future__ import annotations

import argparse
import sys
from functools import lru_cache
from typing import Callable, Literal

Op = Literal["or", "xor"]


def popc(m: int) -> int:
    return m.bit_count()


def pure(S: tuple[int, ...]) -> bool:
    return len({popc(m) for m in S}) <= 1


def xor_pairwise_impossible(n: int, t: int) -> bool:
    """No XOR-only pair tree can separate T-1 vs T when n = 2t-1 (complement swaps shells)."""
    return n == 2 * t - 1


def pair_val_or(m: int, i: int, j: int) -> int:
    return (((m >> i) & 1) | ((m >> j) & 1)) & 1


def pair_val_xor(m: int, i: int, j: int) -> int:
    return (((m >> i) & 1) ^ ((m >> j) & 1)) & 1


def split_pair(
    S: tuple[int, ...], i: int, j: int, val: Callable[[int, int, int], int]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    S0 = tuple(m for m in S if val(m, i, j) == 0)
    S1 = tuple(m for m in S if val(m, i, j) == 1)
    return S0, S1


def min_depth(n: int, t: int, op: Op) -> tuple[int | None, int]:
    """
    Return (min_depth or None if impossible, |domain|).
    XOR + n=2t-1 => None (impossible).
    """
    lo, hi = t - 1, t
    full = tuple(m for m in range(1 << n) if popc(m) in (lo, hi))
    if not full:
        raise ValueError("empty domain")

    if op == "xor" and xor_pairwise_impossible(n, t):
        return None, len(full)

    val = pair_val_or if op == "or" else pair_val_xor

    @lru_cache(maxsize=None)
    def exists_tree(S: tuple[int, ...], depth_remaining: int) -> bool:
        if pure(S):
            return True
        if depth_remaining <= 0:
            return False
        for i in range(n):
            for j in range(i + 1, n):
                S0, S1 = split_pair(S, i, j, val)
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

    max_d = 100 if op == "xor" else max(n + 8, 4 * n + 4)
    for d in range(1, max_d + 1):
        exists_tree.cache_clear()
        if exists_tree(full, d):
            return d, len(full)
    raise RuntimeError("min depth not found in search range")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--op", choices=("or", "xor"), default=None)
    p.add_argument("--n", type=int, default=None)
    p.add_argument("--t", type=int, default=None)
    args = p.parse_args()

    if args.op is not None:
        if args.n is None or args.t is None:
            print("need --n and --t with --op", file=sys.stderr)
            sys.exit(2)
        d, sz = min_depth(args.n, args.t, args.op)
        if d is None:
            print(
                f"op=xor (n,t)=({args.n},{args.t}) domain={sz} "
                f"IMPOSSIBLE (n=2t-1 complement invariance of pair XOR)"
            )
        else:
            nn = args.n
            cmp_n = ">" if d > nn else ("=" if d == nn else "<")
            print(
                f"op={args.op} (n,t)=({args.n},{args.t}) domain={sz} min_depth={d} "
                f"(vs n={nn}: {cmp_n} n)"
            )
        print("PASS")
        return

    # Default battery aligned with 048: (5,3) and (6,4) shells {t-1,t}.
    for n, t in ((5, 3), (6, 4)):
        d_or, sz = min_depth(n, t, "or")
        cmp_or = ">" if d_or > n else ("=" if d_or == n else "<")
        print(
            f"op=or (n,t)=({n},{t}) domain={sz} min_depth={d_or} "
            f"(vs n={n}: {cmp_or} n)"
        )

        d_xor, sz2 = min_depth(n, t, "xor")
        assert sz2 == sz
        if d_xor is None:
            print(
                f"op=xor (n,t)=({n},{t}) domain={sz} "
                f"IMPOSSIBLE (n=2t-1; pair XOR invariant under x↦x⊕1)"
            )
        else:
            cmp_x = ">" if d_xor > n else ("=" if d_xor == n else "<")
            print(
                f"op=xor (n,t)=({n},{t}) domain={sz} min_depth={d_xor} "
                f"(vs n={n}: {cmp_x} n)"
            )

    print("PASS")


if __name__ == "__main__":
    main()
