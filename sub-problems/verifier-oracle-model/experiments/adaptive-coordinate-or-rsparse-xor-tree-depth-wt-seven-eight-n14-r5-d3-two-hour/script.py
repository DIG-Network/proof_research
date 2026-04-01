#!/usr/bin/env python3
"""
Reproduce the n=14 {7,8} r=5, d=3-only probe with timeout 7200s (2 hours).

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py
Exit 0: subprocess completed (stdout shows PASS from parent if baseline not skipped).
Exit 124: wall-clock budget exhausted (INCONCLUSIVE for d=3 decision).
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
        "timeout",
        "7200",
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
        "0",
    ]
    print("Running:", " ".join(cmd), flush=True)
    p = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if p.returncode == 124:
        print(
            "INCONCLUSIVE: timeout 7200s (exit 124) — no d=3 feasibility line in budget.",
            flush=True,
        )
    sys.exit(p.returncode)


if __name__ == "__main__":
    main()
