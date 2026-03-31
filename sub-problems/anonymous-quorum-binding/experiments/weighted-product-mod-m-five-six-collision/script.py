#!/usr/bin/env python3
"""
Public weights w_i = i+1 for indices i in {0,...,n-1}.
Find smallest M >= 2 such that some (t-1)-subset and some t-subset have equal
product mod M (default n=10, t=6).

Compare: zmodm-weighted-sum-five-vs-six-collision (additive mod M).
"""

from __future__ import annotations

from itertools import combinations


def prod_mod(subset: tuple[int, ...], m: int) -> int:
    p = 1
    for i in subset:
        p = (p * (i + 1)) % m
    return p


def smallest_collision_m(
    n: int, t: int, m_hi: int
) -> tuple[int, tuple[int, ...], tuple[int, ...], int] | None:
    fives = list(combinations(range(n), t - 1))
    sixes = list(combinations(range(n), t))
    for m in range(2, m_hi + 1):
        for g in sixes:
            rg = prod_mod(g, m)
            for f in fives:
                if prod_mod(f, m) == rg:
                    return (m, f, g, rg)
    return None


def m2_residue_sets(n: int, t: int) -> tuple[set[int], set[int]]:
    m = 2
    fives = list(combinations(range(n), t - 1))
    sixes = list(combinations(range(n), t))
    return {prod_mod(f, m) for f in fives}, {prod_mod(g, m) for g in sixes}


def main() -> None:
    n, t = 10, 6
    r5, r6 = m2_residue_sets(n, t)
    print(f"M=2 residues (t-1)-sets: {sorted(r5)}  t-sets: {sorted(r6)}  intersect={sorted(r5 & r6)}")

    hit = smallest_collision_m(n, t, m_hi=5000)
    if hit is None:
        print("FAIL: no collision up to m_hi")
        raise SystemExit(1)

    m, f, g, r = hit
    pf = 1
    for i in f:
        pf *= i + 1
    pg = 1
    for i in g:
        pg *= i + 1
    print(f"smallest_M_with_collision={m} residue_mod_M={r}")
    print(f"  F (|={len(f)}): {f}  int_prod={pf}")
    print(f"  G (|={len(g)}): {g}  int_prod={pg}")
    print("PASS")


if __name__ == "__main__":
    main()
