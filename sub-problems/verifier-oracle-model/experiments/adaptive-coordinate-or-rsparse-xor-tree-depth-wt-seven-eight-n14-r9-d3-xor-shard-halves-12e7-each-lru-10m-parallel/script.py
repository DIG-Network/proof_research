#!/usr/bin/env python3
"""
n=14 {7,8}: r=9, d=3-only, XOR menu sharded into two halves [0:1001) and [1001:2002).

Same as adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-12e7-each-lru-10m
but runs both halves **in parallel** (two subprocesses) to reduce wall-clock.

1.2e8 exists_tree budget per half; 10M LRU each. Parent: .../adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py

Exit 0: at least one half completed without PARTIAL and reported d=3 feasible=True (witness).
Exit 1: neither half produced such a witness (both infeasible or error).
Exit 2: at least one half PARTIAL (budget) and no witness from the other.
"""

from __future__ import annotations

import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
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

HALVES: list[tuple[str, str]] = [
    ("0:1001", "shard_0_1001"),
    ("1001:2002", "shard_1001_2002"),
]


def parse_d3_feasible(stdout: str) -> bool | None:
    for line in stdout.splitlines():
        m = re.match(r"\s*d=3\s+feasible=(True|False)\s", line)
        if m:
            return m.group(1) == "True"
    return None


def run_half(xor_range: str, label: str) -> tuple[str, int, str, float]:
    t0 = time.perf_counter()
    if not PARENT.is_file():
        dt = time.perf_counter() - t0
        return label, 1, f"FAIL: missing parent script {PARENT}", dt
    cmd = [
        sys.executable,
        str(PARENT),
        "--skip-baseline",
        "--r-single",
        "9",
        "--d-min",
        "3",
        "--d-max",
        "3",
        "--lru-maxsize",
        "10000000",
        "--max-exists-calls",
        "120000000",
        "--xor-index-range",
        xor_range,
    ]
    print(f"\n=== {label} xor-index-range={xor_range} (parallel worker) ===", flush=True)
    print("Running:", " ".join(cmd), flush=True)
    p = subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        text=True,
        capture_output=True,
    )
    out = (p.stdout or "") + (p.stderr or "")
    print(out, end="" if out.endswith("\n") else "\n", flush=True)
    dt = time.perf_counter() - t0
    return label, p.returncode, out, dt


def main() -> None:
    wall0 = time.perf_counter()
    results: dict[str, tuple[int, str, float]] = {}

    with ThreadPoolExecutor(max_workers=2) as pool:
        futs = {
            pool.submit(run_half, xr, lb): (xr, lb) for xr, lb in HALVES
        }
        for fut in as_completed(futs):
            xr, lb = futs[fut]
            label, code, out, dt = fut.result()
            results[label] = (code, out, dt)
            print(f"=== {label} finished returncode={code} elapsed_s={dt:.2f} ===", flush=True)

    wall = time.perf_counter() - wall0
    print(f"\n=== Total wall-clock (parallel): {wall:.2f} s ===", flush=True)

    witness = False
    any_partial = False
    any_error = False
    any_sigkill = False

    for _xr, label in HALVES:
        code, out, _dt = results[label]
        f3 = parse_d3_feasible(out)
        if code == -9:
            any_sigkill = True
        elif code == 2:
            any_partial = True
        elif code != 0:
            any_error = True
        if f3 is True:
            witness = True
            print(f"{label}: d=3 feasible=True (witness)", flush=True)

    if witness:
        print("PASS: at least one XOR half-shard witnessed d=3 feasible=True", flush=True)
        sys.exit(0)
    if any_sigkill:
        print(
            "INCONCLUSIVE: at least one worker exited -9 (SIGKILL); likely host OOM "
            "when running two 10M-LRU processes in parallel — not a d=3 feasibility verdict",
            flush=True,
        )
        sys.exit(2)
    if any_error:
        print("FAIL: subprocess error", flush=True)
        sys.exit(1)
    if any_partial:
        print(
            "INCONCLUSIVE: budget PARTIAL on a half and no d=3 witness from the other",
            flush=True,
        )
        sys.exit(2)
    print(
        "FAIL: both halves finished without PARTIAL but neither reported d=3 feasible=True",
        flush=True,
    )
    sys.exit(1)


if __name__ == "__main__":
    main()
