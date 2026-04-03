#!/usr/bin/env python3
"""
n=6 {2,3}: full XOR union r=2..4 via --union-rs; baseline coord + full 6-XOR.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6/script.py
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
    / "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6"
    / "script.py"
)

RS = ",".join(str(r) for r in range(2, 5))

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
