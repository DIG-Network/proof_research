#!/usr/bin/env python3
"""
Reproduce contiguous XOR-menu shard scan for n=14, wt {7,8}, r=5, d=3-only.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py
Uses --xor-index-range to slice the 2002 r=5 XOR bipartitions.

Exit 0: every shard subprocess exited 0 (each shard finished d=3 probe within budget).
Exit 1: missing parent, bad shard, or non-zero child exit.
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

# Partition [0, 2002) into contiguous slices ~400 wide (2002 = 5*400 + 2).
SHARDS = ["0:400", "400:800", "800:1200", "1200:1600", "1600:2002"]


def main() -> None:
    if not PARENT.is_file():
        print(f"FAIL: missing parent script {PARENT}", flush=True)
        sys.exit(1)
    for xr in SHARDS:
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
            "--xor-index-range",
            xr,
            "--lru-maxsize",
            "8000000",
            "--max-exists-calls",
            "55000000",
        ]
        print("Running:", " ".join(cmd), flush=True)
        p = subprocess.run(cmd, cwd=str(REPO_ROOT))
        if p.returncode != 0:
            print(f"FAIL: shard {xr} exit {p.returncode}", flush=True)
            sys.exit(1)
    print("PASS: all XOR partition shards completed (see results.md for interpretation)", flush=True)


if __name__ == "__main__":
    main()
