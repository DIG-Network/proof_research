#!/usr/bin/env python3
"""
Idealized verifier budgets for Link(C, K) style statements.

Compares proof-bit and hash-operation scalings for:
  M1: t independent Merkle paths (depth ceil(log2 n))
  M2: one Merkle path + claim "aggregate" without per-index auth (unsound baseline)
  M3: t-fold repetition of a constant-size proof (generic OR) -> Omega(t) proof elements

Uses n, t = floor(n/2)+1 (strict majority).
"""

from __future__ import annotations

import math


def merkle_depth(n: int) -> int:
    return max(0, int(math.ceil(math.log2(n)))) if n > 0 else 0


def bits_per_path(lambda_bits: int, depth: int, n: int) -> int:
    """Each path: depth sibling hashes + index bits O(log n)."""
    return depth * lambda_bits + max(16, int(math.ceil(math.log2(max(n, 2)))))


def model_merkle_t_paths(n: int, t: int, lambda_bits: int = 256) -> dict:
    d = merkle_depth(n)
    per = bits_per_path(lambda_bits, d, n)
    return {
        "name": "Merkle: t independent inclusion paths",
        "proof_bits": t * per,
        "hash_ops_verifier": t * (2 * d),  # sibling checks ~ 2d hashes per path (toy)
        "scaling_in_n_when_t_majority": "Theta(n log n) bits when t = Theta(n)",
    }


def model_naive_single_path(n: int, lambda_bits: int = 256) -> dict:
    d = merkle_depth(n)
    per = bits_per_path(lambda_bits, d, n)
    return {
        "name": "Merkle: ONE path only (unsound for threshold — no per-signer bind)",
        "proof_bits": per,
        "hash_ops_verifier": 2 * d,
        "scaling_in_n_when_t_majority": "O(log n) — INCOMPLETE Link",
    }


def model_t_or_of_constant_proofs(t: int, constant_proof_bits: int = 256) -> dict:
    return {
        "name": "Naive OR: t copies of constant-size disjunct",
        "proof_bits": t * constant_proof_bits,
        "hash_ops_verifier": t * 8,
        "scaling_in_n_when_t_majority": "Theta(n) when t = Theta(n)",
    }


def main() -> None:
    print("=== vc-opening-budget ===")
    lambda_bits = 256
    for n in (64, 256, 1024, 4096):
        t = n // 2 + 1
        m1 = model_merkle_t_paths(n, t, lambda_bits)
        m2 = model_naive_single_path(n, lambda_bits)
        m3 = model_t_or_of_constant_proofs(t, 256)
        print(f"\nn={n}, strict-majority t={t}, Merkle depth ~ {merkle_depth(n)}")
        print(f"  {m1['name']}")
        print(f"    proof_bits ~ {m1['proof_bits']}, ratio proof_bits/n = {m1['proof_bits']/n:.2f}")
        print(f"  {m2['name']}")
        print(f"    proof_bits ~ {m2['proof_bits']} (soundness NOT achieved for threshold)")
        print(f"  {m3['name']}")
        print(f"    proof_bits ~ {m3['proof_bits']}, ratio proof_bits/n = {m3['proof_bits']/n:.2f}")

    # Majority regime: ratios should not be o(1)
    n = 2048
    t = n // 2 + 1
    m1 = model_merkle_t_paths(n, t, lambda_bits)
    ratio = m1["proof_bits"] / n
    print("\n--- check: Merkle-per-signer ratio vs o(1) ---")
    print(f"n={n}, ratio proof_bits/n = {ratio:.2f}")
    assert ratio > 10, "expect large constant * log n growth vs n"

    print("\nVERDICT LINE: PASS for hypothesis that M1/M3 scale Omega(n) in majority regime;")
    print("M2 is sublinear but does not implement Link.")


if __name__ == "__main__":
    main()
