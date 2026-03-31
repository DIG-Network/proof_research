#!/usr/bin/env python3
"""
Microbenchmark: random 216-byte keys (same size as n=12 domain bitmask + depth byte),
compare in-memory dict vs dbm.ndbm vs SQLite insert+select rates.

Does not run full exists_tree — only estimates whether disk backends are in the right
ballpark for ~1e6–1e7 memo ops.
"""

from __future__ import annotations

import os
import sqlite3
import tempfile
import time
import dbm
import random


KEY_LEN = 216 // 8  # 27 bytes, same as 1716-bit domain + 1 depth byte
N_OPS = 50_000
RNG = random.Random(0)


def rand_key() -> bytes:
    return bytes(RNG.getrandbits(8) for _ in range(KEY_LEN))


def bench_dict() -> float:
    d: dict[bytes, bytes] = {}
    keys = [rand_key() for _ in range(N_OPS)]
    t0 = time.perf_counter()
    for k in keys:
        d[k] = b"1"
    for k in keys:
        _ = d[k]
    return time.perf_counter() - t0


def bench_ndbm(path: str) -> float:
    if os.path.exists(path):
        os.remove(path)
    for suf in (".db", ".dir", ".pag", ".dat"):
        try:
            os.remove(path + suf)
        except OSError:
            pass
    keys = [rand_key() for _ in range(N_OPS)]
    t0 = time.perf_counter()
    with dbm.open(path, "c") as db:
        for k in keys:
            db[k] = b"1"
        for k in keys:
            _ = db[k]
    return time.perf_counter() - t0


def bench_sqlite(path: str) -> float:
    try:
        os.remove(path)
    except OSError:
        pass
    keys = [rand_key() for _ in range(N_OPS)]
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA synchronous=OFF")
    conn.execute(
        "CREATE TABLE m (k BLOB PRIMARY KEY, v BLOB NOT NULL)"
    )
    conn.execute("BEGIN IMMEDIATE")
    ins = "INSERT OR REPLACE INTO m (k,v) VALUES (?,?)"
    sel = "SELECT v FROM m WHERE k=?"
    t0 = time.perf_counter()
    for k in keys:
        conn.execute(ins, (k, b"1"))
    for k in keys:
        conn.execute(sel, (k,))
    conn.commit()
    conn.close()
    return time.perf_counter() - t0


def main() -> None:
    td = tempfile.mkdtemp(prefix="memo_micro_")
    ndbm_path = os.path.join(td, "m")
    sqlite_path = os.path.join(td, "m.sqlite")

    d_sec = bench_dict()
    n_sec = bench_ndbm(ndbm_path)
    s_sec = bench_sqlite(sqlite_path)

    print(f"ops={N_OPS} key_bytes={KEY_LEN}")
    print(f"dict_sec={d_sec:.4f}")
    print(f"ndbm_sec={n_sec:.4f}  slowdown_vs_dict={n_sec/d_sec:.1f}x")
    print(f"sqlite_sec={s_sec:.4f}  slowdown_vs_dict={s_sec/d_sec:.1f}x")

    # Even ~20x on this *sequential reuse* microbench implies multi-hour full DP:
    # real exists_tree does millions of scattered inserts with cold keys (no batch locality).
    ratio = max(n_sec / d_sec, s_sec / d_sec)
    if ratio > 15:
        print(
            "OUTCOME: FAIL (disk >>15x dict on 27B keys; "
            "not viable as per-state memo for million-op DP)"
        )
    else:
        print("OUTCOME: INCONCLUSIVE (ratio borderline)")


if __name__ == "__main__":
    main()
