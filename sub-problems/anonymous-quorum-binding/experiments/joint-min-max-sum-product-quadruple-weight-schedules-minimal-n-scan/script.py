#!/usr/bin/env python3
"""
Scan several deterministic public weight schedules for the minimal n>10 such that
exact K(S)=(min w_i, max w_i, sum w_i, prod w_i) has a 5-vs-6 cross-shell collision.

Baseline (097): w_i=i+1 has first collision at n=11.

Exit convention (repo toy experiments):
- PASS: at least one schedule has **no** 5-vs-6 cross-shell collision at n=11 (onset is
  not 11 for that schedule; it may be >=12 later, or absent in a bounded scan)
- FAIL: **every** schedule exhibits a cross-shell collision already at n=11
"""

from __future__ import annotations

import sys
from itertools import combinations
from math import comb, prod
from typing import Callable


def quad(ws: list[int], subset: tuple[int, ...]) -> tuple[int, int, int, int]:
    vals = [ws[i] for i in subset]
    return (min(vals), max(vals), sum(vals), prod(vals))


def cross_shell_collision_at_n(ws: list[int]) -> tuple[bool, tuple[int, int, int, int] | None]:
    n = len(ws)
    keys5: set[tuple[int, int, int, int]] = set()
    keys6: set[tuple[int, int, int, int]] = set()
    for comb5 in combinations(range(n), 5):
        keys5.add(quad(ws, comb5))
    for comb6 in combinations(range(n), 6):
        keys6.add(quad(ws, comb6))
    inter = keys5 & keys6
    if not inter:
        return False, None
    return True, min(inter)


def first_collision_n(
    weights_for_n: Callable[[int], list[int]],
    n_lo: int = 11,
    n_hi: int = 18,
) -> tuple[int | None, tuple[int, int, int, int] | None]:
    """Smallest n in [n_lo, n_hi] with cross-shell collision, or (None, None)."""
    for n in range(n_lo, n_hi + 1):
        ws = weights_for_n(n)
        ok, k = cross_shell_collision_at_n(ws)
        if ok:
            return n, k
    return None, None


def primes_first_n(n: int) -> list[int]:
    if n <= 0:
        return []
    out: list[int] = []
    x = 2
    while len(out) < n:
        is_p = True
        r = int(x**0.5) + 1
        for d in range(2, r):
            if x % d == 0:
                is_p = False
                break
        if is_p:
            out.append(x)
        x += 1
    return out


def fib_first_n(n: int) -> list[int]:
    if n == 0:
        return []
    if n == 1:
        return [1]
    a, b = 1, 1
    out = [a, b]
    while len(out) < n:
        a, b = b, a + b
        out.append(b)
    return out[:n]


SCHEDULES: dict[str, Callable[[int], list[int]]] = {
    "linear_i_plus_1": lambda n: [i + 1 for i in range(n)],
    "reverse_linear_n_minus_i": lambda n: [n - i for i in range(n)],
    "square_(i+1)^2": lambda n: [(i + 1) ** 2 for i in range(n)],
    "pow2_2^i": lambda n: [2**i for i in range(n)],
    "triangular_(i+1)(i+2)/2": lambda n: [(i + 1) * (i + 2) // 2 for i in range(n)],
    "fibonacci": fib_first_n,
    "first_n_primes": primes_first_n,
}


def main() -> None:
    n_lo, n_hi = 11, 18
    any_no_collision_at_11 = False

    for name, fn in SCHEDULES.items():
        ws11 = fn(11)
        coll_11, k11 = cross_shell_collision_at_n(ws11)
        n_first, k_first = first_collision_n(fn, n_lo=n_lo, n_hi=n_hi)
        print(
            f"schedule={name!r} collision_at_n11={coll_11} sample_K_n11={k11} "
            f"first_collision_n_in_[{n_lo},{n_hi}]={n_first} sample_K={k_first}",
            flush=True,
        )
        if not coll_11:
            any_no_collision_at_11 = True

    print(f"scan_range_n=[{n_lo},{n_hi}] schedules={len(SCHEDULES)}", flush=True)
    if any_no_collision_at_11:
        print("PASS_some_schedule_avoids_collision_at_n11", flush=True)
        print("PASS", flush=True)
        return

    print("FAIL_all_schedules_have_cross_shell_collision_at_n11", flush=True)
    print("FAIL", flush=True)
    sys.exit(1)


if __name__ == "__main__":
    main()
