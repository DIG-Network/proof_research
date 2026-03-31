#!/usr/bin/env python3
"""
n=10, weights w_i = i+1 (values 1..10). Find 5-subset and 6-subset with equal
integer sum (threshold toy: t=6 vs |S|=5).
"""

from __future__ import annotations

import itertools

N = 10
SIZE_FIVE = 5
SIZE_SIX = 6
WEIGHTS = [i + 1 for i in range(N)]


def main() -> None:
    verts = list(range(N))
    by_sum: dict[int, tuple[int, ...]] = {}
    for s in itertools.combinations(verts, SIZE_FIVE):
        total = sum(WEIGHTS[i] for i in s)
        by_sum[total] = s

    for t in itertools.combinations(verts, SIZE_SIX):
        total = sum(WEIGHTS[i] for i in t)
        if total not in by_sum:
            continue
        s = by_sum[total]
        print(f"Equal integer sum = {total}")
        print(f"  |S|={SIZE_FIVE}: indices {s} -> weights {[WEIGHTS[i] for i in s]}")
        print(f"  |T|={SIZE_SIX}: indices {t} -> weights {[WEIGHTS[i] for i in t]}")
        print(
            "RESULT: PASS - integer linear aggregate aliases 5-set vs 6-set"
        )
        return

    print("RESULT: FAIL - no 5-set and 6-set share same integer weight sum")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
