#!/usr/bin/env python3
"""
n=10, w_i = i+1. K(S) = (sum w^k for k=1..5) as exact integers.

Test whether any 5-subset and 6-subset share the same K (cross-shell collision).
Convention matches integer-triple-power-sum-five-six-shell: PASS if collision, FAIL if none.
"""

from __future__ import annotations

from itertools import combinations


def main() -> None:
    n = 10
    w = [i + 1 for i in range(n)]

    def key(indices: tuple[int, ...]) -> tuple[int, int, int, int, int]:
        s1 = s2 = s3 = s4 = s5 = 0
        for i in indices:
            x = w[i]
            s1 += x
            s2 += x * x
            s3 += x * x * x
            x4 = x * x * x * x
            s4 += x4
            s5 += x4 * x
        return (s1, s2, s3, s4, s5)

    five: dict[tuple[int, int, int, int, int], tuple[int, ...]] = {}
    for t in combinations(range(n), 5):
        five[key(t)] = t

    collisions: list[
        tuple[tuple[int, int, int, int, int], tuple[int, ...], tuple[int, ...]]
    ] = []
    for t6 in combinations(range(n), 6):
        k = key(t6)
        if k in five:
            collisions.append((k, five[k], t6))

    if not collisions:
        keys5 = {key(t) for t in combinations(range(n), 5)}
        keys6 = {key(t) for t in combinations(range(n), 6)}
        union = keys5 | keys6
        print("NO_EXACT_QUINTUPLE_POWER_COLLISION_BETWEEN_SHELLS")
        print(f"distinct_keys_5shell={len(keys5)} distinct_keys_6shell={len(keys6)}")
        print(f"distinct_keys_union={len(union)} total_subsets={252 + 210}")
        print("injective_on_union=", len(union) == 462)
        print("FAIL")
        return

    print(f"COLLISION_COUNT={len(collisions)}")
    k, t5, t6 = collisions[0]
    print(f"sample_key={k}")
    print(f"five_indices={t5} weights={tuple(w[i] for i in t5)}")
    print(f"six_indices={t6} weights={tuple(w[i] for i in t6)}")
    print("PASS")


if __name__ == "__main__":
    main()
