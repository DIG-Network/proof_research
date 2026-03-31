#!/usr/bin/env python3
"""
n=10, w_i = i+1. Shells |S|=5 and |S|=6.

K(S) = (min w_i, max w_i, sum w_i) over i in S — exact integers.
K_M = (min, max, sum mod M).

Report cross-shell collisions for K and first M with collision for K_M.
"""

from __future__ import annotations

import sys
from itertools import combinations

N = 10


def weights() -> list[int]:
    return [i + 1 for i in range(N)]


def triple(ws: list[int], subset: tuple[int, ...]) -> tuple[int, int, int]:
    vals = [ws[i] for i in subset]
    return (min(vals), max(vals), sum(vals))


def shell_map(
    ws: list[int], r: int
) -> dict[tuple[int, int, int], tuple[int, ...]]:
    m: dict[tuple[int, int, int], tuple[int, ...]] = {}
    for comb in combinations(range(N), r):
        k = triple(ws, comb)
        m.setdefault(k, comb)
    return m


def shell_map_mod(
    ws: list[int], r: int, mod: int
) -> dict[tuple[int, int, int], tuple[int, ...]]:
    m: dict[tuple[int, int, int], tuple[int, ...]] = {}
    for comb in combinations(range(N), r):
        mn, mx, s = triple(ws, comb)
        k = (mn, mx, s % mod)
        m.setdefault(k, comb)
    return m


def main() -> None:
    ws = weights()
    m5 = shell_map(ws, 5)
    m6 = shell_map(ws, 6)
    inter = set(m5) & set(m6)
    print(f"distinct_K_5={len(m5)} K_6={len(m6)} cross_shell_exact={len(inter)}")
    if inter:
        k = sorted(inter)[0]
        print(f"sample_exact_K={k} five={m5[k]} six={m6[k]}")

    first_m: int | None = None
    for mod in range(2, 500):
        m5m = shell_map_mod(ws, 5, mod)
        m6m = shell_map_mod(ws, 6, mod)
        interm = set(m5m) & set(m6m)
        if interm:
            first_m = mod
            k0 = sorted(interm)[0]
            print(
                f"first_mod_with_collision M={mod} cross_shell={len(interm)} "
                f"sample_Kmod={k0} five={m5m[k0]} six={m6m[k0]}"
            )
            break
    if first_m is None:
        print("no_mod_collision_M<500", flush=True)
        print("FAIL", flush=True)
        sys.exit(1)

    if not inter:
        print("FAIL_no_exact_collision", flush=True)
        sys.exit(1)

    print("PASS", flush=True)


if __name__ == "__main__":
    main()
