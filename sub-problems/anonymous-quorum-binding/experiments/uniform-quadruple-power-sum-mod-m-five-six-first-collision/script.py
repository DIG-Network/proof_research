#!/usr/bin/env python3
"""
n=10, w_i=i+1. p_k(S) = sum_{i in S} w_i^k for k=1,2,3,4.

Find smallest M >= 2 such that some 5-set and 6-set have identical
(p1%M, p2%M, p3%M, p4%M).
"""

from __future__ import annotations

import argparse
import sys
from itertools import combinations


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--scan-max", type=int, default=50000)
    args = p.parse_args()

    n = 10
    w = [i + 1 for i in range(n)]

    def powers(indices: tuple[int, ...]) -> tuple[int, int, int, int]:
        p1 = p2 = p3 = p4 = 0
        for i in indices:
            x = w[i]
            p1 += x
            p2 += x * x
            p3 += x * x * x
            p4 += x * x * x * x
        return (p1, p2, p3, p4)

    five = [powers(t) for t in combinations(range(n), 5)]
    six = [powers(t) for t in combinations(range(n), 6)]
    five_t = list(combinations(range(n), 5))
    six_t = list(combinations(range(n), 6))

    for m in range(2, args.scan_max + 1):
        keys5: dict[tuple[int, int, int, int], tuple[int, ...]] = {}
        for t, pk in zip(five_t, five):
            keys5[
                (pk[0] % m, pk[1] % m, pk[2] % m, pk[3] % m)
            ] = t
        for j, t6 in enumerate(six_t):
            pk = six[j]
            k = (pk[0] % m, pk[1] % m, pk[2] % m, pk[3] % m)
            if k in keys5:
                t5 = keys5[k]
                print(f"FIRST_COLLISION_M={m}")
                print(f"mod_key={k}")
                print(
                    f"five_indices={t5} weights={tuple(w[i] for i in t5)} raw={powers(t5)}"
                )
                print(
                    f"six_indices={t6} weights={tuple(w[i] for i in t6)} raw={powers(t6)}"
                )
                print("PASS")
                sys.exit(0)

    print(f"NO_COLLISION_UP_TO_{args.scan_max}")
    print("INCONCLUSIVE")
    sys.exit(1)


if __name__ == "__main__":
    main()
