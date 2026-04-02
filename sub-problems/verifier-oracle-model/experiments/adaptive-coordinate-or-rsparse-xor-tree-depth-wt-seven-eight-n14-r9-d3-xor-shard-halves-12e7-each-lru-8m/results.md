# Results

**Outcome:** INCONCLUSIVE (wrapper exit **2**).

**Setup:** `n=14`, shells `{7,8}`, parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`, `--skip-baseline`, `--r-single 9`, `d=3`-only, contiguous XOR halves `[0:1001)` and `[1001:2002)` (1001 splits each), **`12×10⁷`** `exists_tree` per half, **`8M`** LRU, **sequential** runs.

| Half | xor range | build (s) | DP until PARTIAL (s) | LRU currsize |
|------|-----------|-----------|----------------------|--------------|
| shard_0_1001 | 0:1001 | ~4.12 | ~973.97 | 8M |
| shard_1001_2002 | 1001:2002 | ~4.06 | ~911.72 | 8M |

Both subprocesses exited **2** (PARTIAL). Parsed `d=3 feasible=False` lines are **post-budget** states, not completed decisions. **No** `d=3 feasible=True` witness.

**Total wall (sequential):** ~**1957 s** (~**32.6 min**).

**Paired comparison (`r=9` vs `r=5` at **12e7/8M** half-shards):** **`r=5`** halves **~927 + ~926** s DP (**~1853** s); **`r=9`** **~974 + ~912** s (**~1886** s)—**within ~2%** total DP time despite **`r=9`** often being **faster** than **`r=5`** on **full** 2002-menu runs at comparable caps. First half **`r=9`** **slower** (~**47** s more than **`r=5`** shard0); second half **`r=9`** **faster** (~**14** s less than **`r=5`** shard1)—suggests **split-dependent** DP geometry, not a uniform speedup.

**vs `r=9` 12e7/10M half-shards:** Prior sequential **10M** LRU run **~1034 + ~992** s; **8M** halves are **~60 + ~80** s **faster** per half respectively at same visit cap—**LRU size** still dominates marginal cost at the cap.

**Conclusion:** **8M** LRU **12e7** contiguous half-shards do **not** yield a **`d=3`** witness for **`r=9`**; dual **2002** band remains **open** for a **completed** full-menu **`d=3`** bit.
