#!/usr/bin/env python3
"""
n=5 {2}: full XOR union r=2..3 via --union-rs; baseline coord + full 5-XOR.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py

Exit code: 0 iff union language has min_d == 2 (hypothesis confirmed); 1 otherwise
(falsified or parent failure), per repo experiment convention.
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

RS = ",".join(str(r) for r in range(2, 4))

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
        print("PASS (union min_d=2 hypothesis confirmed)", flush=True)
        raise SystemExit(0)
    print(
        f"FAIL (hypothesis falsified: union min_d={min_d}, expected 2)",
        flush=True,
    )
    raise SystemExit(1)


if __name__ == "__main__":
    main()
