#!/usr/bin/env python3
"""
Ideal functionality F_Link (toy integers) + contrast with naive sig-only verify.

F_Link has INTERNAL state: full public key vector and recomputes commitment
binding. Witness w = sorted tuple of indices S.

Aggregation: Agg(S) = sum(pk[i] for i in S).
Commitment: SHA256 chain Merkle root of leaf hashes of pk_i (same as prior experiments).
"""

from __future__ import annotations

import hashlib
from typing import List, Tuple


def merkle_root(leaves: List[bytes]) -> bytes:
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


def commit_pks(pks: List[int]) -> bytes:
    leaves = [hashlib.sha256(str(x).encode()).digest() for x in pks]
    return merkle_root(leaves)


def agg(indices: Tuple[int, ...], pks: List[int]) -> int:
    return sum(pks[i] for i in indices)


def H(m: bytes, K: int) -> bytes:
    return hashlib.sha256(b"SIG|" + m + b"|" + str(K).encode()).digest()


class FLinkIdeal:
    """Ideal: knows full pk table; witness is signer index set S."""

    def __init__(self, pks: List[int], t: int) -> None:
        self.pks = list(pks)
        self.n = len(pks)
        self.t = t
        self.C = commit_pks(self.pks)

    def verify_link(self, C: bytes, K: int, witness_indices: Tuple[int, ...]) -> bool:
        if C != self.C:
            return False
        if len(set(witness_indices)) != len(witness_indices):
            return False
        if not all(0 <= i < self.n for i in witness_indices):
            return False
        if len(witness_indices) < self.t:
            return False
        return agg(tuple(sorted(witness_indices)), self.pks) == K


def verify_naive_sig_only(K: int, sigma: bytes, m: bytes) -> bool:
    return sigma == H(m, K)


def main() -> None:
    print("=== f-link-ideal-spec ===")
    n = 9
    t = n // 2 + 1
    pks = [3000 + 31 * i for i in range(n)]
    ideal = FLinkIdeal(pks, t)
    C = ideal.C
    m = b"epoch-finalize"

    S_good = tuple(range(t))
    K_good = agg(S_good, pks)
    sigma_good = H(m, K_good)

    S_under = tuple(range(t - 1))
    K_under = agg(S_under, pks)
    sigma_under = H(m, K_under)

    assert ideal.verify_link(C, K_good, S_good) is True
    assert ideal.verify_link(C, K_under, S_under) is False
    print("F_Link: honest quorum -> accept:", ideal.verify_link(C, K_good, S_good))
    print("F_Link: under-quorum witness -> reject:", ideal.verify_link(C, K_under, S_under))

    print("Naive sig-only + honest K:", verify_naive_sig_only(K_good, sigma_good, m))
    print("Naive sig-only + under K:", verify_naive_sig_only(K_under, sigma_under, m))

    assert verify_naive_sig_only(K_good, sigma_good, m) is True
    assert verify_naive_sig_only(K_under, sigma_under, m) is True

    # Composition: sound real verifier should require F_Link first
    def sound_verify(Cb: bytes, m2: bytes, K: int, sigma: bytes, w: Tuple[int, ...], I: FLinkIdeal) -> bool:
        if not I.verify_link(Cb, K, w):
            return False
        return verify_naive_sig_only(K, sigma, m2)

    print("Sound compose (under witness):", sound_verify(C, m, K_under, sigma_under, S_under, ideal))
    print("Sound compose (good witness):", sound_verify(C, m, K_good, sigma_good, S_good, ideal))
    assert sound_verify(C, m, K_under, sigma_under, S_under, ideal) is False
    assert sound_verify(C, m, K_good, sigma_good, S_good, ideal) is True

    print("\nVERDICT: PASS — ideal spec consistent; naive sig-only separates from F_Link.")


if __name__ == "__main__":
    main()
