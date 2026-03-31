#!/usr/bin/env python3
"""
n=10, w_i = i+1. Exhaust |S|=5 and |S|=6.

H(S) = XOR of w_i for i in S (bitwise).

Search for any 5-set and 6-set with equal H. Print first witness or NO_COLLISION.
"""

from __future__ import annotations

from functools import reduce
from itertools import combinations
from operator import xor


def main() -> None:
    n = 10
    w = [i + 1 for i in range(n)]

    def hx(indices: tuple[int, ...]) -> int:
        return reduce(xor, (w[i] for i in indices), 0)

    five = [(hx(t), t) for t in combinations(range(n), 5)]
    six = [(hx(t), t) for t in combinations(range(n), 6)]

    by_x5: dict[int, tuple[int, ...]] = {}
    for x, t in five:
        by_x5[x] = t

    for x, t6 in six:
        if x not in by_x5:
            continue
        t5 = by_x5[x]
        print("COLLISION")
        print(f"  xor_value={x} (decimal)  hex=0x{x:x}")
        print(f"  five-set indices={t5}")
        print(f"  six-set indices={t6}")
        print("PASS")
        return

    print("NO_COLLISION_5_vs_6_XOR")
    print("FAIL")


if __name__ == "__main__":
    main()
