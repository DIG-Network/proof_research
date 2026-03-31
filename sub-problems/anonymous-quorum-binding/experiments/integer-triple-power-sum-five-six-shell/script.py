#!/usr/bin/env python3
"""
n=10, w_i = i+1. K(S) = (sum w, sum w^2, sum w^3) as exact integers.

Test whether any 5-subset and 6-subset share the same K (cross-shell collision).
"""

from __future__ import annotations

from itertools import combinations


def main() -> None:
    n = 10
    w = [i + 1 for i in range(n)]

    def key(indices: tuple[int, ...]) -> tuple[int, int, int]:
        s1 = s2 = s3 = 0
        for i in indices:
            x = w[i]
            s1 += x
            s2 += x * x
            s3 += x * x * x
        return (s1, s2, s3)

    five: dict[tuple[int, int, int], tuple[int, ...]] = {}
    for t in combinations(range(n), 5):
        five[key(t)] = t

    collisions: list[tuple[tuple[int, int, int], tuple[int, ...], tuple[int, ...]]] = []
    for t6 in combinations(range(n), 6):
        k = key(t6)
        if k in five:
            collisions.append((k, five[k], t6))

    if not collisions:
        all_keys = list(five.keys())
        for t6 in combinations(range(n), 6):
            all_keys.append(key(t6))
        print("NO_EXACT_TRIPLE_POWER_COLLISION_BETWEEN_SHELLS")
        print(f"distinct_keys_union={len(set(all_keys))} total_subsets={len(all_keys)}")
        print("FAIL")
        return

    print(f"COLLISION_COUNT={len(collisions)}")
    k, t5, t6 = collisions[0]
    print(f"sample_key_p1={k[0]} p2={k[1]} p3={k[2]}")
    print(f"five_indices={t5} weights={tuple(w[i] for i in t5)}")
    print(f"six_indices={t6} weights={tuple(w[i] for i in t6)}")
    print("PASS")


if __name__ == "__main__":
    main()
