#!/usr/bin/env python3
"""
n=8 {3,4}: full XOR union r=2..7 via --union-rs; baseline coord + full 8-XOR; scan d=1..n.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-three-four-n8/script.py
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
    / "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-three-four-n8"
    / "script.py"
)

RS = ",".join(str(r) for r in range(2, 8))

CMD = [
    sys.executable,
    str(PARENT),
    "--union-rs",
    RS,
    "--lru-maxsize",
    "4000000",
]


def main() -> None:
    print(" ".join(CMD), flush=True)
    raise SystemExit(subprocess.call(CMD, cwd=str(REPO_ROOT)))


if __name__ == "__main__":
    main()
