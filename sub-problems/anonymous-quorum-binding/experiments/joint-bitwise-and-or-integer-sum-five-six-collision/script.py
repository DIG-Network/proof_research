#!/usr/bin/env python3
"""
n=10, w_i=i+1. Shells |S|=5 and |S|=6.

K_and(S) = (h_and(S), sum_{i in S} w_i)  exact integers.
K_or(S)  = (h_or(S),  sum w_i).

Report cross-shell collisions on joint keys (same tuple from some 5-set and some 6-set).

Exit 0 = PASS (both joints have >=1 cross-shell collision).
Exit 1 = FAIL (disjoint joint images for K_and or K_or).
"""

from __future__ import annotations

import sys
from itertools import combinations

N = 10


def weights() -> list[int]:
    return [i + 1 for i in range(N)]


def h_and(ws: list[int], subset: tuple[int, ...]) -> int:
    a = ws[subset[0]]
    for i in subset[1:]:
        a &= ws[i]
    return a


def h_or(ws: list[int], subset: tuple[int, ...]) -> int:
    a = 0
    for i in subset:
        a |= ws[i]
    return a


def sum_w(ws: list[int], subset: tuple[int, ...]) -> int:
    return sum(ws[i] for i in subset)


def joint_keys(
    ws: list[int], r: int, h_fn
) -> dict[tuple[int, int], tuple[int, ...]]:
    """Map joint key -> one witness subset (indices)."""
    out: dict[tuple[int, int], tuple[int, ...]] = {}
    for comb in combinations(range(N), r):
        key = (h_fn(ws, comb), sum_w(ws, comb))
        out.setdefault(key, comb)
    return out


def main() -> None:
    ws = weights()
    k5a = joint_keys(ws, 5, h_and)
    k6a = joint_keys(ws, 6, h_and)
    k5o = joint_keys(ws, 5, h_or)
    k6o = joint_keys(ws, 6, h_or)

    inter_and = set(k5a) & set(k6a)
    inter_or = set(k5o) & set(k6o)

    print(f"distinct_joint_K_and_5={len(k5a)} 6={len(k6a)} cross_shell={len(inter_and)}")
    print(f"distinct_joint_K_or_5={len(k5o)} 6={len(k6o)} cross_shell={len(inter_or)}")

    if inter_and:
        k = min(inter_and)
        print(
            f"sample_K_and key={k} five={k5a[k]} six={k6a[k]}",
            flush=True,
        )
    if inter_or:
        k = min(inter_or)
        print(
            f"sample_K_or key={k} five={k5o[k]} six={k6o[k]}",
            flush=True,
        )

    if not inter_and or not inter_or:
        print("FAIL", flush=True)
        sys.exit(1)
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
