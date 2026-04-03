#!/usr/bin/env python3
"""
n=5, mask shell {2,3} (20 masks): XOR union r=2..3 only via --union-rs.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py

Follow-up to shell2-union-r2-r4-min-d: isolate whether weight-3 masks force
min_d=2 without arity-r=4 XOR splits.

Exit 0 iff parent reports union min_d == 2 (PASS: depth-2 without r=4).
Exit 1 if min_d == 1 (FAIL: r=4 part of union was necessary for the bump).
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

RS = "2,3"

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
            "PASS (min_d=2: {2,3} shell + r=2..3 union only — weight-3 alphabet "
            "forces depth 2 without r=4 XOR splits)",
            flush=True,
        )
        raise SystemExit(0)
    print(
        f"FAIL (min_d={min_d}: depth-2 on {{2,3}} shell required r=4 in the union "
        f"or a wider split menu)",
        flush=True,
    )
    raise SystemExit(1)


if __name__ == "__main__":
    main()
