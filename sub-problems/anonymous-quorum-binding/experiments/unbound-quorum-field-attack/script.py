#!/usr/bin/env python3
"""
Attack: pi = (K, sigma, k_hat) with k_hat >= t forged while only t-1 keys signed.
Toy SigVerify(K,m,sigma) = (sigma == H(m||K)).
"""

from __future__ import annotations

import hashlib
from typing import List, Tuple


def H_sig(m: bytes, K: int) -> bytes:
    return hashlib.sha256(b"SIG|" + m + b"|" + str(K).encode()).digest()


def agg(indices: Tuple[int, ...], pks: List[int]) -> int:
    return sum(pks[i] for i in indices)


def verify_naive_with_khat(
    m: bytes,
    K: int,
    sigma: bytes,
    k_hat: int,
    t: int,
) -> bool:
    if k_hat < t:
        return False
    return sigma == H_sig(m, K)


def main() -> None:
    print("=== unbound-quorum-field-attack ===\n")
    n = 8
    t = n // 2 + 1
    pks = [7000 + 3 * i for i in range(n)]
    m = b"proposal-1"

    # Only t-1 signers; honest aggregate for that set
    S_under = tuple(range(t - 1))
    K = agg(S_under, pks)
    sigma = H_sig(m, K)
    k_hat_lie = t  # claim full quorum

    ok = verify_naive_with_khat(m, K, sigma, k_hat_lie, t)
    print(f"n={n}, t={t}, actual signers |S|={len(S_under)}")
    print(f"claimed k_hat={k_hat_lie}, SigVerify passes: {sigma == H_sig(m, K)}")
    print(f"naive verify (k_hat + sig) accepts: {ok}")

    assert ok is True, "attack should succeed — k_hat is unbound"

    # Honest majority for contrast
    S_good = tuple(range(t))
    Kg = agg(S_good, pks)
    sg = H_sig(m, Kg)
    ok_good = verify_naive_with_khat(m, Kg, sg, t, t)
    assert ok_good is True

    print("\nVERDICT: PASS -- unauthenticated k_hat does not fix under-quorum (attack works).")

if __name__ == "__main__":
    main()
