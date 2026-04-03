#!/usr/bin/env python3
"""
n=14 {7,8}: r=5, d=3-only, XOR menu in eight contiguous eighth-shards.

2002 splits partitioned as:
  [0:251), [251:502), [502:753), [753:1004),
  [1004:1255), [1255:1506), [1506:1757), [1757:2002).

3e7 exists_tree budget per eighth, 8M LRU each (sequential subprocesses).

Aggregate budget 8 * 3e7 = 2.4e8, matching four quarters or two halves at the same total cap.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py

Exit 0: at least one eighth completed without PARTIAL and reported d=3 feasible=True.
Exit 1: neither witness nor PARTIAL inconsistency (all finished, all infeasible).
Exit 2: at least one eighth PARTIAL and no witness from any eighth.
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

EIGHTHS: list[tuple[str, str]] = [
    ("0:251", "e0_0_251"),
    ("251:502", "e1_251_502"),
    ("502:753", "e2_502_753"),
    ("753:1004", "e3_753_1004"),
    ("1004:1255", "e4_1004_1255"),
    ("1255:1506", "e5_1255_1506"),
    ("1506:1757", "e6_1506_1757"),
    ("1757:2002", "e7_1757_2002"),
]

BUDGET_PER_EIGHTH = 30_000_000
LRU = 8_000_000


def parse_d3_feasible(stdout: str) -> bool | None:
    for line in stdout.splitlines():
        m = re.match(r"\s*d=3\s+feasible=(True|False)\s", line)
        if m:
            return m.group(1) == "True"
    return None


def run_eighth(xor_range: str, label: str) -> tuple[int, str]:
    if not PARENT.is_file():
        return 1, f"FAIL: missing parent script {PARENT}"
    cmd = [
        sys.executable,
        str(PARENT),
        "--skip-baseline",
        "--r-single",
        "5",
        "--d-min",
        "3",
        "--d-max",
        "3",
        "--lru-maxsize",
        str(LRU),
        "--max-exists-calls",
        str(BUDGET_PER_EIGHTH),
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

    for xor_range, label in EIGHTHS:
        code, out = run_eighth(xor_range, label)
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
            "PASS: at least one XOR eighth witnessed d=3 feasible=True",
            flush=True,
        )
        sys.exit(0)
    if any_error:
        print("FAIL: subprocess error", flush=True)
        sys.exit(1)
    if any_partial:
        print(
            "INCONCLUSIVE: budget PARTIAL on an eighth and no d=3 witness",
            flush=True,
        )
        sys.exit(2)
    print(
        "FAIL: all eighths finished without PARTIAL but no d=3 feasible=True",
        flush=True,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
