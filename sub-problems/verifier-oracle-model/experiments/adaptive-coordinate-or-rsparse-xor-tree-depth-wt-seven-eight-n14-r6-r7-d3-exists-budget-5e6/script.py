#!/usr/bin/env python3
"""
n=14 {7,8}: r=6 and r=7, d=3-only, --max-exists-calls 5_000_000 (parent script).

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py
Exit 0: that leg finished (PASS from parent).
Exit 2: PARTIAL (budget exhausted).
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


def run_r(r: int) -> int:
    cmd = [
        sys.executable,
        str(PARENT),
        "--skip-baseline",
        "--r-single",
        str(r),
        "--d-min",
        "3",
        "--d-max",
        "3",
        "--lru-maxsize",
        "0",
        "--max-exists-calls",
        "5000000",
    ]
    print(f"\n=== r={r} ===\nRunning:", " ".join(cmd), flush=True)
    p = subprocess.run(cmd, cwd=str(REPO_ROOT))
    print(f"=== r={r} exit {p.returncode} ===", flush=True)
    return p.returncode


def main() -> None:
    if not PARENT.is_file():
        print(f"FAIL: missing parent script {PARENT}", flush=True)
        sys.exit(1)
    e6 = run_r(6)
    e7 = run_r(7)
    print("\nSummary: r=6 exit", e6, "r=7 exit", e7, flush=True)
    if e6 != 2 or e7 != 0:
        print(
            "FAIL: expected r=6 partial (2) and r=7 complete (0); "
            "adjust hypothesis if this environment disagrees.",
            flush=True,
        )
        sys.exit(1)
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
