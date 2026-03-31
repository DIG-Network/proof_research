#!/usr/bin/env python3
"""
n=10, w_i = i+1. K(S) = (sum of w over S, product of w over S) as exact integers.

Report whether any 5-set and 6-set share the same K (collision across shells).
"""

from __future__ import annotations

from itertools import combinations
from math import prod


def main() -> None:
    n = 10
    w = [i + 1 for i in range(n)]

    def key(indices: tuple[int, ...]) -> tuple[int, int]:
        ws = [w[i] for i in indices]
        return (sum(ws), prod(ws))

    five: dict[tuple[int, int], tuple[int, ...]] = {}
    for t in combinations(range(n), 5):
        five[key(t)] = t

    collisions: list[tuple[tuple[int, int], tuple[int, ...], tuple[int, ...]]] = []
    for t6 in combinations(range(n), 6):
        k = key(t6)
        if k in five:
            collisions.append((k, five[k], t6))

    if not collisions:
        print("NO_EXACT_SUM_PRODUCT_COLLISION")
        print("FAIL")
        return

    print(f"COLLISION_COUNT={len(collisions)}")
    k, t5, t6 = collisions[0]
    print(f"sample_key_sum={k[0]} prod={k[1]}")
    print(f"five_indices={t5} weights={tuple(w[i] for i in t5)}")
    print(f"six_indices={t6} weights={tuple(w[i] for i in t6)}")
    print("PASS")


if __name__ == "__main__":
    main()
