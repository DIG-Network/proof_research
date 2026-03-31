#!/usr/bin/env python3
"""
Compare M1 Merkle-per-majority-signer bit budget vs a stylized o(n) cap: lambda * (log2 n)^k.

Uses same bits_per_path model as vc-opening-budget (depth * lambda + index bits).
"""

from __future__ import annotations

import math


def merkle_depth(n: int) -> int:
    return max(0, int(math.ceil(math.log2(n)))) if n > 0 else 0


def bits_per_path(lambda_bits: int, depth: int, n: int) -> int:
    return depth * lambda_bits + max(16, int(math.ceil(math.log2(max(n, 2)))))


def m1_total_bits(n: int, lambda_bits: int = 256) -> tuple[int, int, int]:
    t = n // 2 + 1
    d = merkle_depth(n)
    per = bits_per_path(lambda_bits, d, n)
    return t, per, t * per


def stylized_sublinear_cap(n: int, lambda_bits: int, k: int) -> int:
    """B = lambda * (log2 n)^k  (bits) — grows polylog, not used as serious lower bound proof."""
    lg = math.log2(max(n, 2))
    return int(lambda_bits * (lg**k))


def main() -> None:
    print("=== sublinear-pi-merkle-clash ===\n")
    lambda_bits = 256
    k = 2
    print(f"Stylized 'generous' sublinear cap: B(n) = {lambda_bits} * (log2 n)^{k}\n")

    for n in (128, 256, 512, 1024, 2048, 4096, 8192):
        t, per, total = m1_total_bits(n, lambda_bits)
        cap = stylized_sublinear_cap(n, lambda_bits, k)
        ratio = total / cap if cap else float("inf")
        print(f"n={n:5d}  t={t:5d}  bits/path~{per:5d}  M1_total~{total:10d}  B(n)~{cap:7d}  ratio M1/B~{ratio:8.2f}")

    # Assert clash at n=2048 (same spirit as vc-opening-budget)
    n0 = 2048
    _, _, total0 = m1_total_bits(n0, lambda_bits)
    cap0 = stylized_sublinear_cap(n0, lambda_bits, k)
    assert total0 > cap0 * 85, "expect large separation at n=2048 (ratio ~94x for this model)"

    print("\nVERDICT: PASS -- M1 majority-Merkle bits >> lambda*polylog(n) cap at moderate n.")

if __name__ == "__main__":
    main()
