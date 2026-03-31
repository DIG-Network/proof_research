#!/usr/bin/env python3
"""
Public weights v_i = (i+1)^2 on indices 0..n-1 (default n=10).
Find smallest M >= 2 such that some (t-1)-subset and some t-subset have equal
sum of v_i mod M (default t=6).

Compare: zmodm-weighted-sum-five-vs-six-collision (linear weights), 047 (elementary symmetric mod M).
"""

from __future__ import annotations

from itertools import combinations


def sum_sq_mod(subset: tuple[int, ...], m: int) -> int:
    s = 0
    for i in subset:
        s = (s + (i + 1) * (i + 1)) % m
    return s


def residue_sets_mod2(n: int, t: int) -> tuple[set[int], set[int]]:
    m = 2
    fives = list(combinations(range(n), t - 1))
    sixes = list(combinations(range(n), t))
    return {sum_sq_mod(f, m) for f in fives}, {sum_sq_mod(g, m) for g in sixes}


def smallest_collision_m(n: int, t: int, m_hi: int) -> tuple[int, tuple[int, ...], tuple[int, ...], int] | None:
    fives = list(combinations(range(n), t - 1))
    sixes = list(combinations(range(n), t))
    for m in range(2, m_hi + 1):
        for g in sixes:
            rg = sum_sq_mod(g, m)
            for f in fives:
                if sum_sq_mod(f, m) == rg:
                    return (m, f, g, rg)
    return None


def main() -> None:
    n, t = 10, 6
    r5, r6 = residue_sets_mod2(n, t)
    print(f"M=2 residues (t-1)-sets: {sorted(r5)}  t-sets: {sorted(r6)}  intersect={sorted(r5 & r6)}")

    hit = smallest_collision_m(n, t, m_hi=5000)
    if hit is None:
        print("FAIL: no collision up to m_hi")
        raise SystemExit(1)

    m, f, g, r = hit
    sf = sum((i + 1) ** 2 for i in f)
    sg = sum((i + 1) ** 2 for i in g)
    print(f"smallest_M_with_collision={m} residue_mod_M={r}")
    print(f"  F (|={len(f)}): {f}  int_sum_sq={sf}")
    print(f"  G (|={len(g)}): {g}  int_sum_sq={sg}")
    print("PASS")


if __name__ == "__main__":
    main()
