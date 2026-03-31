#!/usr/bin/env python3
"""
n=10, public weights w_i = i+1. Exhaust all |S|=5 and |S|=6 subsets.

Search lexicographic (M1, M2) with M1,M2 >= 2 for first collision:
  (sum_{i in S} w_i mod M1, sum_{i in S} w_i^2 mod M2)
agrees for some 5-set and some 6-set.

If --scan-max N: only search M1,M2 in [2, N].
"""

from __future__ import annotations

import argparse
from itertools import combinations


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--scan-max", type=int, default=60, help="max M1 and M2 inclusive")
    args = p.parse_args()
    cap = args.scan_max

    n = 10
    w = [i + 1 for i in range(n)]
    w2 = [x * x for x in w]

    five = list(combinations(range(n), 5))
    six = list(combinations(range(n), 6))

    def stats(indices: tuple[int, ...]) -> tuple[int, int]:
        return (sum(w[i] for i in indices), sum(w2[i] for i in indices))

    for m1 in range(2, cap + 1):
        for m2 in range(2, cap + 1):
            by_key: dict[tuple[int, int], tuple[str, tuple[int, ...]]] = {}
            for idx in five:
                s, q = stats(idx)
                key = (s % m1, q % m2)
                by_key[key] = ("5", idx)
            for idx in six:
                s, q = stats(idx)
                key = (s % m1, q % m2)
                if key in by_key:
                    kind, f_idx = by_key[key]
                    if kind == "5":
                        print("FIRST_COLLISION")
                        print(f"M1={m1} M2={m2} key={key}")
                        print(f"  five-set indices={f_idx} sum={sum(w[i] for i in f_idx)} sumsq={sum(w2[i] for i in f_idx)}")
                        print(f"  six-set indices={idx} sum={sum(w[i] for i in idx)} sumsq={sum(w2[i] for i in idx)}")
                        print("PASS")
                        return
            # no collision for this (m1,m2)

    print(f"NO_COLLISION_M1_M2_UP_TO_{cap}")
    print("INCONCLUSIVE")


if __name__ == "__main__":
    main()
