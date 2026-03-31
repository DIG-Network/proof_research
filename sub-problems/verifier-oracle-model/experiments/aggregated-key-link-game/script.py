#!/usr/bin/env python3
"""
Toy model for experiment aggregated-key-link-game.

We model public keys as integers pk_i and a 'multisignature' that is simply
    sigma = H(m || K)   (deterministic, not secure — only for interface demo)
Verification checks sigma == H(m || K).

Aggregation: K = sum(pk_i for i in S)  (integer sum — stand-in for group law).

Commitment C = Merkle-like binding digest of sorted pk list (verifier never sees pk_i).

Attack: adversary knows all pk_i. Pick S_under of size t-1, set K = agg(S_under),
sigma = H(m||K). Naive Verify(C, m, (K,sigma)) that only checks sigma succeeds.

If Verify also required Link(C,K): "K is sum of >=t distinct committed keys",
the under-quorum attempt would need to pass Link — which is exactly the hard part.
"""

from __future__ import annotations

import hashlib
from typing import List


def H(m: bytes, K: int) -> bytes:
    return hashlib.sha256(b"SIG|" + m + b"|" + str(K).encode()).digest()


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


def commit_validator_set(pks: List[int]) -> bytes:
    leaves = [hashlib.sha256(str(pk).encode()).digest() for pk in pks]
    return merkle_root(leaves)


def agg(subset_indices: List[int], pks: List[int]) -> int:
    return sum(pks[i] for i in subset_indices)


def verify_naive(C: bytes, m: bytes, pi: tuple[int, bytes], pks: List[int] | None) -> bool:
    K, sigma = pi
    return sigma == H(m, K)


def verify_with_link(
    C: bytes,
    m: bytes,
    pi: tuple[int, bytes],
    pks: List[int],
    t: int,
) -> bool:
    """Oracle-only link: full key list (NOT allowed in target model — reference checker)."""
    K, sigma = pi
    if sigma != H(m, K):
        return False
    n = len(pks)
    # brute: exists subset of size >= t with sum == K
    from itertools import combinations

    for r in range(t, n + 1):
        for comb in combinations(range(n), r):
            if agg(list(comb), pks) == K:
                return True
    return False


def main() -> None:
    print("=== aggregated-key-link-game ===")
    n = 7
    t = n // 2 + 1  # 4
    pks = [1000 + i * 17 for i in range(n)]
    C = commit_validator_set(pks)
    m = b"checkpoint-42"

    # Under-quorum: only t-1 signers "intended"
    S_under = list(range(t - 1))
    K_bad = agg(S_under, pks)
    sigma_bad = H(m, K_bad)
    pi_bad = (K_bad, sigma_bad)

    ok_naive = verify_naive(C, m, pi_bad, None)
    ok_link = verify_with_link(C, m, pi_bad, pks, t)

    print(f"n={n}, t={t}, under-quorum |S|={len(S_under)}")
    print(f"C = {C.hex()[:24]}...")
    print(f"verify_naive (sig equation only): {ok_naive}")
    print(f"verify_with_link (exponential oracle): {ok_link}")

    # Honest quorum proof for contrast
    S_good = list(range(t))
    K_good = agg(S_good, pks)
    pi_good = (K_good, H(m, K_good))
    print(f"honest |S|={len(S_good)} naive ok: {verify_naive(C, m, pi_good, None)}")
    print(f"honest link ok: {verify_with_link(C, m, pi_good, pks, t)}")

    assert ok_naive is True, "attack should succeed without link"
    assert ok_link is False, "oracle link should reject under-quorum"
    print("\nVERDICT: PASS — under-quorum forges naive interface; link predicate separates.")

if __name__ == "__main__":
    main()
