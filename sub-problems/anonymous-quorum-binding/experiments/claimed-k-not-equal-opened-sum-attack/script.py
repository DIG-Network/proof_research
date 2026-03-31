#!/usr/bin/env python3
"""
Toy: quorum-sized Merkle openings + toy sig on K.

Sound verify: also requires K == sum(pk_i for i in S) (same as r1-baseline).
Flawed verify: drops the sum check; adversary picks K_adv != K_sum with sigma = H(m|K_adv).
"""

from __future__ import annotations

import hashlib
from typing import List, Sequence, Tuple


def H_leaf(pk: int) -> bytes:
    return hashlib.sha256(b"L" + str(pk).encode()).digest()


def H_node(left: bytes, right: bytes) -> bytes:
    return hashlib.sha256(b"I" + left + right).digest()


def build_merkle(leaves: List[bytes]) -> tuple[list[list[bytes]], bytes]:
    if len(leaves) & (len(leaves) - 1) != 0:
        raise ValueError("leaf count must be power of 2")
    levels: List[List[bytes]] = [leaves[:]]
    while len(levels[-1]) > 1:
        row = levels[-1]
        nxt = [H_node(row[i], row[i + 1]) for i in range(0, len(row), 2)]
        levels.append(nxt)
    return levels, levels[-1][0]


def merkle_proof(levels: List[List[bytes]], leaf_index: int) -> List[bytes]:
    path: List[bytes] = []
    idx = leaf_index
    for l in range(len(levels) - 1):
        row = levels[l]
        buddy = idx ^ 1
        path.append(row[buddy])
        idx //= 2
    return path


def verify_path(
    root: bytes, leaf_hash: bytes, leaf_index: int, path: Sequence[bytes]
) -> bool:
    cur = leaf_hash
    idx = leaf_index
    for sib in path:
        if idx % 2 == 0:
            cur = H_node(cur, sib)
        else:
            cur = H_node(sib, cur)
        idx //= 2
    return cur == root


def agg(indices: Tuple[int, ...], pks: List[int]) -> int:
    return sum(pks[i] for i in indices)


def H_sig(m: bytes, K: int) -> bytes:
    return hashlib.sha256(b"SIG|" + m + b"|" + str(K).encode()).digest()


def verify_sound(
    C: bytes,
    m: bytes,
    pks: List[int],
    t: int,
    S: Tuple[int, ...],
    paths: List[List[bytes]],
    K: int,
    sigma: bytes,
) -> bool:
    if len(set(S)) != len(S) or any(i < 0 or i >= len(pks) for i in S):
        return False
    if len(S) < t or len(paths) != len(S):
        return False
    for i, path in zip(S, paths):
        if not verify_path(C, H_leaf(pks[i]), i, path):
            return False
    if agg(S, pks) != K:
        return False
    return sigma == H_sig(m, K)


def verify_flawed_omits_sum_check(
    C: bytes,
    m: bytes,
    pks: List[int],
    t: int,
    S: Tuple[int, ...],
    paths: List[List[bytes]],
    K: int,
    sigma: bytes,
) -> bool:
    """Bug: no K == agg(S) constraint."""
    if len(set(S)) != len(S) or any(i < 0 or i >= len(pks) for i in S):
        return False
    if len(S) < t or len(paths) != len(S):
        return False
    for i, path in zip(S, paths):
        if not verify_path(C, H_leaf(pks[i]), i, path):
            return False
    return sigma == H_sig(m, K)


def main() -> None:
    n = 8
    t = n // 2 + 1
    pks = [3000 + 11 * i for i in range(n)]
    levels, C = build_merkle([H_leaf(pk) for pk in pks])
    m = b"checkpoint"

    S = tuple(range(t))
    paths = [merkle_proof(levels, i) for i in S]
    K_sum = agg(S, pks)
    K_adv = K_sum + 999_999
    sigma = H_sig(m, K_adv)

    ok_sound = verify_sound(C, m, pks, t, S, paths, K_adv, sigma)
    ok_flawed = verify_flawed_omits_sum_check(C, m, pks, t, S, paths, K_adv, sigma)

    print(f"n={n} t={t} |S|={len(S)}")
    print(f"K_sum={K_sum} K_adv={K_adv}")
    print(f"verify_sound: {ok_sound}")
    print(f"verify_flawed (no sum check): {ok_flawed}")

    assert ok_sound is False
    assert ok_flawed is True

    print("RESULT: PASS - claimed K can diverge from opened keys if sum check omitted")


if __name__ == "__main__":
    main()
