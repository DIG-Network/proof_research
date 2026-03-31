#!/usr/bin/env python3
"""
n=10 validators, weights w_i = i+1. For each M in 1..MAX_M, check if some 5-subset
and some 6-subset have equal sum mod M (threshold toy: t=6).
"""

from __future__ import annotations

import itertools

N = 10
T_QUORUM = 6
SIZE_A = 5
WEIGHTS = [i + 1 for i in range(N)]  # 1..10
MAX_M = 50


def main() -> None:
    verts = list(range(N))
    combs5 = list(itertools.combinations(verts, SIZE_A))
    combs6 = list(itertools.combinations(verts, T_QUORUM))

    for m in range(2, MAX_M + 1):
        sums5: dict[int, tuple[int, ...]] = {}
        for s in combs5:
            r = sum(WEIGHTS[i] for i in s) % m
            sums5[r] = s
        for t in combs6:
            r = sum(WEIGHTS[i] for i in t) % m
            if r in sums5:
                sa = sums5[r]
                print(f"M={m} residue={r}")
                print(f"  |S|={SIZE_A} sum mod M == r: indices {sa} (int sum={sum(WEIGHTS[i] for i in sa)})")
                print(f"  |T|={T_QUORUM} sum mod M == r: indices {t} (int sum={sum(WEIGHTS[i] for i in t)})")
                print(
                    "RESULT: PASS - mod-M weighted sum aliases 5-set vs 6-set for this public weight vector"
                )
                return

    print(
        f"RESULT: FAIL - no cross-cardinality collision for w_i=i+1 with any M in 1..{MAX_M}"
    )
    raise SystemExit(1)


if __name__ == "__main__":
    main()
