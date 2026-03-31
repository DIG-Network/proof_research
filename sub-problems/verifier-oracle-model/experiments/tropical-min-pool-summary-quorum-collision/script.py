#!/usr/bin/env python3
"""
h(S) = min_{i in S} c_i with fixed distinct costs c_i = i.
Both a 5-set and a 6-set containing index 0 give h = 0 at t=6.
Tropical / min-plus style one-number summary across quorum cut.
"""


def h_min(costs: list[int], subset: set[int]) -> int:
    return min(costs[i] for i in subset)


def main() -> None:
    n = 10
    t = n // 2 + 1
    assert t == 6
    costs = list(range(n))

    sa = {0, 1, 2, 3, 4}
    sb = {0, 5, 6, 7, 8, 9}
    assert len(sa) == t - 1 and len(sb) == t
    assert len(sa) < t <= len(sb)

    ha = h_min(costs, sa)
    hb = h_min(costs, sb)
    assert ha == hb == 0

    print(f"n={n} t={t}  c_i=i  h(S)=min_{{i in S}} c_i")
    print(f"S_a={sorted(sa)}  |S_a|={len(sa)}  h={ha}")
    print(f"S_b={sorted(sb)}  |S_b|={len(sb)}  h={hb}")
    print("RESULT: PASS - min-only tropical summary aliases across quorum boundary")


if __name__ == "__main__":
    main()
