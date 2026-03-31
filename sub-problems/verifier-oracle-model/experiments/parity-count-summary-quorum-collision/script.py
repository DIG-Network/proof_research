#!/usr/bin/env python3
"""
Coarse summary h(k)=k mod 2 cannot decide strict threshold k >= t for n=10, t=6:
counts 4 (under) and 6 (at threshold) both even.
"""

from __future__ import annotations


def main() -> None:
    n = 10
    t = n // 2 + 1
    assert t == 6

    k_under = 4
    k_at = 6
    assert k_under < t
    assert k_at >= t

    h_under = k_under % 2
    h_at = k_at % 2
    assert h_under == h_at == 0

    print(f"n={n} t={t}")
    print(f"k_under={k_under} (quorum? {k_under >= t}) h={h_under}")
    print(f"k_at   ={k_at} (quorum? {k_at >= t}) h={h_at}")
    print("RESULT: PASS - parity of count aliases across threshold boundary")


if __name__ == "__main__":
    main()
