# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-quarters-6e7-each-lru-8m

**Outcome (journal):** **PASS** — all four quarter-shards finished **`d=3`** without **`max_exists_calls` PARTIAL**; each **`d=3 feasible=False`**. **Wrapper exit code:** **1** (no **`feasible=True`** witness; same convention as **`r=5`** quarter wrapper).

**Aggregate budget:** **4 × 6×10⁷ = 2.4×10⁸** `exists_tree` invocations (**8M** LRU per quarter).

| Quarter | `xor-index-range` | splits | DP sec | `exists_tree_cache_misses_after_d=3` |
|---------|-------------------|--------|--------|----------------------------------------|
| q0 | `0:501` | 501 | ~330.03 | 8_000_000 (saturated) |
| q1 | `501:1002` | 501 | ~308.13 | 8_000_000 |
| q2 | `1002:1503` | 501 | ~333.86 | 8_000_000 |
| q3 | `1503:2002` | 499 | ~323.23 | 8_000_000 |

**Total sequential wall:** ~**1419 s** (~**23.6 min**) for the wrapper (four subprocesses).

**Comparison to `r=5` quarters:** Same completion pattern (**no PARTIAL**, definite **`d=3 False`** on each quarter). **`r=9`** wall time ~**5%** faster than **`r=5`** ~**1491 s** at this shard geometry — consistent with full-menu runs where **`r=9`** is often slightly faster than **`r=5`** in the **2002** band.

**Implication:** **`r=9`** quarter sub-menus mirror **`r=5`** for **finer-shard decisive negatives** at **`d=3`**; still **not** a sound bound on full-menu **`min_d`**.

**Repro:** `python3 -u sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-quarters-6e7-each-lru-8m/script.py`
