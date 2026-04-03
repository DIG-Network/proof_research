#!/usr/bin/env python3
"""
n=14 {7,8}: r=5, d=3-only with --max-exists-calls 30_000_000 (3×10^7), --memo-dict.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py

Budget note: 3e7 in Python is 30_000_000 (thirty million), not 300_000_000.

Exit 0: parent finished (PASS line).
Exit 2: parent PARTIAL (budget exhausted mid d=3 probe).
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
        "5",
        "--d-min",
        "3",
        "--d-max",
        "3",
        "--memo-dict",
        "--max-exists-calls",
        "30000000",
    ]
    print("Running:", " ".join(cmd), flush=True)
    p = subprocess.run(cmd, cwd=str(REPO_ROOT))
    sys.exit(p.returncode)


if __name__ == "__main__":
    main()
