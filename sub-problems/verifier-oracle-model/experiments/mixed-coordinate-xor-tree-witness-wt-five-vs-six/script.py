#!/usr/bin/env python3
"""
One witness tree for mixed coordinate + pair-XOR (same order as entry 066).

Phase 1: memoized exists_tree(S, d) — identical logic to adaptive-coordinate-or-pair-xor script.
Phase 2: witness(S, d) only descends along splits that exists_tree certifies solvable,
so we never explore futile subtrees (naive build_witness times out on the full 462-set).

Tuple shapes:
  ("L", count, wt)   wt None iff count==0 (empty leaf)
  ("C", i, t0, t1)   coord i
  ("X", i, j, t0, t1) pair xor
"""

from __future__ import annotations

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


def main() -> None:
    full = tuple(m for m in range(1 << N) if popc(m) in (5, 6))
    assert len(full) == 462

    target_d = 5
    if not exists_tree(full, target_d):
        print(f"NO_TREE_AT_DEPTH_{target_d}")
        print("FAIL")
        sys.exit(1)

    w = witness(full, target_d)
    j = tuple_to_json(w)
    assert json_leaf_count_sum(j) == len(full), "leaf multiset size mismatch"
    print(f"witness_tree_depth={tuple_depth(w)}")
    print(json.dumps(j, indent=2, sort_keys=True))
    print("PASS")


if __name__ == "__main__":
    main()
