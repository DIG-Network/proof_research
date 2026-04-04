#!/usr/bin/env python3
"""
n=5, shell {2,3}: find smallest k such that coord + full r=2 XOR menu + k triple-XOR splits
(subset of the 10 r=3 splits) achieves min_d=2.

Parent: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py
New flag: --union-r3-indices (0-based into lex-ordered C(5,3) triples).

Exit codes (AGENTS.md): 0 = PASS (hypothesis confirmed), 1 = FAIL (falsified).

Hypothesis tested: **minimal** needed `r=3` count with full `r=2` fixed is **≥ 2**.
- If minimal `k` is **1** → hypothesis **falsified** → exit **1**.
- If first witness appears at `k ≥ 2` → **confirmed** → exit **0**.
- If no witness through `k=10` → exit **1** (unexpected / error class).
"""

from __future__ import annotations

import re
import subprocess
import sys
from itertools import combinations
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

N = 5
N_TRIPLES = 10  # C(5,3)
LRU = "4000000"


def run_parent(r3_indices: tuple[int, ...] | None) -> tuple[int, str]:
    cmd = [
        sys.executable,
        str(PARENT),
        "--shells",
        "2,3",
        "--union-rs",
        "2,3",
        "--lru-maxsize",
        LRU,
    ]
    if r3_indices is not None:
        cmd.extend(["--union-r3-indices", ",".join(str(i) for i in r3_indices)])
    proc = subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    out = proc.stdout + proc.stderr
    if proc.returncode != 0:
        return -1, out
    m = re.search(
        r"coord_plus_union_rs=\[[^\]]+\]\s+total_splits=\d+\s+min_d=(\d+)",
        proc.stdout,
    )
    if not m:
        return -1, out
    return int(m.group(1)), out


def main() -> None:
    md0, out0 = run_parent(None)
    print(out0, end="", flush=True)
    if md0 < 0:
        print("FAIL: baseline parent run failed or unparsable", flush=True)
        raise SystemExit(1)
    if md0 != 2:
        print(f"FAIL: expected full r=2..3 union min_d=2, got {md0}", flush=True)
        raise SystemExit(1)

    md_pair_only, out_pair = run_parent(tuple())
    print(out_pair, end="", flush=True)
    if md_pair_only != 3:
        print(
            f"FAIL: expected r=2 only (empty r3 subset) min_d=3, got {md_pair_only}",
            flush=True,
        )
        raise SystemExit(1)

    for k in range(1, N_TRIPLES + 1):
        ncomb = 0
        for idxs in combinations(range(N_TRIPLES), k):
            ncomb += 1
            md, out = run_parent(idxs)
            if md < 0:
                print(out, end="", flush=True)
                print(f"FAIL: parent error at k={k} indices={idxs}", flush=True)
                raise SystemExit(1)
            if md == 2:
                print(out, end="", flush=True)
                print(
                    f"min_k={k} witness r3_indices={list(idxs)} "
                    f"(scanned {ncomb} combos at this k; pair-only baseline min_d=3)",
                    flush=True,
                )
                if k >= 2:
                    print(
                        "PASS (hypothesis confirmed: minimal triple-split count ≥ 2)",
                        flush=True,
                    )
                    raise SystemExit(0)
                print(
                    "FAIL (hypothesis falsified: a single r=3 split suffices with full r=2)",
                    flush=True,
                )
                raise SystemExit(1)
        print(
            f"  k={k}: no witness among C({N_TRIPLES},{k})={ncomb} subsets (all min_d≠2)",
            flush=True,
        )

    print(
        "FAIL: no subset through k=10 reached min_d=2 (unexpected vs full 20-split menu)",
        flush=True,
    )
    raise SystemExit(1)


if __name__ == "__main__":
    main()
