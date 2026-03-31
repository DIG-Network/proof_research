#!/usr/bin/env python3
"""
n=10, w_i = i+1. Shells |S|=5 and |S|=6.

h_lcm(S) = lcm of all w_i for i in S.
Joint J(S) = (h_lcm(S), sum_w(S)) exact integers.

Report cross-shell collisions for h_lcm and for J.
PASS if both have >=1 collision (refutes standalone shell separation).
"""

from __future__ import annotations

import math
import sys
from itertools import combinations

N = 10


def weights() -> list[int]:
    return [i + 1 for i in range(N)]


def subset_lcm(ws: list[int], subset: tuple[int, ...]) -> int:
    L = ws[subset[0]]
    for i in subset[1:]:
        L = L * ws[i] // math.gcd(L, ws[i])
    return L


def subset_sum(ws: list[int], subset: tuple[int, ...]) -> int:
    return sum(ws[i] for i in subset)


def shell_map_lcm(ws: list[int], r: int) -> dict[int, tuple[int, ...]]:
    m: dict[int, tuple[int, ...]] = {}
    for comb in combinations(range(N), r):
        v = subset_lcm(ws, comb)
        m.setdefault(v, comb)
    return m


def shell_map_joint(ws: list[int], r: int) -> dict[tuple[int, int], tuple[int, ...]]:
    m: dict[tuple[int, int], tuple[int, ...]] = {}
    for comb in combinations(range(N), r):
        key = (subset_lcm(ws, comb), subset_sum(ws, comb))
        m.setdefault(key, comb)
    return m


def main() -> None:
    ws = weights()
    m5l = shell_map_lcm(ws, 5)
    m6l = shell_map_lcm(ws, 6)
    m5j = shell_map_joint(ws, 5)
    m6j = shell_map_joint(ws, 6)

    inter_l = set(m5l) & set(m6l)
    inter_j = set(m5j) & set(m6j)

    print(f"distinct_h_lcm_5={len(m5l)} 6={len(m6l)} cross_shell_lcm={len(inter_l)}")
    print(
        f"distinct_joint_lcm_sum_5={len(m5j)} 6={len(m6j)} cross_shell_joint={len(inter_j)}"
    )

    if inter_l:
        g = min(inter_l)
        print(f"sample_h_lcm={g} five={m5l[g]} six={m6l[g]}")
    if inter_j:
        k = min(inter_j)
        print(f"sample_joint={k} five={m5j[k]} six={m6j[k]}")

    if not inter_l or not inter_j:
        print("FAIL", flush=True)
        sys.exit(1)
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
