#!/usr/bin/env python3
"""
R1 baseline: linear-size pi = Merkle path per signer in S + aggregate K + toy signature.

n=8, t=5. Power-of-2 leaves for simple binary Merkle proofs.
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


def verify_r1(
    C: bytes,
    m: bytes,
    pks: List[int],
    t: int,
    levels: List[List[bytes]],
    S: Tuple[int, ...],
    paths: List[List[bytes]],
    K: int,
    sigma: bytes,
) -> bool:
    if len(set(S)) != len(S):
        return False
    if any(i < 0 or i >= len(pks) for i in S):
        return False
    if len(S) < t:
        return False
    if len(paths) != len(S):
        return False
    for i, path in zip(S, paths):
        lh = H_leaf(pks[i])
        if not verify_path(C, lh, i, path):
            return False
    if agg(S, pks) != K:
        return False
    return sigma == H_sig(m, K)


def main() -> None:
    print("=== r1-baseline-linear-proof-sound ===\n")
    n = 8
    t = n // 2 + 1
    pks = [5000 + 17 * i for i in range(n)]
    levels, C = build_merkle([H_leaf(pk) for pk in pks])
    m = b"vote-yes"

    S_good = tuple(range(t))
    paths_good = [merkle_proof(levels, i) for i in S_good]
    K_good = agg(S_good, pks)
    sigma_good = H_sig(m, K_good)

    S_under = tuple(range(t - 1))
    paths_under = [merkle_proof(levels, i) for i in S_under]
    K_under = agg(S_under, pks)
    sigma_under = H_sig(m, K_under)

    ok_honest = verify_r1(C, m, pks, t, levels, S_good, paths_good, K_good, sigma_good)
    ok_under = verify_r1(C, m, pks, t, levels, S_under, paths_under, K_under, sigma_under)

    print(f"n={n}, t={t}, path_len_each={len(paths_good[0])} hashes")
    print(f"approx pi field count: |S| paths + K + sigma ~ {len(S_good)} * {len(paths_good[0])} + O(1) hashes")
    print(f"honest verify: {ok_honest}")
    print(f"under-quorum verify: {ok_under}")

    assert ok_honest is True
    assert ok_under is False

    # Wrong K with valid paths still fails
    ok_bad_k = verify_r1(C, m, pks, t, levels, S_good, paths_good, K_good + 1, H_sig(m, K_good + 1))
    assert ok_bad_k is False

    print("\nVERDICT: PASS -- R1 linear Merkle-per-signer + Link-style agg check sound in toy model.")

if __name__ == "__main__":
    main()
