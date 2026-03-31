#!/usr/bin/env python3
"""
n=10, w_i = i+1. Shells |S|=5 and |S|=6.

h_gcd(S) = gcd of all w_i for i in S.
Also joint J(S) = (h_gcd(S), sum_w(S)) with exact integer sum.

Report cross-shell collisions for h_gcd and for J.
PASS if both have >=1 collision (expected refutation of shell separation).
"""

from __future__ import annotations

import math
import sys
from itertools import combinations

N = 10


def weights() -> list[int]:
    return [i + 1 for i in range(N)]


def subset_gcd(ws: list[int], subset: tuple[int, ...]) -> int:
    g = ws[subset[0]]
    for i in subset[1:]:
        g = math.gcd(g, ws[i])
    return g


def subset_sum(ws: list[int], subset: tuple[int, ...]) -> int:
    return sum(ws[i] for i in subset)


def shell_map_gcd(ws: list[int], r: int) -> dict[int, tuple[int, ...]]:
    m: dict[int, tuple[int, ...]] = {}
    for comb in combinations(range(N), r):
        v = subset_gcd(ws, comb)
        m.setdefault(v, comb)
    return m


def shell_map_joint(ws: list[int], r: int) -> dict[tuple[int, int], tuple[int, ...]]:
    m: dict[tuple[int, int], tuple[int, ...]] = {}
    for comb in combinations(range(N), r):
        key = (subset_gcd(ws, comb), subset_sum(ws, comb))
        m.setdefault(key, comb)
    return m


def main() -> None:
    ws = weights()
    m5g = shell_map_gcd(ws, 5)
    m6g = shell_map_gcd(ws, 6)
    m5j = shell_map_joint(ws, 5)
    m6j = shell_map_joint(ws, 6)

    inter_g = set(m5g) & set(m6g)
    inter_j = set(m5j) & set(m6j)

    print(f"distinct_h_gcd_5={len(m5g)} 6={len(m6g)} cross_shell_gcd={len(inter_g)}")
    print(f"distinct_joint_gcd_sum_5={len(m5j)} 6={len(m6j)} cross_shell_joint={len(inter_j)}")

    if inter_g:
        g = min(inter_g)
        print(f"sample_h_gcd={g} five={m5g[g]} six={m6g[g]}")
    if inter_j:
        k = min(inter_j)
        print(f"sample_joint={k} five={m5j[k]} six={m6j[k]}")

    if not inter_g or not inter_j:
        print("FAIL", flush=True)
        sys.exit(1)
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
