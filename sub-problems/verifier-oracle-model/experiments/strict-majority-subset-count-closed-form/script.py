#!/usr/bin/env python3
"""
Brute count of strict-majority subsets vs classical closed forms.

t = floor(n/2)+1; N(n) = sum_{k=t}^n C(n,k).

Odd n:  N = 2^(n-1)
Even n: N = (2^n - C(n, n/2)) / 2
"""

from __future__ import annotations

import math


def strict_majority_t(n: int) -> int:
    return n // 2 + 1


def brute_count(n: int) -> int:
    t = strict_majority_t(n)
    return sum(math.comb(n, k) for k in range(t, n + 1))


def closed_form(n: int) -> int:
    if n % 2 == 1:
        return 2 ** (n - 1)
    half = n // 2
    return (2**n - math.comb(n, half)) // 2


def log2_approx(x: int) -> float:
    return math.log2(x) if x > 0 else float("-inf")


def stylized_cap(n: int, lambda_bits: int = 256, k_exp: int = 2) -> float:
    lg = math.log2(max(n, 2))
    return float(lambda_bits * (lg**k_exp))


def main() -> None:
    print("=== strict-majority-subset-count-closed-form ===\n")
    for n in range(1, 26):
        b = brute_count(n)
        c = closed_form(n)
        assert b == c, f"mismatch n={n}: brute={b} closed={c}"

    print("Brute vs closed form: OK for n = 1..25\n")

    print(f"{'n':>4} {'N(n)':>12} {'log2 N':>10} {'B(n)':>10} {'odd':>5}")
    for n in (7, 8, 15, 16, 31, 32, 63, 64, 127, 128):
        nn = closed_form(n)
        cap = stylized_cap(n)
        print(
            f"{n:4d} {nn:12d} {log2_approx(nn):10.3f} {cap:10.1f} "
            f"{'yes' if n % 2 else 'no':>5}"
        )
        if n % 2 == 1:
            assert nn == 2 ** (n - 1)

    print("\nRESULT: PASS - identities verified; log2 N(n) grows Theta(n)")


if __name__ == "__main__":
    main()
