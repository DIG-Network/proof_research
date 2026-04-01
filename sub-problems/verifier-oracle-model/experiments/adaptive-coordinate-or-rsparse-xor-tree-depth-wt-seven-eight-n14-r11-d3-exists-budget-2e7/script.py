#!/usr/bin/env python3
"""
n=14 {7,8}: r=11, d=3-only, --max-exists-calls 20_000_000 (4× prior 5e6 shard).

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py
Exit 0: d=3 probe completed without budget exhaustion (expect feasible=True).
Exit 2: PARTIAL (still hits max_exists_calls).
"""

from __future__ import annotations

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


def main() -> None:
    if not PARENT.is_file():
        print(f"FAIL: missing parent script {PARENT}", flush=True)
        sys.exit(1)
    cmd = [
        sys.executable,
        str(PARENT),
        "--skip-baseline",
        "--r-single",
        "11",
        "--d-min",
        "3",
        "--d-max",
        "3",
        "--lru-maxsize",
        "0",
        "--max-exists-calls",
        "20000000",
    ]
    print("Running:", " ".join(cmd), flush=True)
    p = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)
    out = (p.stdout or "") + (p.stderr or "")
    print(out, end="" if out.endswith("\n") else out, flush=True)
    if p.returncode == 2:
        print("FAIL: PARTIAL (exit 2) — budget still exhausted at 2e7", flush=True)
        sys.exit(1)
    if p.returncode != 0:
        print(f"FAIL: unexpected parent exit {p.returncode}", flush=True)
        sys.exit(1)
    # Parent prints "  d=3 feasible=..." inside the d loop
    feasible_true = False
    feasible_false = False
    for line in out.splitlines():
        if "d=3 feasible=True" in line:
            feasible_true = True
        if "d=3 feasible=False" in line:
            feasible_false = True
    if feasible_true:
        print("PASS: d=3 feasible under 2e7 budget (hypothesis confirmed)", flush=True)
        return
    if feasible_false:
        print(
            "FAIL: probe finished but d=3 infeasible — not a budget wall; min_d>3 for r=11",
            flush=True,
        )
        sys.exit(1)
    print("FAIL: could not parse d=3 feasibility from parent output", flush=True)
    sys.exit(1)


if __name__ == "__main__":
    main()
