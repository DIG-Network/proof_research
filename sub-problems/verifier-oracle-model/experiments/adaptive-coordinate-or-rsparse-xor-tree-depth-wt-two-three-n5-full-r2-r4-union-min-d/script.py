#!/usr/bin/env python3
"""
n=5, masks of weight in {2,3} (20 masks): full XOR union r=2..4 via --union-rs.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py

Hypothesis: min_d for this union language remains 1 (same as weight-2-only shell
with r=2..3 union); the n>=6 "min_d=2 full union" ladder does not extend to n=5
even after enlarging the shell.

Exit 0 iff parent reports union min_d == 1 (PASS); 1 otherwise.
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

RS = ",".join(str(r) for r in range(2, 5))

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
    if min_d == 1:
        print(
            "PASS (min_d=1: enlarged shell + r=2..4 union still depth-1 certificate)",
            flush=True,
        )
        raise SystemExit(0)
    print(
        f"FAIL (hypothesis falsified: union min_d={min_d}, expected 1)",
        flush=True,
    )
    raise SystemExit(1)


if __name__ == "__main__":
    main()
