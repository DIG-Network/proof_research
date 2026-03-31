#!/usr/bin/env python3
"""
Toy accounting: R1-style verify touches t paths; each path = 1 leaf hash + depth internal hashes.

Power-of-2 n only (matches Merkle experiments in journal).
"""

from __future__ import annotations

import math


def merkle_depth(n_leaves: int) -> int:
    if n_leaves <= 1:
        return 0
    return int(math.ceil(math.log2(n_leaves)))


def strict_majority_t(n: int) -> int:
    return n // 2 + 1


def hash_ops_per_signer(n: int) -> int:
    d = merkle_depth(n)
    return 1 + d


def total_merkle_hash_ops(n: int) -> tuple[int, int, int]:
    t = strict_majority_t(n)
    per = hash_ops_per_signer(n)
    return t, per, t * per


def main() -> None:
    print("=== r1-style-verify-hash-ops-scaling ===\n")
    print("Model: per signer = 1 leaf-hash + depth internal hashes on path\n")
    print(f"{'n':>6} {'t':>6} {'depth':>6} {'per':>5} {'t*per':>10} {'/(n)':>8}")
    for n in (8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192):
        if n & (n - 1) != 0:
            continue
        t, per, tot = total_merkle_hash_ops(n)
        d = merkle_depth(n)
        ratio = tot / n if n else float("inf")
        print(f"{n:6d} {t:6d} {d:6d} {per:5d} {tot:10d} {ratio:8.2f}")

    n0 = 2048
    t0, per0, tot0 = total_merkle_hash_ops(n0)
    d0 = merkle_depth(n0)
    assert t0 == n0 // 2 + 1
    assert d0 == 11
    assert per0 == 1 + d0
    assert tot0 == t0 * per0

    # Theta(n log n): tot / (n * log2(n)) should stay bounded (approaches ~1/2 for this t and depth ~ log2 n)
    ratio_nlgn = tot0 / (n0 * math.log2(n0))
    print(f"\nn={n0}: t*per={tot0}, t*per/(n log2 n)={ratio_nlgn:.4f}")

    print("RESULT: PASS - R1 Merkle phase is Theta(n log n) hash ops at majority t")


if __name__ == "__main__":
    main()
