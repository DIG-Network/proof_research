#!/usr/bin/env python3
"""
Microbench: parent n=14 script, r=5, d=3-only, 8e7 exists_tree budget, 10M LRU.

Run A: default lru_cache memo (capped at 10M — heavy eviction).
Run B: --memo-dict (plain dict, no eviction; same invocation budget semantics).

Both should exit 2 (PARTIAL). PASS if B wall time is materially below A
(documenting memo-dict as the algorithmic lever for this DP).
"""

from __future__ import annotations

import re
import subprocess
import sys
import time
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


def run_parent(extra: list[str]) -> tuple[int, float, str]:
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
        "--lru-maxsize",
        "10000000",
        "--max-exists-calls",
        "8000000",
        *extra,
    ]
    t0 = time.perf_counter()
    p = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)
    dt = time.perf_counter() - t0
    out = (p.stdout or "") + (p.stderr or "")
    return p.returncode, dt, out


def main() -> None:
    if not PARENT.is_file():
        print(f"FAIL: missing parent {PARENT}", flush=True)
        sys.exit(1)

    code_a, sec_a, out_a = run_parent([])
    code_b, sec_b, out_b = run_parent(["--memo-dict"])

    print(f"run_A_lru_cache exit={code_a} wall_s={sec_a:.4f}", flush=True)
    print(f"run_B_memo_dict exit={code_b} wall_s={sec_b:.4f}", flush=True)
    print(f"speedup_A_over_B={sec_a/sec_b:.3f}x", flush=True)

    for label, out in ("A", out_a), ("B", out_b):
        if "PARTIAL" not in out:
            print(f"FAIL: run_{label} missing PARTIAL in output", flush=True)
            sys.exit(1)

    m_b = re.search(r"memo_dict_size=(\d+)", out_b)
    if not m_b:
        print("FAIL: could not parse memo_dict_size from run B", flush=True)
        sys.exit(1)
    print(f"memo_dict_size_at_cutoff={m_b.group(1)}", flush=True)

    if code_a != 2 or code_b != 2:
        print(f"FAIL: expected exit 2 both runs, got {code_a} and {code_b}", flush=True)
        sys.exit(1)

    if sec_b >= sec_a * 0.85:
        print(
            "FAIL: memo-dict should beat capped LRU substantially at same invocation budget",
            flush=True,
        )
        sys.exit(1)

    print("PASS", flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
