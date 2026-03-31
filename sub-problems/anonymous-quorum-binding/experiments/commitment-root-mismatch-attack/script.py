#!/usr/bin/env python3
"""
Toy Merkle + toy signature: show unsoundness when verify does not pin paths to on-chain C.

Two disjoint 8-validator worlds:
- C_honest: keys pk_H[0..7] (benign, unknown to attacker's sig world)
- C_attack: keys pk_A[0..7]; adversary uses majority S_A (|S_A| = 5), aggregate K_A, valid toy sigma

Flawed verifier takes (C_onchain, m, pi) but checks recomputed_root == pi.declared_root
instead of recomputed_root == C_onchain -> accepts while C_onchain != C_attack.
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


def recompute_root_from_one_path(
    leaf_hash: bytes, leaf_index: int, path: Sequence[bytes]
) -> bytes:
    cur = leaf_hash
    idx = leaf_index
    for sib in path:
        if idx % 2 == 0:
            cur = H_node(cur, sib)
        else:
            cur = H_node(sib, cur)
        idx //= 2
    return cur


def verify_sound(C_onchain: bytes, m: bytes, pi: dict) -> bool:
    """Paths must close to the on-chain commitment."""
    pks = pi["pks"]
    S = tuple(pi["S"])
    if len(set(S)) != len(S) or len(S) < 5:
        return False
    paths = pi["paths"]
    if len(paths) != len(S):
        return False
    K = agg(S, pks)
    for i, path in zip(S, paths):
        leaf = H_leaf(pks[i])
        if not verify_path(C_onchain, leaf, i, path):
            return False
    return H_sig(m, K) == pi["sigma"]


def verify_flawed_trusts_declared_root(C_onchain: bytes, m: bytes, pi: dict) -> bool:
    """
    Bug: ignores C_onchain for path verification; uses pi['declared_root'].
    Adversary sets declared_root = root of their own tree.
    """
    _ = C_onchain
    pks = pi["pks"]
    S = tuple(pi["S"])
    declared = pi["declared_root"]
    if len(set(S)) != len(S) or len(S) < 5:
        return False
    paths = pi["paths"]
    if len(paths) != len(S):
        return False
    K = agg(S, pks)
    for i, path in zip(S, paths):
        leaf = H_leaf(pks[i])
        r = recompute_root_from_one_path(leaf, i, path)
        if r != declared:
            return False
    return H_sig(m, K) == pi["sigma"]


def main() -> None:
    m = b"checkpoint-42"
    n = 8

    pk_honest = list(range(1000, 1000 + n))
    leaves_h = [H_leaf(pk) for pk in pk_honest]
    levels_h, C_honest = build_merkle(leaves_h)

    pk_attack = list(range(9000, 9000 + n))
    leaves_a = [H_leaf(pk) for pk in pk_attack]
    levels_a, C_attack = build_merkle(leaves_a)

    S_a = (0, 1, 2, 3, 4)
    paths_a = [merkle_proof(levels_a, i) for i in S_a]
    K_a = agg(S_a, pk_attack)
    sigma_a = H_sig(m, K_a)

    pi = {
        "pks": pk_attack,
        "S": list(S_a),
        "paths": paths_a,
        "sigma": sigma_a,
        "declared_root": C_attack,
    }

    assert C_honest != C_attack

    ok_sound = verify_sound(C_honest, m, pi)
    ok_flawed = verify_flawed_trusts_declared_root(C_honest, m, pi)

    print("C_honest != C_attack:", C_honest != C_attack)
    print("verify_sound(C_honest, ...):", ok_sound)
    print("verify_flawed(C_honest, ...):", ok_flawed)

    assert ok_sound is False, "sound verify must reject cross-world proof"
    assert ok_flawed is True, "flawed verify must accept (attack succeeds)"

    print("RESULT: PASS - commitment-root mismatch attack on flawed interface")


if __name__ == "__main__":
    main()
