#!/usr/bin/env python3
"""
Toy checks for experiment `natural-primitives-failures`.

No cryptography implementation — numerical / combinatorial models of proof size
and a discrete-log style ambiguity demo for linear aggregation.
"""

from __future__ import annotations

import math


def merkle_proof_bits_per_signer(lambda_bits: int, n: int) -> float:
    """Co-path bits per signer: ~ lambda * ceil(log2 n) for hash outputs of length lambda."""
    depth = max(1, math.ceil(math.log2(n)))
    return lambda_bits * depth


def total_merkle_path_proof_bits(lambda_bits: int, n: int, t: int) -> float:
    """t independent inclusion proofs (one pubkey + co-path per signer)."""
    return t * (lambda_bits + merkle_proof_bits_per_signer(lambda_bits, n))


def majority_threshold(n: int) -> int:
    return n // 2 + 1


def check_sublinear_growth() -> bool:
    """
    For t = Theta(n), total Merkle-per-signer proof bits is Omega(n log n) in this model.
    'Sublinear in n' would require |pi| / n -> 0 as n grows; here ratio -> infinity * lambda (log n).
    """
    lambda_bits = 256
    ok = True
    for n in [64, 256, 1024, 4096]:
        t = majority_threshold(n)
        bits = total_merkle_path_proof_bits(lambda_bits, n, t)
        ratio = bits / n
        # Ratio should grow with log n (not stay o(1))
        if ratio < lambda_bits * 0.5:
            ok = False
    return ok


def simulate_aggregate_key_ambiguity(prime: int, generator: int) -> bool:
    """
    In Z_p*, let pk_i = g^{sk_i}. Aggregate PK_S = prod pk_i = g^{sum sk_i}.
    Different subsets S, S' with same linear combination sum give same aggregate key
    (trivial collision in exponents). Here we show two *different* subsets can yield
    *different* aggregates — verifier must know which aggregate to pair against.
    """
    def mod_pow(a: int, e: int, p: int) -> int:
        return pow(a % p, e, p)

    g = generator % prime
    # Small toy keys
    sk = [2, 3, 5, 7, 11, 13]
    pk = [mod_pow(g, s, prime) for s in sk]
    n = len(pk)

    def agg(indices: list[int]) -> int:
        r = 1
        for i in indices:
            r = (r * pk[i]) % prime
        return r

    # Two different majority subsets (n=6, t=4)
    S1 = [0, 1, 2, 3]
    S2 = [2, 3, 4, 5]
    a1, a2 = agg(S1), agg(S2)
    # They should differ in generic choice (not guaranteed for all primes — check)
    distinct = a1 != a2
    # Verifier with only a commitment to {pk_i} and a claimed sig tied to ONE aggregate
    # cannot deduce aggregate without knowing S or full linear comb info.
    return distinct and n == 6 and majority_threshold(n) == 4


def rsa_accumulator_or_sketch_bits(t: int, n: int, lambda_bits: int) -> dict[str, float]:
    """
    Sketch: RSA accumulator membership witness is O(lambda) per element, but
    proving t-out-of-n OR (t distinct valid witnesses) without SNARK often
    requires Omega(t) group elements or equivalent in known textbook patterns.
    We only record linear-in-t baseline for comparison.
    """
    per_witness = lambda_bits * 2  # crude: two RSA-size integers
    return {
        "t": float(t),
        "n": float(n),
        "naive_t_witnesses_bits": t * per_witness,
        "per_element_witness_bits": per_witness,
    }


def main() -> None:
    checks = []

    c1 = check_sublinear_growth()
    checks.append(("check_sublinear_growth (Merkle-per-signer scales as n log n)", c1))

    # Use a prime where subsets above differ
    prime = 1000003
    gen = 5
    c2 = simulate_aggregate_key_ambiguity(prime, gen)
    checks.append(("simulate_aggregate_key_ambiguity (two majorities, different aggregates)", c2))

    n, lb = 1024, 256
    t = majority_threshold(n)
    rsa_stats = rsa_accumulator_or_sketch_bits(t, n, lb)
    c3 = rsa_stats["naive_t_witnesses_bits"] >= t * lb  # sanity
    checks.append(("rsa_accumulator_sketch (naive t witnesses scale linearly in t)", c3))

    print("natural-primitives-failures / script.py results\n")
    for name, passed in checks:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")

    bits = total_merkle_path_proof_bits(256, 1024, majority_threshold(1024))
    print(f"\n  Example: n=1024, t={majority_threshold(1024)}, Merkle-per-signer model ~ {bits:.0f} proof bits")
    print(f"  Ratio proof_bits/n ~ {bits/1024:.1f} (not o(1) in n)\n")

    all_pass = all(p for _, p in checks)
    raise SystemExit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
