#!/usr/bin/env python3
"""
Toy: count strict-majority subsets W vs distinct aggregate sums U for integer PKs.

Shows: anonymity (collapse of pi across S) is compatible with large W;
specifying which aggregate K among U possibilities needs ceil(log2 U) bits worst-case.
Also search for Agg collisions (S1 != S2, same sum) for small structured keys.
"""

from __future__ import annotations

import itertools
import math
from typing import List, Set, Tuple


def majority_subset_count(n: int) -> int:
    t = n // 2 + 1
    return sum(math.comb(n, k) for k in range(t, n + 1))


def all_majority_subsets(n: int) -> List[Tuple[int, ...]]:
    t = n // 2 + 1
    out: List[Tuple[int, ...]] = []
    for k in range(t, n + 1):
        for comb in itertools.combinations(range(n), k):
            out.append(comb)
    return out


def agg_sum(indices: Tuple[int, ...], pks: List[int]) -> int:
    return sum(pks[i] for i in indices)


def distinct_aggregates(n: int, pks: List[int]) -> tuple[int, int, float]:
    subs = all_majority_subsets(n)
    values: Set[int] = set()
    for s in subs:
        values.add(agg_sum(s, pks))
    W = len(subs)
    U = len(values)
    bits = math.log2(U) if U > 0 else 0.0
    return W, U, bits


def find_collision(n: int, pks: List[int]) -> Tuple[Tuple[int, ...], Tuple[int, ...]] | None:
    subs = all_majority_subsets(n)
    mp: dict[int, Tuple[int, ...]] = {}
    for s in subs:
        v = agg_sum(s, pks)
        if v in mp and mp[v] != s:
            return mp[v], s
        mp[v] = s
    return None


def main() -> None:
    print("=== simulator-bandwidth-toy ===\n")

    for n in (6, 8, 10):
        t = n // 2 + 1
        pks = [1000 + 13 * i for i in range(n)]
        W, U, bits = distinct_aggregates(n, pks)
        print(f"n={n}, t={t}: W (majority subsets)={W}, U (distinct Agg)={U}, log2(U)={bits:.3f}")

    # Structured keys more likely to collide
    n = 10
    pks_struct = [2**i for i in range(n)]
    W, U, bits = distinct_aggregates(n, pks_struct)
    col = find_collision(n, pks_struct)
    print(f"\nStructured pks 2^i: W={W}, U={U}, log2(U)={bits:.3f}")
    print(f"Collision found: {col is not None}")
    if col:
        print(f"  S1={col[0]}, S2={col[1]}, sum={agg_sum(col[0], pks_struct)}")

    # Asymptotic reminder for large n (counting only, no full enumeration)
    n_big = 64
    W_big = majority_subset_count(n_big)
    print(f"\nn={n_big}: W ~ {W_big:.3e}, log2(W) ~ {math.log2(W_big):.2f} bits (subset count only)")

    print("\nVERDICT LINE: U often < W (many S share same Agg sum) even for affine PKs;")
    print("H1: anonymity does not require injective pi on S. Bottleneck remains Link(C,K), not log2(W).")

if __name__ == "__main__":
    main()
