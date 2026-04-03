#!/usr/bin/env python3
"""
Scan n=11 then n=12 for 5-vs-6 cross-shell collision of exact
K(S)=(min w, max w, sum w, prod w) with w_i=i+1.

Hypothesis: minimal n>10 with collision is n=11 (PASS if collision at 11).

Exit convention (repo toy experiments):
- PASS: collision at n=11 (minimal n claim confirmed)
- FAIL: no collision at n=11, collision at n=12 (minimal n is 12, not 11)
"""

from __future__ import annotations

import sys
from itertools import combinations
from math import comb, prod


def weights(n: int) -> list[int]:
    return [i + 1 for i in range(n)]


def quad(ws: list[int], subset: tuple[int, ...]) -> tuple[int, int, int, int]:
    vals = [ws[i] for i in subset]
    return (min(vals), max(vals), sum(vals), prod(vals))


def shell_key_set(ws: list[int], r: int) -> set[tuple[int, int, int, int]]:
    n = len(ws)
    return {quad(ws, comb) for comb in combinations(range(n), r)}


def cross_shell_count(n: int) -> tuple[int, int, int, int, tuple | None]:
    """Returns (distinct_5, distinct_6, cross, c5, c6, sample_k_or_none)."""
    ws = weights(n)
    keys5 = shell_key_set(ws, 5)
    keys6 = shell_key_set(ws, 6)
    inter = keys5 & keys6
    sample = min(inter) if inter else None
    return (len(keys5), len(keys6), len(inter), comb(n, 5), comb(n, 6), sample)


def witness_for_k(n: int, k: tuple[int, int, int, int]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    ws = weights(n)
    m5: dict[tuple[int, int, int, int], tuple[int, ...]] = {}
    m6: dict[tuple[int, int, int, int], tuple[int, ...]] = {}
    for comb in combinations(range(n), 5):
        m5.setdefault(quad(ws, comb), comb)
    for comb in combinations(range(n), 6):
        m6.setdefault(quad(ws, comb), comb)
    return (m5[k], m6[k])


def main() -> None:
    n11 = cross_shell_count(11)
    d5_11, d6_11, x11, c5_11, c6_11, s11 = n11
    print(
        f"n=11 distinct_K_5={d5_11} (C={c5_11}) distinct_K_6={d6_11} (C={c6_11}) cross_shell_exact={x11}"
    )
    if x11:
        assert s11 is not None
        a, b = witness_for_k(11, s11)
        print(f"sample_exact_K={s11} five={a} six={b}")
        print("PASS_minimal_n_is_11", flush=True)
        print("PASS", flush=True)
        return

    n12 = cross_shell_count(12)
    d5_12, d6_12, x12, c5_12, c6_12, s12 = n12
    print(
        f"n=12 distinct_K_5={d5_12} (C={c5_12}) distinct_K_6={d6_12} (C={c6_12}) cross_shell_exact={x12}"
    )
    if not x12:
        print("UNEXPECTED_no_collision_at_n12", flush=True)
        sys.exit(2)

    assert s12 is not None
    a12, b12 = witness_for_k(12, s12)
    print(f"sample_exact_K={s12} five={a12} six={b12}")
    print("FAIL_minimal_n_is_12_not_11", flush=True)
    print("FAIL", flush=True)
    sys.exit(1)


if __name__ == "__main__":
    main()
