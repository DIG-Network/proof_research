# Results

**Outcome:** INCONCLUSIVE (wrapper exit **2**).

**Setup:** `n=14`, shells `{7,8}`, parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`, `--skip-baseline`, `--r-single 5`, `d=3`-only, contiguous XOR halves `[0:1001)` and `[1001:2002)` (1001 splits each), **`12×10⁷`** `exists_tree` per half, **`8M`** LRU, **sequential** runs.

| Half | xor range | build (s) | DP until PARTIAL (s) | LRU currsize |
|------|-----------|-----------|----------------------|--------------|
| shard_0_1001 | 0:1001 | ~2.69 | ~927.22 | 8M |
| shard_1001_2002 | 1001:2002 | ~2.67 | ~926.15 | 8M |

Both subprocesses exited **2** (PARTIAL). Parsed `d=3 feasible=False` lines are **post-budget** states, not completed decisions. **No** `d=3 feasible=True` witness.

**Total wall (sequential):** ~**1853 s** (~**31 min**).

**Scaling vs 7e7 half-shards:** At **7e7/8M**, each half PARTIAL ~**540 s**. Raising to **12e7** adds ~**387 s** per half (~**72%** more wall for **+71%** budget), **LRU saturated** at **8M** both times—marginal cost per extra `exists_tree` call ~**7.7 µs** at the cap (order-of-magnitude consistent with full-menu **r=5** 10e7→11e7 scaling in digest).

**Comparison:** Full-menu **r=5** at **12e7/10M** was PARTIAL ~**1077 s** (single process, 2002 splits). Each **half** at **12e7/8M** PARTIAL ~**927 s**—still **not** half of full-menu wall, but half-shard **8M** reaches **12e7** without OOM (unlike **12M** LRU on full menu).
