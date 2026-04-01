#!/usr/bin/env python3
"""
Reproduce shard: n=14 {7,8}, coord + r-sparse XOR for r in {2,3,4}, d=2 only.

Delegates to the parent n=14 experiment script (unbounded LRU, skip baseline).
Exit 0 iff all three runs print PASS (parent exits 0).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PARENT = Path(__file__).resolve().parent.parent / "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14" / "script.py"


def main() -> None:
    if not PARENT.is_file():
        print(f"FAIL: missing parent script {PARENT}", flush=True)
        sys.exit(1)
    for r in (2, 3, 4):
        cmd = [
            sys.executable,
            str(PARENT),
            "--skip-baseline",
            "--r-single",
            str(r),
            "--d-min",
            "2",
            "--d-max",
            "2",
            "--lru-maxsize",
            "0",
        ]
        print(f"\n=== r={r} ===", flush=True)
        rc = subprocess.call(cmd)
        if rc != 0:
            print(f"FAIL: subprocess r={r} exit {rc}", flush=True)
            sys.exit(rc)
    print("\nPASS (all r in {2,3,4}, d=2 infeasible)", flush=True)


if __name__ == "__main__":
    main()
