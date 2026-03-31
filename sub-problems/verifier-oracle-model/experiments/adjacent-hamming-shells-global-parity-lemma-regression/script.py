#!/usr/bin/env python3
"""
Regression: global XOR separates two adjacent Hamming shells k and k+1 on {0,1}^n.

For any x, popcount(x) mod 2 equals x_0 ⊕ ... ⊕ x_{n-1}. Consecutive k and k+1
have opposite parity, so one shell is all-even-popcount and the other all-odd
on that union — one parity gate separates them (the 092 phenomenon in general).

Exhaustive: generate all weight-k and weight-(k+1) masks via combinations for
n <= N_MAX. Tautology: k and k+1 opposite parity for n <= N_TAUTO (no 2^n).
"""

from __future__ import annotations

import sys
from itertools import combinations

N_MAX = 18  # binom(18,9) ~ 48k per shell worst; feasible
N_TAUTO = 200


def popc(m: int) -> int:
    return m.bit_count()


def xor_parity(m: int) -> int:
    return popc(m) % 2


def masks_fixed_weight(n: int, w: int) -> list[int]:
    return [sum(1 << i for i in comb) for comb in combinations(range(n), w)]


def check_pair(n: int, k: int) -> None:
    assert 0 <= k < n
    a = masks_fixed_weight(n, k)
    b = masks_fixed_weight(n, k + 1)
    assert len(a) == __import__("math").comb(n, k)
    assert len(b) == __import__("math").comb(n, k + 1)

    for m in a:
        assert popc(m) == k
        assert xor_parity(m) == (k % 2)
    for m in b:
        assert popc(m) == k + 1
        assert xor_parity(m) == ((k + 1) % 2)

    assert (k % 2) != ((k + 1) % 2)

    even_shell = k if k % 2 == 0 else k + 1
    odd_shell = k + 1 if k % 2 == 0 else k

    for m in a + b:
        p = xor_parity(m)
        w = popc(m)
        if p == 0:
            assert w == even_shell
        else:
            assert w == odd_shell


def main() -> None:
    for n in range(1, N_MAX + 1):
        for k in range(n):
            check_pair(n, k)
        print(f"n={n} all k OK (shells k,k+1 separated by global XOR parity)", flush=True)

    for n in (N_MAX + 1, N_TAUTO):
        for k in (0, 1, n // 2, max(0, n - 2)):
            if not (0 <= k < n):
                continue
            assert (k % 2) != ((k + 1) % 2)
        print(f"n={n} consecutive-k opposite-parity (sample k, no shell enum)", flush=True)

    print("PASS", flush=True)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FAIL", e, flush=True)
        sys.exit(1)
