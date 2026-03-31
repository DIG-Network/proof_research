#!/usr/bin/env python3
"""
n=10, public weights w_i = i+1 (i in 0..9 -> 1..10).

Shell A: |S|=5, Shell B: |S|=6.

h_and(S) = bitwise AND of w_i over i in S.
h_or(S)  = bitwise OR  of w_i over i in S.

Report cross-shell image intersections (same h value realized by some 5-set and some 6-set).
Exit 0 = PASS (hypothesis: cross-shell collisions exist for both summaries).
Exit 1 = FAIL (at least one summary has disjoint shell images on this toy).
"""

from __future__ import annotations

import sys
from itertools import combinations

N = 10


def weights() -> list[int]:
    return [i + 1 for i in range(N)]


def h_and(ws: list[int], subset: tuple[int, ...]) -> int:
    a = ws[subset[0]]
    for i in subset[1:]:
        a &= ws[i]
    return a


def h_or(ws: list[int], subset: tuple[int, ...]) -> int:
    a = 0
    for i in subset:
        a |= ws[i]
    return a


def shell_maps(ws: list[int], r: int, fn) -> dict[int, list[tuple[int, ...]]]:
    m: dict[int, list[tuple[int, ...]]] = {}
    for comb in combinations(range(N), r):
        v = fn(ws, comb)
        m.setdefault(v, []).append(comb)
    return m


def main() -> None:
    ws = weights()
    m5a = shell_maps(ws, 5, h_and)
    m6a = shell_maps(ws, 6, h_and)
    m5o = shell_maps(ws, 5, h_or)
    m6o = shell_maps(ws, 6, h_or)

    inter_and = set(m5a) & set(m6a)
    inter_or = set(m5o) & set(m6o)

    print(f"distinct_h_and_values_5={len(m5a)} 6={len(m6a)}")
    print(f"cross_shell_h_and_collisions={len(inter_and)}")
    print(f"distinct_h_or_values_5={len(m5o)} 6={len(m6o)}")
    print(f"cross_shell_h_or_collisions={len(inter_or)}")

    if inter_and:
        v = min(inter_and)
        s5 = m5a[v][0]
        s6 = m6a[v][0]
        print(f"sample_h_and={v} five_set={s5} six_set={s6}")
    if inter_or:
        v = min(inter_or)
        s5 = m5o[v][0]
        s6 = m6o[v][0]
        print(f"sample_h_or={v} five_set={s5} six_set={s6}")

    if not inter_and or not inter_or:
        print("FAIL unexpected_disjoint_shell_image", flush=True)
        sys.exit(1)

    print("PASS", flush=True)


if __name__ == "__main__":
    main()
