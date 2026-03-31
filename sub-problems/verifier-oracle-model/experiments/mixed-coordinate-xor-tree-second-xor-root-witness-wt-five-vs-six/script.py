#!/usr/bin/env python3
"""
Second feasible pair-XOR at root, then 067-style witness for subtrees (coord-first).

Enumerates (i,j) lex on the full 462-set; keeps splits where both sides have
exists_tree(..., d-1). If count >= 2, root = second hit; children built with
witness from mixed-coordinate-xor-tree-witness-wt-five-vs-six logic.
"""

from __future__ import annotations

import hashlib
import json
import sys
from functools import lru_cache

N = 10


def popc(m: int) -> int:
    return m.bit_count()


def pure(S: tuple[int, ...]) -> bool:
    return len({popc(m) for m in S}) <= 1


def split_coord(S: tuple[int, ...], i: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    S0 = tuple(m for m in S if ((m >> i) & 1) == 0)
    S1 = tuple(m for m in S if ((m >> i) & 1) == 1)
    return S0, S1


def split_xor(S: tuple[int, ...], i: int, j: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    S0 = tuple(m for m in S if (((m >> i) ^ (m >> j)) & 1) == 0)
    S1 = tuple(m for m in S if (((m >> i) ^ (m >> j)) & 1) == 1)
    return S0, S1


def recurse_children(
    exists_fn, S0: tuple[int, ...], S1: tuple[int, ...], depth_remaining: int
) -> bool:
    if not S0:
        return exists_fn(S1, depth_remaining - 1)
    if not S1:
        return exists_fn(S0, depth_remaining - 1)
    return exists_fn(S0, depth_remaining - 1) and exists_fn(S1, depth_remaining - 1)


EMPTY_LEAF = ("L", 0, None)


@lru_cache(maxsize=None)
def exists_tree(S: tuple[int, ...], depth_remaining: int) -> bool:
    if pure(S):
        return True
    if depth_remaining <= 0:
        return False
    for i in range(N):
        S0, S1 = split_coord(S, i)
        if recurse_children(exists_tree, S0, S1, depth_remaining):
            return True
    for i in range(N):
        for j in range(i + 1, N):
            S0, S1 = split_xor(S, i, j)
            if recurse_children(exists_tree, S0, S1, depth_remaining):
                return True
    return False


@lru_cache(maxsize=None)
def witness(S: tuple[int, ...], depth_remaining: int) -> tuple:
    if pure(S):
        if not S:
            return EMPTY_LEAF
        return ("L", len(S), popc(S[0]))

    for i in range(N):
        S0, S1 = split_coord(S, i)
        if not S0:
            if exists_tree(S1, depth_remaining - 1):
                return ("C", i, EMPTY_LEAF, witness(S1, depth_remaining - 1))
        elif not S1:
            if exists_tree(S0, depth_remaining - 1):
                return ("C", i, witness(S0, depth_remaining - 1), EMPTY_LEAF)
        else:
            if exists_tree(S0, depth_remaining - 1) and exists_tree(
                S1, depth_remaining - 1
            ):
                return (
                    "C",
                    i,
                    witness(S0, depth_remaining - 1),
                    witness(S1, depth_remaining - 1),
                )

    for i in range(N):
        for j in range(i + 1, N):
            S0, S1 = split_xor(S, i, j)
            if not S0:
                if exists_tree(S1, depth_remaining - 1):
                    return ("X", i, j, EMPTY_LEAF, witness(S1, depth_remaining - 1))
            elif not S1:
                if exists_tree(S0, depth_remaining - 1):
                    return ("X", i, j, witness(S0, depth_remaining - 1), EMPTY_LEAF)
            else:
                if exists_tree(S0, depth_remaining - 1) and exists_tree(
                    S1, depth_remaining - 1
                ):
                    return (
                        "X",
                        i,
                        j,
                        witness(S0, depth_remaining - 1),
                        witness(S1, depth_remaining - 1),
                    )

    raise RuntimeError("witness called but no solvable split — exists_tree mismatch")


def xor_root_feasible(S: tuple[int, ...], d: int, i: int, j: int) -> bool:
    S0, S1 = split_xor(S, i, j)
    if not S0:
        return bool(exists_tree(S1, d - 1))
    if not S1:
        return bool(exists_tree(S0, d - 1))
    return exists_tree(S0, d - 1) and exists_tree(S1, d - 1)


def tuple_depth(t: tuple) -> int:
    if t[0] == "L":
        return 0
    if t[0] == "C":
        _, _, a, b = t
        return 1 + max(tuple_depth(a), tuple_depth(b))
    if t[0] == "X":
        _, _, _, a, b = t
        return 1 + max(tuple_depth(a), tuple_depth(b))
    raise ValueError(t)


def tuple_to_json(t: tuple) -> object:
    if t[0] == "L":
        _, c, w = t
        return {"type": "leaf", "count": c, "wt": w}
    if t[0] == "C":
        _, i, a, b = t
        return {
            "type": "coord",
            "i": i,
            "branch0": tuple_to_json(a) if a != EMPTY_LEAF else {"type": "leaf", "count": 0, "wt": None},
            "branch1": tuple_to_json(b) if b != EMPTY_LEAF else {"type": "leaf", "count": 0, "wt": None},
        }
    if t[0] == "X":
        _, i, j, a, b = t
        return {
            "type": "xor",
            "i": i,
            "j": j,
            "branch0": tuple_to_json(a) if a != EMPTY_LEAF else {"type": "leaf", "count": 0, "wt": None},
            "branch1": tuple_to_json(b) if b != EMPTY_LEAF else {"type": "leaf", "count": 0, "wt": None},
        }
    raise ValueError(t)


def json_leaf_count_sum(node: object) -> int:
    if not isinstance(node, dict):
        raise TypeError(node)
    if node["type"] == "leaf":
        return int(node["count"])
    return json_leaf_count_sum(node["branch0"]) + json_leaf_count_sum(node["branch1"])


def json_sha256(obj: object) -> str:
    b = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(b).hexdigest()


def main() -> None:
    full = tuple(m for m in range(1 << N) if popc(m) in (5, 6))
    assert len(full) == 462

    target_d = 5
    if not exists_tree(full, target_d):
        print(f"NO_TREE_AT_DEPTH_{target_d}")
        print("FAIL")
        sys.exit(1)

    feasible: list[tuple[int, int]] = []
    for i in range(N):
        for j in range(i + 1, N):
            if xor_root_feasible(full, target_d, i, j):
                feasible.append((i, j))

    print(f"feasible_xor_root_count={len(feasible)}")
    print(f"feasible_xor_roots_first_10={feasible[:10]}")

    if len(feasible) < 2:
        print("LESS_THAN_TWO_FEASIBLE_XOR_ROOTS")
        print("FAIL")
        sys.exit(1)

    i2, j2 = feasible[1]
    print(f"second_xor_root_pair=({i2},{j2})")

    S0, S1 = split_xor(full, i2, j2)
    if not S0:
        w = ("X", i2, j2, EMPTY_LEAF, witness(S1, target_d - 1))
    elif not S1:
        w = ("X", i2, j2, witness(S0, target_d - 1), EMPTY_LEAF)
    else:
        w = ("X", i2, j2, witness(S0, target_d - 1), witness(S1, target_d - 1))

    jtree = tuple_to_json(w)
    assert json_leaf_count_sum(jtree) == len(full), "leaf multiset size mismatch"
    d = tuple_depth(w)
    print(f"witness_tree_depth={d}")
    if d > target_d:
        print(f"DEPTH_EXCEEDS_{target_d}")
        print("FAIL")
        sys.exit(1)

    w_default = witness(full, target_d)
    j_default = tuple_to_json(w_default)
    h2 = json_sha256(jtree)
    h0 = json_sha256(j_default)
    print(f"sha256_second_root={h2}")
    print(f"sha256_default_067={h0}")
    if h2 != h0:
        print("DIFFERS_FROM_DEFAULT_WITNESS")
    else:
        print("SAME_AS_DEFAULT_WITNESS_UNEXPECTED")

    print(json.dumps(jtree, indent=2, sort_keys=True))
    print("PASS")


if __name__ == "__main__":
    main()
