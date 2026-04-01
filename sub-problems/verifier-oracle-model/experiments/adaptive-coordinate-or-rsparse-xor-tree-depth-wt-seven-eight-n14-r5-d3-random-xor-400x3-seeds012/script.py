#!/usr/bin/env python3
"""
Three fixed-seed random 400-index XOR submenus for n=14, r=5, d=3-only.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py
Uses --xor-index-indices (non-contiguous) vs contiguous --xor-index-range shards.
"""

from __future__ import annotations

import random
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

TOTAL_XOR_5 = 2002  # C(14,5)
SAMPLE_K = 400
SEEDS = (0, 1, 2)


def main() -> None:
    if not PARENT.is_file():
        print(f"FAIL: missing parent script {PARENT}", flush=True)
        sys.exit(1)
    for seed in SEEDS:
        rng = random.Random(seed)
        idxs = sorted(rng.sample(range(TOTAL_XOR_5), SAMPLE_K))
        indices_arg = ",".join(str(i) for i in idxs)
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
            "--xor-index-indices",
            indices_arg,
            "--lru-maxsize",
            "8000000",
            "--max-exists-calls",
            "55000000",
        ]
        print(f"Running seed={seed} (|indices|={len(idxs)}) …", flush=True)
        print(" ", " ".join(cmd[:12]), "…", flush=True)
        p = subprocess.run(cmd, cwd=str(REPO_ROOT))
        if p.returncode != 0:
            print(f"FAIL: seed {seed} exit {p.returncode}", flush=True)
            sys.exit(1)
    print(
        "PASS: all random-submenu probes completed (see results.md for interpretation)",
        flush=True,
    )


if __name__ == "__main__":
    main()
