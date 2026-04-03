#!/usr/bin/env python3
"""
n=14 {7,8}: r=5, d=3-only with --max-exists-calls 50_000_000 (5×10^7), --memo-dict, --log-rss.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py

Session-state next action (a): intermediate dict budget with /proc VmRSS logging.

Exit 0: parent finished (PASS line).
Exit 2: parent PARTIAL (budget exhausted mid d=3 probe).
"""

from __future__ import annotations

import os
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
        "-u",
        str(PARENT),
        "--skip-baseline",
        "--r-single",
        "5",
        "--d-min",
        "3",
        "--d-max",
        "3",
        "--memo-dict",
        "--log-rss",
        "--progress-every",
        "2000000",
        "--max-exists-calls",
        "50000000",
    ]
    print("Running:", " ".join(cmd), flush=True)
    env = {**os.environ, "PYTHONUNBUFFERED": "1"}
    p = subprocess.run(cmd, cwd=str(REPO_ROOT), env=env)
    sys.exit(p.returncode)


if __name__ == "__main__":
    main()
