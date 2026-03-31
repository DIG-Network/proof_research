#!/usr/bin/env python3
"""
n=10, w_i=i+1. |S|=5 vs |S|=6.

Lex-first (M1,...,M5) with min_m <= Mi <= scan_max and pairwise gcd(Mi,Mj)==1:
  first collision on
  (sum w mod M1, sum w^2 mod M2, ..., sum w^5 mod M5).
"""

from __future__ import annotations

import argparse
import sys
from itertools import combinations
from math import gcd


def pairwise_coprime5(t: tuple[int, int, int, int, int]) -> bool:
    a, b, c, d, e = t
    for x, y in (
        (a, b),
        (a, c),
        (a, d),
        (a, e),
        (b, c),
        (b, d),
        (b, e),
        (c, d),
        (c, e),
        (d, e),
    ):
        if gcd(x, y) != 1:
            return False
    return True


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--scan-max",
        type=int,
        default=18,
        help="max each Mi inclusive (keep modest: O(scan^5 * 462) inner work)",
    )
    p.add_argument("--min-m", type=int, default=2, help="minimum each Mi")
    args = p.parse_args()
    cap = args.scan_max
    lo = args.min_m

    n = 10
    w = [i + 1 for i in range(n)]
    w2 = [x * x for x in w]
    w3 = [x * x * x for x in w]
    w4 = [x * x * x * x for x in w]
    w5 = [x * x * x * x * x for x in w]

    def penta(indices: tuple[int, ...]) -> tuple[int, int, int, int, int]:
        return (
            sum(w[i] for i in indices),
            sum(w2[i] for i in indices),
            sum(w3[i] for i in indices),
            sum(w4[i] for i in indices),
            sum(w5[i] for i in indices),
        )

    five = [(t, penta(t)) for t in combinations(range(n), 5)]
    six = [(t, penta(t)) for t in combinations(range(n), 6)]

    for m1 in range(lo, cap + 1):
        for m2 in range(lo, cap + 1):
            for m3 in range(lo, cap + 1):
                for m4 in range(lo, cap + 1):
                    for m5 in range(lo, cap + 1):
                        if not pairwise_coprime5((m1, m2, m3, m4, m5)):
                            continue
                        by_key: dict[
                            tuple[int, int, int, int, int],
                            tuple[tuple[int, ...], tuple[int, int, int, int, int]],
                        ] = {}
                        for idx_t, pk in five:
                            key = (
                                pk[0] % m1,
                                pk[1] % m2,
                                pk[2] % m3,
                                pk[3] % m4,
                                pk[4] % m5,
                            )
                            by_key[key] = (idx_t, pk)
                        for idx_t, pk in six:
                            key = (
                                pk[0] % m1,
                                pk[1] % m2,
                                pk[2] % m3,
                                pk[3] % m4,
                                pk[4] % m5,
                            )
                            if key not in by_key:
                                continue
                            f_idx, fpk = by_key[key]
                            print("FIRST_COLLISION")
                            print(
                                f"M1={m1} M2={m2} M3={m3} M4={m4} M5={m5} min_m={lo} key={key}"
                            )
                            print(f"  five-set indices={f_idx} penta={fpk}")
                            print(f"  six-set indices={idx_t} penta={pk}")
                            print("PASS")
                            sys.exit(0)

    print(
        f"NO_COLLISION_PAIRWISE_COPRIME_quintuple_min{lo}_UP_TO_{cap}",
    )
    print("INCONCLUSIVE")
    sys.exit(1)


if __name__ == "__main__":
    main()
