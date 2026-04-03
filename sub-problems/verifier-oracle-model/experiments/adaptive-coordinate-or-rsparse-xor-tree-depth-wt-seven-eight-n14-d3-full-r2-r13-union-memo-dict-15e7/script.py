#!/usr/bin/env python3
"""
n=14 {7,8}: single-shot full XOR menu (r=2..13 union), d=3 only, memo_dict, bounded exists_tree work.

Invokes parent with --full-r2-r13-union-only so the entire budget applies to the combined language.

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
    "3",
    "--d-max",
    "3",
    "--memo-dict",
    "--lru-maxsize",
    "0",
    "--max-exists-calls",
    "150000000",
    "--progress-every",
    "5000000",
    "--log-rss",
]


def main() -> None:
    print(" ".join(CMD), flush=True)
    raise SystemExit(subprocess.call(CMD, cwd=str(REPO_ROOT)))


if __name__ == "__main__":
    main()
