#!/usr/bin/env python3
"""
Extend the square weight schedule w_i=(i+1)^2 scan for 5-vs-6 cross-shell collisions
of exact K(S)=(min, max, sum, product).

098 certified no collision for n in [11,18] for this schedule. This script scans a
larger band [n_lo, n_hi] and stops at the first n with a collision.

Exit:
- PASS: no collision for any n in [n_lo, n_hi]
- FAIL: minimal n in range with collision (prints witness K)
"""

from __future__ import annotations

import sys
from itertools import combinations
from math import prod
from typing import Tuple


def quad(ws: list[int], subset: tuple[int, ...]) -> tuple[int, int, int, int]:
    vals = [ws[i] for i in subset]
    return (min(vals), max(vals), sum(vals), prod(vals))


def cross_shell_collision_at_n(
    ws: list[int],
) -> Tuple[
    bool,
    tuple[int, int, int, int] | None,
    tuple[int, ...] | None,
    tuple[int, ...] | None,
]:
    n = len(ws)
    k_to_5: dict[tuple[int, int, int, int], tuple[int, ...]] = {}
    k_to_6: dict[tuple[int, int, int, int], tuple[int, ...]] = {}
    for comb5 in combinations(range(n), 5):
        k = quad(ws, comb5)
        k_to_5.setdefault(k, comb5)
    for comb6 in combinations(range(n), 6):
        k = quad(ws, comb6)
        k_to_6.setdefault(k, comb6)
    inter = set(k_to_5) & set(k_to_6)
    if not inter:
        return False, None, None, None
    k = min(inter)
    return True, k, k_to_5[k], k_to_6[k]


def square_weights(n: int) -> list[int]:
    return [(i + 1) ** 2 for i in range(n)]


def main() -> None:
    n_lo, n_hi = 11, 35
    for n in range(n_lo, n_hi + 1):
        ws = square_weights(n)
        coll, k, idx5, idx6 = cross_shell_collision_at_n(ws)
        print(f"n={n} collision={coll} sample_K={k}", flush=True)
        if coll:
            w5 = [ws[i] for i in idx5]  # type: ignore[arg-type]
            w6 = [ws[i] for i in idx6]  # type: ignore[arg-type]
            print(
                f"FAIL_first_collision_n={n} witness_K={k} "
                f"idx5={idx5} weights5={w5} idx6={idx6} weights6={w6}",
                flush=True,
            )
            print("FAIL", flush=True)
            sys.exit(1)

    print(
        f"PASS_no_cross_shell_collision_for_square_weights_n_in_[{n_lo},{n_hi}]",
        flush=True,
    )
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
