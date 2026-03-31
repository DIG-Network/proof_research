#!/usr/bin/env python3
"""
n=10, w_i=i+1. |S|=5 vs |S|=6.

Lex-first (M1, M2, M3) with min <= Mi <= scan_max and pairwise gcd(Mi,Mj)==1:
  first collision on (sum w mod M1, sum w^2 mod M2, sum w^3 mod M3).

Default min_m=4 (follow-up to experiment 059 which used min_m=2).
"""

from __future__ import annotations

import argparse
from itertools import combinations
from math import gcd


def pairwise_coprime(a: int, b: int, c: int) -> bool:
    return gcd(a, b) == 1 and gcd(a, c) == 1 and gcd(b, c) == 1


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--scan-max", type=int, default=150, help="max each Mi inclusive")
    p.add_argument("--min-m", type=int, default=4, help="minimum each Mi")
    args = p.parse_args()
    cap = args.scan_max
    lo = args.min_m

    n = 10
    w = [i + 1 for i in range(n)]
    w2 = [x * x for x in w]
    w3 = [x * x * x for x in w]

    def tri(indices: tuple[int, ...]) -> tuple[int, int, int]:
        return (
            sum(w[i] for i in indices),
            sum(w2[i] for i in indices),
            sum(w3[i] for i in indices),
        )

    five = [(t, *tri(t)) for t in combinations(range(n), 5)]
    six = [(t, *tri(t)) for t in combinations(range(n), 6)]

    for m1 in range(lo, cap + 1):
        for m2 in range(lo, cap + 1):
            for m3 in range(lo, cap + 1):
                if not pairwise_coprime(m1, m2, m3):
                    continue
                by_key: dict[
                    tuple[int, int, int],
                    tuple[str, tuple[int, ...], int, int, int],
                ] = {}
                for idx_t, s, q, c in five:
                    key = (s % m1, q % m2, c % m3)
                    by_key[key] = ("5", idx_t, s, q, c)
                for idx_t, s, q, c in six:
                    key = (s % m1, q % m2, c % m3)
                    if key not in by_key:
                        continue
                    kind, f_idx, fs, fq, fc = by_key[key]
                    if kind != "5":
                        continue
                    print("FIRST_COLLISION")
                    print(f"M1={m1} M2={m2} M3={m3} min_m={lo} key={key}")
                    print(
                        f"  five-set indices={f_idx} sum={fs} sumsq={fq} sumcb={fc}"
                    )
                    print(
                        f"  six-set indices={idx_t} sum={s} sumsq={q} sumcb={c}"
                    )
                    print("PASS")
                    return

    print(f"NO_COLLISION_PAIRWISE_COPRIME_min{lo}_UP_TO_{cap}")
    print("INCONCLUSIVE")


if __name__ == "__main__":
    main()
