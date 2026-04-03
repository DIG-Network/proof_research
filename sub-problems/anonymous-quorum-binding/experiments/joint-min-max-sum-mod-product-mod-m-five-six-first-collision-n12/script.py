#!/usr/bin/env python3
"""
n=12, w_i = i+1. Shells |S|=5 and |S|=6.

K_M(S) = (min w_i, max w_i, (sum w_i) mod M, (prod w_i) mod M).

Scan M = 2, 3, ... until the first M where some 5-set and some 6-set share the same K_M
(cross-shell collision). Report that M and one witness pair.

Exit convention (repo toy experiments):
- PASS: hypothesis "first collision M is 2" confirmed (first_hit_M == 2)
- FAIL: first collision strictly larger than 2 (hypothesis falsified)
"""

from __future__ import annotations

import sys
from itertools import combinations

N = 12
HYP_FIRST_M = 2


def weights() -> list[int]:
    return [i + 1 for i in range(N)]


def key_mod(ws: list[int], subset: tuple[int, ...], m: int) -> tuple[int, int, int, int]:
    vals = [ws[i] for i in subset]
    mn, mx = min(vals), max(vals)
    s = sum(vals) % m
    p = 1
    for v in vals:
        p = (p * v) % m
    return (mn, mx, s, p)


def first_collision_m(ws: list[int], m_max: int) -> tuple[int, tuple[int, int, int, int], tuple[int, ...], tuple[int, ...]] | None:
    for m in range(2, m_max + 1):
        m5: dict[tuple[int, int, int, int], tuple[int, ...]] = {}
        m6: dict[tuple[int, int, int, int], tuple[int, ...]] = {}
        for comb in combinations(range(N), 5):
            k = key_mod(ws, comb, m)
            m5.setdefault(k, comb)
        for comb in combinations(range(N), 6):
            k = key_mod(ws, comb, m)
            m6.setdefault(k, comb)
        inter = set(m5) & set(m6)
        if inter:
            k0 = sorted(inter)[0]
            return (m, k0, m5[k0], m6[k0])
    return None


def main() -> None:
    ws = weights()
    m_max = 5000
    hit = first_collision_m(ws, m_max)
    if hit is None:
        print(f"INCONCLUSIVE_no_cross_shell_collision_M<= {m_max}")
        print("INCONCLUSIVE", flush=True)
        sys.exit(2)

    m0, key, five, six = hit
    print(f"n={N} first_collision_M={m0} K_M={key} five={five} six={six}")
    print(f"hypothesis_first_M={HYP_FIRST_M}")
    if m0 == HYP_FIRST_M:
        print("PASS", flush=True)
        return
    print("FAIL", flush=True)
    sys.exit(1)


if __name__ == "__main__":
    main()
