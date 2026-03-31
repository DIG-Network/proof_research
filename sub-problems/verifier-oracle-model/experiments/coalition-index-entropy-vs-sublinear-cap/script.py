#!/usr/bin/env python3
"""
Compare log2(binom(n, t)) for t = floor(n/2)+1 vs stylized B(n) = lambda * (log2 n)^2
(same cap family as sublinear-pi-merkle-clash).

Uses sum of logs to avoid bigint combinatorial explosion.
"""

from __future__ import annotations

import math


def log2_binom(n: int, k: int) -> float:
    """log2(C(n,k)), k in [0,n], via sum log2((n-k+i)/i)."""
    if k < 0 or k > n:
        return float("-inf")
    if k == 0 or k == n:
        return 0.0
    k = min(k, n - k)
    s = 0.0
    for i in range(1, k + 1):
        s += math.log2((n - k + i) / i)
    return s


def strict_majority_t(n: int) -> int:
    return n // 2 + 1


def stylized_cap(n: int, lambda_bits: int, k_exp: int) -> float:
    lg = math.log2(max(n, 2))
    return float(lambda_bits * (lg**k_exp))


def main() -> None:
    lambda_bits = 256
    k_exp = 2
    print("=== coalition-index-entropy-vs-sublinear-cap ===\n")
    print(f"B(n) = {lambda_bits} * (log2 n)^{k_exp}\n")
    print(f"{'n':>8} {'t':>8} {'log2_binom':>14} {'B(n)':>14} {'ratio':>10}")
    crossover = None
    for n in (
        128,
        256,
        512,
        1024,
        2048,
        4096,
        8192,
        16384,
        32768,
        65536,
        131072,
        262144,
    ):
        t = strict_majority_t(n)
        lb = log2_binom(n, t)
        cap = stylized_cap(n, lambda_bits, k_exp)
        ratio = lb / cap if cap else float("inf")
        print(f"{n:8d} {t:8d} {lb:14.2f} {cap:14.2f} {ratio:10.4f}")
        if crossover is None and lb > cap:
            crossover = n

    assert crossover is not None, "expect log2_binom to exceed B(n) for some n in table"
    print(f"\nSmallest n in table with log2_binom > B(n): {crossover}")

    # Tight check at first crossover row
    t0 = strict_majority_t(crossover)
    assert log2_binom(crossover, t0) > stylized_cap(crossover, lambda_bits, k_exp)

    print("RESULT: PASS - injective minimal-coalition index needs Omega(n) bits; exceeds polylog B at large n")


if __name__ == "__main__":
    main()
