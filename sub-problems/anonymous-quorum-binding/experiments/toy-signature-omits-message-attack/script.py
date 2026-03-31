#!/usr/bin/env python3
"""
Toy: signature that omits message m in verification accepts any m with same (K, sigma).

Contrasts H_sig(m,K) = SHA256(b"SIG|"+m+b"|"+str(K)) (sound) vs H_bad(K) = SHA256(b"BAD|"+str(K)).
"""

from __future__ import annotations

import hashlib


def H_sound(m: bytes, K: int) -> bytes:
    return hashlib.sha256(b"SIG|" + m + b"|" + str(K).encode()).digest()


def H_bad(K: int) -> bytes:
    return hashlib.sha256(b"BAD|" + str(K).encode()).digest()


def verify_sound(m: bytes, K: int, sigma: bytes) -> bool:
    return sigma == H_sound(m, K)


def verify_flawed_ignores_message(m: bytes, K: int, sigma: bytes) -> bool:
    _ = m
    return sigma == H_bad(K)


def main() -> None:
    K = 42_424
    m1 = b"finalize-epoch-9"
    m2 = b"rollback-epoch-9"

    sigma_bad = H_bad(K)
    assert verify_flawed_ignores_message(m1, K, sigma_bad)
    assert verify_flawed_ignores_message(m2, K, sigma_bad)
    assert m1 != m2

    sigma_good = H_sound(m1, K)
    assert verify_sound(m1, K, sigma_good)
    assert verify_sound(m2, K, sigma_good) is False

    print("same sigma_bad verifies two messages under flawed:", m1, m2)
    print("sound verify rejects wrong message for sigma_good:", verify_sound(m2, K, sigma_good))
    print("RESULT: PASS - omit m from sig check => cross-message malleability")


if __name__ == "__main__":
    main()
