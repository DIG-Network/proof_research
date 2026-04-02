#!/usr/bin/env python3
"""
n=14 {7,8}: d=3-only, non-contiguous 1001-wide XOR submenu via odd indices 0,2,...,2000.

Same |menu|=1001 as contiguous half [0:1001) but interleaved in canonical itertools order.
Runs r=5 then r=9 sequentially (C(14,5)=C(14,9)=2002).

12e7 exists_tree budget each, 8M LRU (matches half-shard envelope; single process).

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py
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
    / "adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14"
    / "script.py"
)

TOTAL_XOR = 2002
# Non-contiguous 1001 indices: even starting at 0 → 0,2,4,...,2000
ODD_MENU_INDICES = list(range(0, TOTAL_XOR, 2))
assert len(ODD_MENU_INDICES) == 1001

RUNS: list[tuple[int, str]] = [
    (5, "r5_odd_1001"),
    (9, "r9_odd_1001"),
]


def parse_d3_feasible(stdout: str) -> bool | None:
    for line in stdout.splitlines():
        m = re.match(r"\s*d=3\s+feasible=(True|False)\s", line)
        if m:
            return m.group(1) == "True"
    return None


def run_r(r: int, label: str) -> tuple[int, str]:
    if not PARENT.is_file():
        return 1, f"FAIL: missing parent script {PARENT}"
    indices_arg = ",".join(str(i) for i in ODD_MENU_INDICES)
    cmd = [
        sys.executable,
        str(PARENT),
        "--skip-baseline",
        "--r-single",
        str(r),
        "--d-min",
        "3",
        "--d-max",
        "3",
        "--lru-maxsize",
        "8000000",
        "--max-exists-calls",
        "120000000",
        "--xor-index-indices",
        indices_arg,
    ]
    print(f"\n=== {label} r={r} |indices|={len(ODD_MENU_INDICES)} (odd step) ===", flush=True)
    print("Running:", " ".join(cmd[:14]), "…", flush=True)
    p = subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        text=True,
        capture_output=True,
    )
    out = (p.stdout or "") + (p.stderr or "")
    print(out, end="" if out.endswith("\n") else "\n", flush=True)
    return p.returncode, out


def main() -> None:
    witness = False
    any_partial = False
    any_error = False

    for r, label in RUNS:
        code, out = run_r(r, label)
        f3 = parse_d3_feasible(out)
        if code == 2:
            any_partial = True
        elif code != 0:
            any_error = True
        if f3 is True:
            witness = True
            print(f"{label}: d=3 feasible=True (witness)", flush=True)

    if witness:
        print("PASS: at least one r-run witnessed d=3 feasible=True on odd-index 1001 menu", flush=True)
        sys.exit(0)
    if any_error:
        print("FAIL: subprocess error", flush=True)
        sys.exit(1)
    if any_partial:
        print(
            "INCONCLUSIVE: budget PARTIAL on a run and no d=3 witness from the other",
            flush=True,
        )
        sys.exit(2)
    print(
        "FAIL: both runs finished without PARTIAL but neither reported d=3 feasible=True",
        flush=True,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
