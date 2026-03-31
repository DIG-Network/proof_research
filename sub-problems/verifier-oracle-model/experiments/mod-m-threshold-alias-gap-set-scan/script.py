#!/usr/bin/env python3
"""
For each n, t = floor(n/2)+1, compute crossing gap set D = {k2-k1 : 0<=k1<t<=k2<=n}.
Verify D = {1..n} and mod-m alias characterization (extends 081).
"""

from __future__ import annotations


def gap_set(n: int, t: int) -> set[int]:
    d: set[int] = set()
    for k1 in range(0, t):
        for k2 in range(t, n + 1):
            d.add(k2 - k1)
    return d


def aliases_at_m(n: int, t: int, m: int) -> bool:
    """Exists k1<t<=k2 with k1 ≡ k2 (mod m)."""
    for k1 in range(0, t):
        for k2 in range(t, n + 1):
            if k1 % m == k2 % m:
                return True
    return False


def first_clean_m(n: int, t: int) -> int:
    m = 2
    while True:
        if not aliases_at_m(n, t, m):
            return m
        m += 1
        if m > n + 5:
            raise RuntimeError("unexpected")


def main() -> None:
    for n in range(2, 31):
        t = n // 2 + 1
        d = gap_set(n, t)
        expected = set(range(1, n + 1))
        assert d == expected, (n, t, sorted(d), sorted(expected - d), sorted(d - expected))

        for m in range(2, n + 2):
            a = aliases_at_m(n, t, m)
            expect_alias = m <= n
            assert a == expect_alias, (n, t, m, a, expect_alias)

        assert first_clean_m(n, t) == n + 1

    # Stronger: D = {1..n} for every threshold t in [1,n] (not only majority).
    for n in range(2, 21):
        for t in range(1, n + 1):
            assert gap_set(n, t) == set(range(1, n + 1)), (n, t)
            for m in range(2, n + 2):
                assert aliases_at_m(n, t, m) == (m <= n), (n, t, m)
            assert first_clean_m(n, t) == n + 1

    print(
        "RESULT: PASS — majority t: n=2..30; plus all t in [1,n] for n<=20: "
        "D={1..n}; k mod m aliases across t iff 2<=m<=n; first clean m=n+1"
    )


if __name__ == "__main__":
    main()
