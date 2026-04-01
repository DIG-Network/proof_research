#!/usr/bin/env python3
"""
n=14 {7,8}: r=8,9,10, d=3-only, --max-exists-calls 5_000_000 (parent script).

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py
Exit 0: all three legs PARTIAL (exit 2 from parent), matching r=5,6 class.
Exit 1: unexpected parent exit or missing parent.
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
    rs = [8, 9, 10]
    exits = [run_r(r) for r in rs]
    print("\nSummary:", ", ".join(f"r={r} exit {e}" for r, e in zip(rs, exits, strict=True)), flush=True)
    bad = [(r, e) for r, e in zip(rs, exits, strict=True) if e != 2]
    if bad:
        print(
            "FAIL: expected PARTIAL (exit 2) for each r in {8,9,10}; "
            f"got {bad}. Adjust hypothesis if this host disagrees.",
            flush=True,
        )
        sys.exit(1)
    print("PASS", flush=True)


if __name__ == "__main__":
    main()
