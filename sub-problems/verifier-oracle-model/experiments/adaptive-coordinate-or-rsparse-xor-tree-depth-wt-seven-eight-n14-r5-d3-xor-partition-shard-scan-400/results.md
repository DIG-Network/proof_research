# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-partition-shard-scan-400`

**Outcome:** PASS (engineering + completed shard scan; **no** certificate for full-menu `min_d`)

**Parent change:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` gained `--xor-index-range START:END` (requires `--r-single`). Slices the built `r`-sparse XOR partition list before DP.

**Shard schedule (partition of 2002 XOR splits):**

| Range | Splits | Wall DP (approx) | `d=3 feasible` | LRU at end |
|-------|--------|------------------|------------------|------------|
| 0:400 | 400 | ~112 s | False | 8_000_000 |
| 400:800 | 400 | ~120 s | False | 8_000_000 |
| 800:1200 | 400 | ~107 s | False | 8_000_000 |
| 1200:1600 | 400 | ~103 s | False | 8_000_000 |
| 1600:2002 | 402 | ~82 s | False | 8_000_000 |

**Common flags:** `--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 55000000`

**Interpretation**

- Every shard completed without SIGKILL and without `max-exists` PARTIAL — **H1** confirmed on this host.
- **No** shard reported `feasible=True` at `d=3` — **H2** confirmed: this contiguous sharding finds **no** one-block positive witness for full-menu depth-3 feasibility.
- **Full-menu status unchanged:** The prior `5e7`/`8M` run still stands as the best **partial** evidence for the full 2002-split language; this scan does **not** replace it with a `min_d` verdict.

**Repro:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-partition-shard-scan-400/script.py` (~8–9 min total).
