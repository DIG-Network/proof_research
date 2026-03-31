#!/usr/bin/env python3
"""
Unweighted elementary symmetric statistic on binary membership:

  e_d(S) = C(|S|, d)  =  #{d-subsets of S}

Pascal recurrence: C(t,d) = C(t-1,d) + C(t-1,d-1), hence for t >= d >= 1:

  C(t,d) - C(t-1,d) = C(t-1, d-1).

So for comparing quorum sizes t-1 vs t, modular reduction kills separation at degree d
iff M divides the integer C(t-1, d-1).

Entry 046 is d=2: delta = C(t-1,1) = t-1.
"""

from __future__ import annotations

import math


def main() -> None:
    for t in range(2, 40):
        for d in range(1, min(t, 15) + 1):
            lhs = math.comb(t, d) - math.comb(t - 1, d)
            rhs = math.comb(t - 1, d - 1)
            assert lhs == rhs, (t, d, lhs, rhs)

    t = 6
    print("PASS  Pascal check t in [2,39), d in [1,min(t,15)]")
    print(f"  example t={t} (sizes t-1=5 vs t=6), deltas C(t-1,d-1) for d>=1:")
    for d in range(1, t + 1):
        delta = math.comb(t - 1, d - 1)
        divs = [m for m in range(2, min(delta, 30) + 1) if delta % m == 0]
        print(f"    d={d:2d}  C(t,d)-C(t-1,d)={delta:4d}  sample M>1 with collision: {divs[:8]}")

    # Regression: d=2 row matches 046 (delta = t-1 = 5)
    assert math.comb(t, 2) - math.comb(t - 1, 2) == t - 1

    print("PASS")


if __name__ == "__main__":
    main()
