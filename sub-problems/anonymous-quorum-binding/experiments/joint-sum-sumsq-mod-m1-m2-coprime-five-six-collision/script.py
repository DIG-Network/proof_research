#!/usr/bin/env python3
"""
n=10, w_i=i+1. |S|=5 vs |S|=6.

Lex-first (M1, M2) with min bounds and gcd(M1,M2)==1:
  first collision on (sum w mod M1, sum w^2 mod M2).
"""

from __future__ import annotations

import argparse
from itertools import combinations
from math import gcd


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--scan-max", type=int, default=120, help="max M1 and M2 inclusive")
    p.add_argument("--min-m1", type=int, default=2, help="minimum M1")
    p.add_argument("--min-m2", type=int, default=2, help="minimum M2")
    args = p.parse_args()
    cap = args.scan_max
    lo1, lo2 = args.min_m1, args.min_m2

    n = 10
    w = [i + 1 for i in range(n)]
    w2 = [x * x for x in w]

    five = list(combinations(range(n), 5))
    six = list(combinations(range(n), 6))

    def stats(indices: tuple[int, ...]) -> tuple[int, int]:
        return (sum(w[i] for i in indices), sum(w2[i] for i in indices))

    for m1 in range(lo1, cap + 1):
        for m2 in range(lo2, cap + 1):
            if gcd(m1, m2) != 1:
                continue
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
                        print(f"M1={m1} M2={m2} gcd={gcd(m1,m2)} key={key}")
                        print(
                            f"  five-set indices={f_idx} sum={sum(w[i] for i in f_idx)} sumsq={sum(w2[i] for i in f_idx)}"
                        )
                        print(
                            f"  six-set indices={idx} sum={sum(w[i] for i in idx)} sumsq={sum(w2[i] for i in idx)}"
                        )
                        print("PASS")
                        return

    print(f"NO_COLLISION_COPRIME_IN_[{lo1},{cap}]x[{lo2},{cap}]")
    print("INCONCLUSIVE")


if __name__ == "__main__":
    main()
