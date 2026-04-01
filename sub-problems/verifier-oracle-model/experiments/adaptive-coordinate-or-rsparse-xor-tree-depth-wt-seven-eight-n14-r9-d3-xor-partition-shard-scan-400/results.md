# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-partition-shard-scan-400`

**Outcome:** PASS (engineering + completed shard scan; **no** certificate for full-menu `min_d`)

**Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with `--xor-index-range` (same 2002-split menu as `r=5`, since `C(14,9)=C(14,5)`).

**Shard schedule (partition of 2002 XOR splits, `r=9`):**

| Range | Splits | Wall DP (approx) | `d=3 feasible` | LRU misses after `d=3` |
|-------|--------|------------------|----------------|-------------------------|
| 0:400 | 400 | ~110.7 s | False | 8_000_000 |
| 400:800 | 400 | ~124.0 s | False | 8_000_000 |
| 800:1200 | 400 | ~123.6 s | False | 8_000_000 |
| 1200:1600 | 400 | ~132.2 s | False | 8_000_000 |
| 1600:2002 | 402 | ~151.6 s | False | 8_000_000 |

**Common flags:** `--skip-baseline --r-single 9 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 55000000`

**Total wall time (wrapper):** ~746 s (~12.4 min).

**Interpretation**

- **H1:** Every shard completed without SIGKILL and without `max-exists` PARTIAL.
- **H2:** **No** shard reported `feasible=True` at `d=3` — same pattern as the `r=5` contiguous shard scan: **no** one-block positive witness from this sharding strategy.
- **Comparison with `r=5` shards:** Per-shard DP times are in the same ballpark (~80–150 s per shard); `r=9` final shard ~152 s vs `r=5` ~82 s for `1600:2002` (not identical parity workload across index order).
- **Full-menu `r=9` `d=3`:** Still **not** decided: negatives on shards are **not** logically conclusive for the full 2002-split language; the prior full-menu **5e7**/**8M** run remains **PARTIAL** at the root.

**Repro:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-partition-shard-scan-400/script.py`
