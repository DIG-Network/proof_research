#!/usr/bin/env python3
"""
Sanity checks for sub-problem verifier-oracle-model / experiment info-theoretic-barrier.

Interprets 'sublinear proof' combinatorially: how many bits are needed to
distinguish quorum subsets if the proof must act as (near-)injective metadata
for subset-dependent verification keys in a naive encoding.

Also prints a toy algebraic reminder: linear aggregate 'public key' depends on
which cosigner set is assumed — constant-size π cannot name an arbitrary subset
without compression or extra structure.
"""

from __future__ import annotations

import hashlib
import math


def merkle_root(leaves: list[bytes]) -> bytes:
    if not leaves:
        return hashlib.sha256(b"").digest()
    level = [hashlib.sha256(b"L" + x).digest() for x in leaves]
    while len(level) > 1:
        nxt = []
        for i in range(0, len(level), 2):
            if i + 1 < len(level):
                nxt.append(hashlib.sha256(b"I" + level[i] + level[i + 1]).digest())
            else:
                nxt.append(level[i])
        level = nxt
    return level[0]


def count_majority_subsets(n: int) -> int:
    t = n // 2 + 1
    # sum_{k=t}^{n} C(n,k)
    total = 0
    for k in range(t, n + 1):
        total += math.comb(n, k)
    return total


def bits_needed_to_index_majority_subsets(n: int) -> float:
    return math.log2(count_majority_subsets(n))


def main() -> None:
    print("=== info-theoretic-barrier script ===")
    n = 64
    t = n // 2 + 1
    mcount = count_majority_subsets(n)
    bits = bits_needed_to_index_majority_subsets(n)
    print(f"n={n}, strict-majority threshold t={t}")
    print(f"number of distinct strict-majority subsets: {mcount}")
    print(f"log2(count) ~ {bits:.2f} bits to injectively index subsets")

    # Toy 'keys' as bytes; Merkle root is O(lambda) regardless of n (here fixed hash)
    keys = [hashlib.sha256(f"pk-{i}".encode()).digest() for i in range(n)]
    root = merkle_root(keys)
    print(f"toy Merkle root (32 bytes): {root.hex()[:16]}...")

    # If verification key for BLS-like aggregation were uniquely determined by
    # subset S, injective encoding of S needs >= log2(|{S:|S|>=t}|) bits in worst case.
    constant_size_pi_bits = 256  # e.g., one group element + a few scalars
    print(f"constant-size pi assumption: ~{constant_size_pi_bits} bits payload")
    if bits > constant_size_pi_bits:
        print(
            "RESULT_HINT: injective subset metadata cannot fit in constant-size pi "
            "without compression / structure; verifier must get subset info elsewhere "
            "or use non-injective (ambiguous) encoding (soundness risk)."
        )
    else:
        print("RESULT_HINT: for this n, injective index could fit — scale n.")

    # Algebraic reminder: two different majority subsets -> two different aggregate keys
    # (model integers mod p as stand-in for group elements)
    p = 1000003
    pk = [(i * 7919 + 3) % p for i in range(n)]

    def agg(subset: list[int]) -> int:
        return sum(pk[i] for i in subset) % p

    s1 = list(range(t))  # first t validators
    s2 = list(range(n - t, n))  # last t validators
    a1, a2 = agg(s1), agg(s2)
    print(f"toy mod-p aggregate pk for S1 (first t): {a1}")
    print(f"toy mod-p aggregate pk for S2 (last t): {a2}")
    print(f"equal aggregates? {a1 == a2} (typically false — verifier must know which model)")

    print("\n=== VERDICT LINE FOR results.md ===")
    print("INCONCLUSIVE: combinatorial lower bound is for injective subset indexing,")
    print("not a full impossibility proof for sound threshold verification.")


if __name__ == "__main__":
    main()
