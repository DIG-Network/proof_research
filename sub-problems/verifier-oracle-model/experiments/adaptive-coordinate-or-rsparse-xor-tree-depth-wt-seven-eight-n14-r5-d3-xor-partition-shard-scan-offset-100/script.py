#!/usr/bin/env python3
"""
Phase-shifted XOR-menu shard scan: n=14, wt {7,8}, r=5, d=3-only.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py
Skips indices [0,100) so slices are disjoint from the 0-origin 400-wide partition
except for possible overlap at boundaries — here we use start=100 to probe
a different contiguous block of the 2002 r=5 XOR bipartitions.

Exit 0: every shard subprocess exited 0.
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

# Five ~400-wide contiguous slices starting at index 100; last ends at 2002.
SHARDS = ["100:500", "500:900", "900:1300", "1300:1700", "1700:2002"]


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
    print(
        "PASS: all phase-shifted XOR partition shards completed "
        "(see results.md for interpretation)",
        flush=True,
    )


if __name__ == "__main__":
    main()
