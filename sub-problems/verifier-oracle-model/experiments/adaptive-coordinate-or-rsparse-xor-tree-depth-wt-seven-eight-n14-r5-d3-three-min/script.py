#!/usr/bin/env python3
"""
Reproduce the 2026-04-01 three-minute r=5, d=3-only probe (verifier-oracle-model).

Runs the parent n=14 {7,8} script under `timeout 180` with unbounded LRU.
Exit 0: subprocess completed (check stdout for PASS/FAIL from parent).
Exit 124: wall-clock budget exhausted (INCONCLUSIVE for d=3 decision).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

# …/sub-problems/verifier-oracle-model/experiments/<this-exp>/script.py → repo root is parents[4]
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
        "180",
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
            "INCONCLUSIVE: timeout 180s (exit 124) — no d=3 feasibility line in budget.",
            flush=True,
        )
    sys.exit(p.returncode)


if __name__ == "__main__":
    main()
