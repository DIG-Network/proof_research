#!/usr/bin/env python3
"""
n=10, w_i=i+1. T_M(S) = (sum w mod M, XOR w over S).

Find smallest M >= 2 such that no 5-set and 6-set share the same T_M.
If none up to scan_max: INCONCLUSIVE.
"""

from __future__ import annotations

import argparse
from functools import reduce
from itertools import combinations
from operator import xor


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--scan-max", type=int, default=2000, help="max M to try")
    args = p.parse_args()
    cap = args.scan_max

    n = 10
    w = [i + 1 for i in range(n)]

    def sx(indices: tuple[int, ...]) -> tuple[int, int]:
        s = sum(w[i] for i in indices)
        x = reduce(xor, (w[i] for i in indices), 0)
        return (s, x)

    five = [sx(t) for t in combinations(range(n), 5)]
    six = [sx(t) for t in combinations(range(n), 6)]

    keys_exact_5 = {(s, x) for s, x in five}
    keys_exact_6 = {(s, x) for s, x in six}
    inter_exact = keys_exact_5 & keys_exact_6
    print(f"exact_(sum,xor)_collisions_between_shells={len(inter_exact)}")
    if inter_exact:
        print("IMPOSSIBILITY: same (sum mod M, xor) for every M for those pairs")
        k = next(iter(inter_exact))
        print(f"sample_key={k}")
        print("PASS")
        return

    for m in range(2, cap + 1):
        keys5 = {(s % m, x) for s, x in five}
        keys6 = {(s % m, x) for s, x in six}
        if keys5.isdisjoint(keys6):
            print("SEPARATOR_FOUND")
            print(f"M={m} scan_max={cap}")
            print(f"  |keys5|={len(keys5)} |keys6|={len(keys6)}")
            print("PASS")
            return

    print(f"NO_SEPARATOR_UP_TO_{cap}")
    print("INCONCLUSIVE")


if __name__ == "__main__":
    main()
