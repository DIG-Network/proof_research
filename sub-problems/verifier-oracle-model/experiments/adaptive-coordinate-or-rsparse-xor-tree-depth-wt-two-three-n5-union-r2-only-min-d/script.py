#!/usr/bin/env python3
"""
n=5, mask shell {2,3} (20 masks): XOR union r=2 only via --union-rs 2.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py

Isolates whether r=3 XOR splits (10 triple splits) are necessary for min_d=2,
given prior PASS with union r=2..3 (20 splits total).

Exit 0 iff parent reports union min_d == 2 (PASS: pair XOR alone suffices).
Exit 1 otherwise (FAIL: triple XOR splits in the r=2..3 union were needed to reach depth 2).
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
PARENT = (
    REPO_ROOT
    / "sub-problems"
    / "verifier-oracle-model"
    / "experiments"
    / "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5"
    / "script.py"
)

RS = "2"

CMD = [
    sys.executable,
    str(PARENT),
    "--shells",
    "2,3",
    "--union-rs",
    RS,
    "--lru-maxsize",
    "4000000",
]


def main() -> None:
    print(" ".join(CMD), flush=True)
    proc = subprocess.run(
        CMD,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    sys.stdout.write(proc.stdout)
    sys.stderr.write(proc.stderr)
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)
    m = re.search(
        r"coord_plus_union_rs=\[[^\]]+\]\s+total_splits=\d+\s+min_d=(\d+)",
        proc.stdout,
    )
    if not m:
        print("FAIL: could not parse union min_d from parent output", flush=True)
        raise SystemExit(1)
    min_d = int(m.group(1))
    if min_d == 2:
        print(
            "PASS (min_d=2: {2,3} shell + r=2 union only — pair XOR splits suffice; "
            "r=3 XOR splits not needed for depth-2 certificate here)",
            flush=True,
        )
        raise SystemExit(0)
    print(
        f"FAIL (min_d={min_d}: pair-XOR-only union does not match min_d=2 from "
        f"r=2..3 union — arity-r=3 XOR splits are load-bearing for depth 2 here)",
        flush=True,
    )
    raise SystemExit(1)


if __name__ == "__main__":
    main()
