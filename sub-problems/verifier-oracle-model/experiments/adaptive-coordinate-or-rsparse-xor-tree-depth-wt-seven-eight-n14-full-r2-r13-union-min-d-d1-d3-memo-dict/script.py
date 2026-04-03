#!/usr/bin/env python3
"""
n=14 {7,8}: full XOR union r=2..13, probe min depth d=1..3 with memo_dict + RSS log.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py
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

CMD = [
    sys.executable,
    str(PARENT),
    "--skip-baseline",
    "--full-r2-r13-union-only",
    "--d-min",
    "1",
    "--d-max",
    "3",
    "--memo-dict",
    "--log-rss",
]


def main() -> None:
    print(" ".join(CMD), flush=True)
    raise SystemExit(subprocess.call(CMD, cwd=str(REPO_ROOT)))


if __name__ == "__main__":
    main()
