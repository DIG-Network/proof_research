#!/usr/bin/env python3
"""
n=6, shell {2,3} (fixed in parent): full r=2 menu + each singleton r=3 split (20 scans).

Tests whether EVERY triple index i yields min_d=2 when adjoined to full r=2 (4M LRU).

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6/script.py

Exit: 0 = PASS (all 20 indices witness min_d=2), 1 = FAIL.
"""

from __future__ import annotations

import re
import subprocess
import sys
from itertools import combinations
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
PARENT = (
    REPO_ROOT
    / "sub-problems"
    / "verifier-oracle-model"
    / "experiments"
    / "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6"
    / "script.py"
)

N = 6
N_TRIPLES = 20
LRU = "4000000"


def triple_for_index(i: int) -> tuple[int, int, int]:
    triples = list(combinations(range(N), 3))
    return triples[i]


def run_parent(r3_index: int | None, *, skip_baseline: bool) -> tuple[int, str]:
    cmd = [
        sys.executable,
        str(PARENT),
        "--union-rs",
        "2,3",
        "--lru-maxsize",
        LRU,
    ]
    if skip_baseline:
        cmd.append("--skip-baseline")
    if r3_index is not None:
        cmd.extend(["--union-r3-indices", str(r3_index)])
    proc = subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    out = proc.stdout + proc.stderr
    if proc.returncode != 0:
        return -1, out
    m = re.search(
        r"coord_plus_union_rs=\[[^\]]+\]\s+total_splits=\d+\s+min_d=(\d+)",
        proc.stdout,
    )
    if not m:
        return -1, out
    return int(m.group(1)), out


def main() -> None:
    md_full, out_full = run_parent(None, skip_baseline=False)
    print(out_full, end="", flush=True)
    if md_full != 2:
        print(f"FAIL: expected full r=2..3 union min_d=2, got {md_full}", flush=True)
        raise SystemExit(1)

    cmd_pair = [
        sys.executable,
        str(PARENT),
        "--union-rs",
        "2",
        "--lru-maxsize",
        LRU,
        "--skip-baseline",
    ]
    proc = subprocess.run(
        cmd_pair,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    out_p2 = proc.stdout + proc.stderr
    print(out_p2, end="", flush=True)
    if proc.returncode != 0:
        print("FAIL: pair-only parent run failed", flush=True)
        raise SystemExit(1)
    m = re.search(
        r"coord_plus_union_rs=\[2\]\s+total_splits=\d+\s+min_d=(\d+)",
        proc.stdout,
    )
    if not m:
        print("FAIL: could not parse pair-only min_d", flush=True)
        raise SystemExit(1)
    md_pair_only = int(m.group(1))
    if md_pair_only != 3:
        print(
            f"FAIL: expected r=2-only min_d=3, got {md_pair_only}",
            flush=True,
        )
        raise SystemExit(1)

    witnesses: list[int] = []
    expected_splits = 35 + 1  # C(6,2) pair splits + one triple split
    for i in range(N_TRIPLES):
        md, out = run_parent(i, skip_baseline=True)
        if md < 0:
            print(out, end="", flush=True)
            print(f"FAIL: parent error at r3_index={i}", flush=True)
            raise SystemExit(1)
        trip = triple_for_index(i)
        print(
            f"r3_index={i} triple={trip} total_splits={expected_splits} min_d={md}",
            flush=True,
        )
        if md == 2:
            witnesses.append(i)

    print(f"witness_indices_min_d2={witnesses}", flush=True)
    if witnesses == list(range(N_TRIPLES)):
        print(
            "PASS (every singleton triple index achieves min_d=2 with full r=2 fixed)",
            flush=True,
        )
        raise SystemExit(0)
    missing = [i for i in range(N_TRIPLES) if i not in witnesses]
    print(
        f"FAIL: expected all indices 0..{N_TRIPLES - 1}; "
        f"missing min_d=2 at indices {missing}",
        flush=True,
    )
    raise SystemExit(1)


if __name__ == "__main__":
    main()
