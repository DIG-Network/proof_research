#!/usr/bin/env python3
"""
Continuation of 105: for pow2, Fibonacci, first-n primes only, test n=62 only
for 5-vs-6 cross-shell collision on exact K(S)=(min w, max w, sum w, product w).

105 showed no collision for these three at n=61 (101+102+103+104 through n=60).

Exit:
- PASS: at least one schedule has a collision at n=62
- FAIL: no schedule collides at n=62
"""

from __future__ import annotations

import sys
import time
from itertools import combinations
from math import prod
from typing import Callable, Tuple


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
    for comb5 in combinations(range(n), 5):
        k = quad(ws, comb5)
        k_to_5.setdefault(k, comb5)
    for comb6 in combinations(range(n), 6):
        k = quad(ws, comb6)
        if k in k_to_5:
            return True, k, k_to_5[k], comb6
    return False, None, None, None


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
    "pow2_2^i": lambda n: [2**i for i in range(n)],
    "fibonacci": fib_first_n,
    "first_n_primes": primes_first_n,
}


def main() -> None:
    n_fixed = 62
    any_collide = False
    t0 = time.perf_counter()

    for name, fn in SCHEDULES.items():
        ws = fn(n_fixed)
        t_sched = time.perf_counter()
        coll, k, i5, i6 = cross_shell_collision_at_n(ws)
        elapsed = time.perf_counter() - t_sched
        if coll:
            any_collide = True
            w5 = [ws[i] for i in i5]  # type: ignore[arg-type]
            w6 = [ws[i] for i in i6]  # type: ignore[arg-type]
            print(
                f"schedule={name!r} n={n_fixed} COLLISION witness_K={k} "
                f"idx5={i5} weights5={w5} idx6={i6} weights6={w6} "
                f"elapsed_s={elapsed:.3f}",
                flush=True,
            )
        else:
            print(
                f"schedule={name!r} n={n_fixed} NO_COLLISION elapsed_s={elapsed:.3f}",
                flush=True,
            )

    wall = time.perf_counter() - t0
    print(f"n={n_fixed} schedules={len(SCHEDULES)} total_wall_s={wall:.3f}", flush=True)
    if any_collide:
        print("PASS_at_least_one_schedule_collides_at_n62", flush=True)
        print("PASS", flush=True)
        return

    print("FAIL_no_schedule_collides_at_n62", flush=True)
    print("FAIL", flush=True)
    sys.exit(1)


if __name__ == "__main__":
    main()
