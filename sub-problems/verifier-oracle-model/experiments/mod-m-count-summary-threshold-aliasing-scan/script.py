#!/usr/bin/env python3
"""
Scan h(k)=k mod m for cross-threshold aliasing on k in [0,n], t=floor(n/2)+1.

For each m, find lex-smallest (k_under, k_at) with k_under < t <= k_at and
k_under % m == k_at % m, or report NONE.
"""

from __future__ import annotations


def first_witness(n: int, t: int, m: int) -> tuple[int, int] | None:
    for k1 in range(0, t):
        for k2 in range(t, n + 1):
            if k1 % m == k2 % m:
                return (k1, k2)
    return None


def all_gaps_realizable(n: int, t: int) -> set[int]:
    gaps: set[int] = set()
    for k1 in range(0, t):
        for k2 in range(t, n + 1):
            gaps.add(k2 - k1)
    return gaps


def main() -> None:
    n = 10
    t = n // 2 + 1
    assert t == 6

    gaps = all_gaps_realizable(n, t)
    assert gaps == set(range(1, n + 1)), (gaps, "expected full 1..n for n=10,t=6")

    print(f"n={n} t={t}")
    print("realizable gaps k2-k1 (k1<t<=k2):", sorted(gaps))
    print()

    first_no_alias: int | None = None
    for m in range(2, n + 15):
        w = first_witness(n, t, m)
        if w is None:
            if first_no_alias is None:
                first_no_alias = m
            print(f"m={m:3d}  NO cross-threshold alias (h separates classes on [0,n])")
        else:
            k1, k2 = w
            print(
                f"m={m:3d}  witness k_under={k1} k_at={k2} "
                f"residue={k1 % m}  (quorum? {k1 >= t} vs {k2 >= t})"
            )

    assert first_no_alias == n + 1, f"expected first clean m at n+1={n+1}, got {first_no_alias}"

    # H1: alias iff m <= n
    for m in range(2, 200):
        w = first_witness(n, t, m)
        aliases = w is not None
        expect = m <= n
        assert aliases == expect, f"m={m}: alias={aliases} expected {expect}"

    print()
    print("RESULT: PASS — m<=n always has a witness; first m with NONE is n+1=11")


if __name__ == "__main__":
    main()
