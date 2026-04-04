#!/usr/bin/env python3
"""
Continuation of 134: for pow2, Fibonacci, first-n primes only, test n=91 only
for 5-vs-6 cross-shell collision on exact K(S)=(min w, max w, sum w, product w).

134 showed no collision for these three at n=90 (101+102+...+134 through n=90).

For n>=91 this script uses a temporary SQLite table for 5-subset keys (RAM-safe);
pure in-memory dict would OOM at ~C(n,5) rows.

Exit:
- PASS: at least one schedule has a collision at n=91
- FAIL: no schedule collides at n=91
"""

from __future__ import annotations

import os
import sqlite3
import struct
import sys
import tempfile
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
    """In-memory map; fine for moderate n."""
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


def cross_shell_collision_at_n_sqlite(
    ws: list[int],
) -> Tuple[
    bool,
    tuple[int, int, int, int] | None,
    tuple[int, ...] | None,
    tuple[int, ...] | None,
]:
    """
    Disk-backed 5-set keys so RAM stays bounded (n=91 has C(91,5) ~ 4.3e7 entries).
    idx5 packed as 5 unsigned shorts (n <= 65535).
    """
    n = len(ws)
    conn: sqlite3.Connection | None = None
    fd, db_path = tempfile.mkstemp(prefix="quad_k5_", suffix=".sqlite")
    os.close(fd)
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA journal_mode=OFF")
        conn.execute("PRAGMA synchronous=OFF")
        conn.execute("PRAGMA temp_store=MEMORY")
        conn.execute(
            """
            CREATE TABLE k5 (
                kmin INTEGER NOT NULL,
                kmax INTEGER NOT NULL,
                ksum INTEGER NOT NULL,
                kprod TEXT NOT NULL,
                idx5 BLOB NOT NULL,
                PRIMARY KEY (kmin, kmax, ksum, kprod)
            ) WITHOUT ROWID
            """
        )
        ins = "INSERT OR IGNORE INTO k5 VALUES (?,?,?,?,?)"
        batch: list[tuple[int, int, int, str, bytes]] = []
        BSZ = 50_000
        for comb5 in combinations(range(n), 5):
            a, b, s, p = quad(ws, comb5)
            batch.append((a, b, s, str(p), struct.pack("5H", *comb5)))
            if len(batch) >= BSZ:
                conn.executemany(ins, batch)
                batch.clear()
        if batch:
            conn.executemany(ins, batch)
        conn.commit()

        for comb6 in combinations(range(n), 6):
            a, b, s, p = quad(ws, comb6)
            row = conn.execute(
                "SELECT idx5 FROM k5 WHERE kmin=? AND kmax=? AND ksum=? AND kprod=?",
                (a, b, s, str(p)),
            ).fetchone()
            if row is not None:
                i5 = struct.unpack("5H", row[0])
                return True, (a, b, s, p), i5, comb6
        return False, None, None, None
    finally:
        if conn is not None:
            conn.close()
        try:
            os.unlink(db_path)
        except OSError:
            pass


def cross_shell_collision_for_schedule(ws: list[int]) -> Tuple[
    bool,
    tuple[int, int, int, int] | None,
    tuple[int, ...] | None,
    tuple[int, ...] | None,
]:
    n = len(ws)
    if n >= 91:
        return cross_shell_collision_at_n_sqlite(ws)
    return cross_shell_collision_at_n(ws)


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
    n_fixed = 91
    any_collide = False
    t0 = time.perf_counter()

    for name, fn in SCHEDULES.items():
        ws = fn(n_fixed)
        t_sched = time.perf_counter()
        coll, k, i5, i6 = cross_shell_collision_for_schedule(ws)
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
        print("PASS_at_least_one_schedule_collides_at_n91", flush=True)
        print("PASS", flush=True)
        return

    print("FAIL_no_schedule_collides_at_n91", flush=True)
    print("FAIL", flush=True)
    sys.exit(1)


if __name__ == "__main__":
    main()
