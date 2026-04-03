#!/usr/bin/env python3
"""
n=14 {7,8}: r=9, d=3-only, XOR menu in four contiguous quarter-shards.

2002 splits partitioned as [0:501), [501:1002), [1002:1503), [1503:2002).

6e7 exists_tree budget per quarter, 8M LRU each (sequential subprocesses).

Aggregate budget 4 * 6e7 = 2.4e8, matching two 12e7 half-shard runs.

Mirror of r=5 quarter-shard wrapper; parent arity is the only change.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py

Exit 0: at least one quarter completed without PARTIAL and reported d=3 feasible=True.
Exit 1: neither witness nor PARTIAL inconsistency (all finished, all infeasible).
Exit 2: at least one quarter PARTIAL and no witness from any quarter.
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

QUARTERS: list[tuple[str, str]] = [
    ("0:501", "q0_0_501"),
    ("501:1002", "q1_501_1002"),
    ("1002:1503", "q2_1002_1503"),
    ("1503:2002", "q3_1503_2002"),
]

BUDGET_PER_QUARTER = 60_000_000
LRU = 8_000_000
R_SINGLE = 9


def parse_d3_feasible(stdout: str) -> bool | None:
    for line in stdout.splitlines():
        m = re.match(r"\s*d=3\s+feasible=(True|False)\s", line)
        if m:
            return m.group(1) == "True"
    return None


def run_quarter(xor_range: str, label: str) -> tuple[int, str]:
    if not PARENT.is_file():
        return 1, f"FAIL: missing parent script {PARENT}"
    cmd = [
        sys.executable,
        str(PARENT),
        "--skip-baseline",
        "--r-single",
        str(R_SINGLE),
        "--d-min",
        "3",
        "--d-max",
        "3",
        "--lru-maxsize",
        str(LRU),
        "--max-exists-calls",
        str(BUDGET_PER_QUARTER),
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

    for xor_range, label in QUARTERS:
        code, out = run_quarter(xor_range, label)
        f3 = parse_d3_feasible(out)
        if code == 2:
            any_partial = True
        elif code != 0:
            any_error = True
        if f3 is True:
            witness = True
            print(f"{label}: d=3 feasible=True (witness)", flush=True)

    if witness:
        print(
            "PASS: at least one XOR quarter witnessed d=3 feasible=True",
            flush=True,
        )
        sys.exit(0)
    if any_error:
        print("FAIL: subprocess error", flush=True)
        sys.exit(1)
    if any_partial:
        print(
            "INCONCLUSIVE: budget PARTIAL on a quarter and no d=3 witness",
            flush=True,
        )
        sys.exit(2)
    print(
        "FAIL: all quarters finished without PARTIAL but no d=3 feasible=True",
        flush=True,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
