#!/usr/bin/env python3
"""
One signer index repeated t times: flawed verifier accepts; sound verifier rejects.

Toy: same Merkle path duplicated t times; K = t * pk[0] (multiplicity sum); sigma = H(m|K).
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


def agg_with_multiplicity(indices: Tuple[int, ...], pks: List[int]) -> int:
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
    if len(set(S)) != len(S):
        return False
    if any(i < 0 or i >= len(pks) for i in S):
        return False
    if len(S) < t or len(paths) != len(S):
        return False
    for i, path in zip(S, paths):
        if not verify_path(C, H_leaf(pks[i]), i, path):
            return False
    if agg_with_multiplicity(S, pks) != K:
        return False
    return sigma == H_sig(m, K)


def verify_flawed_allows_duplicates(
    C: bytes,
    m: bytes,
    pks: List[int],
    t: int,
    S: Tuple[int, ...],
    paths: List[List[bytes]],
    K: int,
    sigma: bytes,
) -> bool:
    """Bug: no distinct-index requirement."""
    if any(i < 0 or i >= len(pks) for i in S):
        return False
    if len(S) < t or len(paths) != len(S):
        return False
    for i, path in zip(S, paths):
        if not verify_path(C, H_leaf(pks[i]), i, path):
            return False
    if agg_with_multiplicity(S, pks) != K:
        return False
    return sigma == H_sig(m, K)


def main() -> None:
    n = 8
    t = n // 2 + 1
    pks = [7000 + 3 * i for i in range(n)]
    levels, C = build_merkle([H_leaf(pk) for pk in pks])
    m = b"proposal-7"

    path0 = merkle_proof(levels, 0)
    S_dup = (0,) * t
    paths_dup = [path0] * t
    K_dup = t * pks[0]
    sigma_dup = H_sig(m, K_dup)

    assert len(set(S_dup)) == 1 < t

    ok_sound = verify_sound(C, m, pks, t, S_dup, paths_dup, K_dup, sigma_dup)
    ok_flawed = verify_flawed_allows_duplicates(
        C, m, pks, t, S_dup, paths_dup, K_dup, sigma_dup
    )

    print(f"n={n} t={t} S={S_dup} unique_signers={len(set(S_dup))}")
    print(f"verify_sound: {ok_sound}")
    print(f"verify_flawed (duplicates OK): {ok_flawed}")

    assert ok_sound is False
    assert ok_flawed is True

    print("RESULT: PASS - repeat one index t times fools verifier without distinctness check")


if __name__ == "__main__":
    main()
