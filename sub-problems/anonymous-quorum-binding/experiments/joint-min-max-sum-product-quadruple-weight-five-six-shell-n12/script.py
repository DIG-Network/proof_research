#!/usr/bin/env python3
"""
n=12, w_i = i+1. Shells |S|=5 and |S|=6.

K(S) = (min w_i, max w_i, sum w_i, prod w_i) over i in S — exact integers.

Report whether any 5-set and 6-set share the same K (cross-shell collision).

Exit convention (repo toy experiments):
- PASS: cross-shell collision exists (hypothesis confirmed)
- FAIL: no cross-shell collision (hypothesis falsified; K injective on the union)
"""

from __future__ import annotations

import sys
from itertools import combinations
from math import comb, prod

N = 12


def weights() -> list[int]:
    return [i + 1 for i in range(N)]


def quad(ws: list[int], subset: tuple[int, ...]) -> tuple[int, int, int, int]:
    vals = [ws[i] for i in subset]
    return (min(vals), max(vals), sum(vals), prod(vals))


def shell_map(ws: list[int], r: int) -> dict[tuple[int, int, int, int], tuple[int, ...]]:
    m: dict[tuple[int, int, int, int], tuple[int, ...]] = {}
    for comb in combinations(range(N), r):
        k = quad(ws, comb)
        m.setdefault(k, comb)
    return m


def main() -> None:
    ws = weights()
    m5 = shell_map(ws, 5)
    m6 = shell_map(ws, 6)
    inter = set(m5) & set(m6)
    n5 = len(m5)
    n6 = len(m6)
    c5 = comb(N, 5)
    c6 = comb(N, 6)
    print(f"n={N} distinct_K_5={n5} (C(n,5)={c5}) distinct_K_6={n6} (C(n,6)={c6}) cross_shell_exact={len(inter)}")
    if inter:
        k = sorted(inter)[0]
        print(f"sample_exact_K={k} five={m5[k]} six={m6[k]}")
        print("PASS", flush=True)
        return
    print("FAIL_no_cross_shell_collision", flush=True)
    print("FAIL", flush=True)
    sys.exit(1)


if __name__ == "__main__":
    main()
