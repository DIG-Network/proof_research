#!/usr/bin/env python3
"""
n=14 {7,8}: r=9, d=3-only, XOR menu sharded into two halves [0:1001) and [1001:2002).

15e7 exists_tree budget per half, 10M LRU each (sequential subprocesses — no parallel workers).

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py

Exit 0: at least one half completed without PARTIAL and reported d=3 feasible=True (witness).
Exit 1: neither half produced such a witness (both infeasible or error).
Exit 2: at least one half PARTIAL (budget) and no d=3 witness from the other.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
PARENT = (
    REPO_ROOT
    / "sub-problems"
    / "verifier-oracle-model"
    / "experiments"
    / "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14"
    / "script.py"
)

HALVES: list[tuple[str, str]] = [
    ("0:1001", "shard_0_1001"),
    ("1001:2002", "shard_1001_2002"),
]


def parse_d3_feasible(stdout: str) -> bool | None:
    for line in stdout.splitlines():
        m = re.match(r"\s*d=3\s+feasible=(True|False)\s", line)
        if m:
            return m.group(1) == "True"
    return None


def run_half(xor_range: str, label: str) -> tuple[int, str]:
    if not PARENT.is_file():
        return 1, f"FAIL: missing parent script {PARENT}"
    cmd = [
        sys.executable,
        str(PARENT),
        "--skip-baseline",
        "--r-single",
        "9",
        "--d-min",
        "3",
        "--d-max",
        "3",
        "--lru-maxsize",
        "10000000",
        "--max-exists-calls",
        "150000000",
        "--xor-index-range",
        xor_range,
    ]
    print(f"\n=== {label} xor-index-range={xor_range} ===", flush=True)
    print("Running:", " ".join(cmd), flush=True)
    p = subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        text=True,
        capture_output=True,
    )
    out = (p.stdout or "") + (p.stderr or "")
    print(out, end="" if out.endswith("\n") else "\n", flush=True)
    return p.returncode, out


def main() -> None:
    witness = False
    any_partial = False
    any_error = False

    for xor_range, label in HALVES:
        code, out = run_half(xor_range, label)
        f3 = parse_d3_feasible(out)
        if code == 2:
            any_partial = True
        elif code != 0:
            any_error = True
        if f3 is True:
            witness = True
            print(f"{label}: d=3 feasible=True (witness)", flush=True)

    if witness:
        print("PASS: at least one XOR half-shard witnessed d=3 feasible=True", flush=True)
        sys.exit(0)
    if any_error:
        print("FAIL: subprocess error", flush=True)
        sys.exit(1)
    if any_partial:
        print(
            "INCONCLUSIVE: budget PARTIAL on a half and no d=3 witness from the other",
            flush=True,
        )
        sys.exit(2)
    print(
        "FAIL: both halves finished without PARTIAL but neither reported d=3 feasible=True",
        flush=True,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
