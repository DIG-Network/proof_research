#!/usr/bin/env python3
"""
Explicit rogue-key style assignment: two distinct strict-majority subsets, same sum.

n=6, t=4. pk = [1,1,5,5,5,5].
S1 = {0,1,2,3}, S2 = {0,1,4,5} -> both sum 12.
"""

from __future__ import annotations

import itertools
from typing import List, Tuple


def majority_subsets(n: int) -> List[Tuple[int, ...]]:
    t = n // 2 + 1
    out: List[Tuple[int, ...]] = []
    for k in range(t, n + 1):
        out.extend(itertools.combinations(range(n), k))
    return out


def agg(s: Tuple[int, ...], pks: List[int]) -> int:
    return sum(pks[i] for i in s)


def distinct_U(pks: List[int], subs: List[Tuple[int, ...]]) -> int:
    return len({agg(s, pks) for s in subs})


def main() -> None:
    print("=== rogue-key-aggregate-collision ===\n")
    n = 6
    t = n // 2 + 1
    pks = [1, 1, 5, 5, 5, 5]
    s1 = (0, 1, 2, 3)
    s2 = (0, 1, 4, 5)
    subs = majority_subsets(n)
    W = len(subs)
    U = distinct_U(pks, subs)

    a1, a2 = agg(s1, pks), agg(s2, pks)
    print(f"n={n}, t={t}, pk={pks}")
    print(f"S1={s1}, Agg(S1)={a1}")
    print(f"S2={s2}, Agg(S2)={a2}")
    print(f"equal aggregates: {a1 == a2}")
    print(f"W={W}, U={U} (distinct majority subset sums)")

    assert len(s1) >= t and len(s2) >= t
    assert s1 != s2
    assert a1 == a2
    assert U < W

    print("\nVERDICT: PASS -- malicious pk forces Agg collision on two majorities.")

if __name__ == "__main__":
    main()
