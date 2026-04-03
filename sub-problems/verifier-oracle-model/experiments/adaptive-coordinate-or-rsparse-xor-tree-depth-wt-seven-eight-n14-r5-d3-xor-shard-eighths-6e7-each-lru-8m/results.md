# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-eighths-6e7-each-lru-8m

**Outcome:** **PASS** (journal convention: clean completion of all eighths with definite **`d=3 feasible=False`** on each; wrapper exits **1** because no **`feasible=True`** witness).

**Setup:** `n=14`, shells `{7,8}`, `--r-single 5`, `--d-min 3 --d-max 3`, `--lru-maxsize 8000000`, `--max-exists-calls 60000000`, eight `--xor-index-range` shards matching the **3e7** eighth partition.

**Findings:**

- All **8** subprocesses finished **without** **PARTIAL** (no exit code **2**).
- Every eighth reported **`d=3 feasible=False`**.
- **`exists_tree_cache_misses_after_d=3`** peaked at **2 835 863** (still **≪ 8 000 000**).
- Sum of per-eighth **`dp_sec`** ≈ **151.77** s; total wall for the wrapper run ≈ **185.3** s.

**Interpretation:** Doubling the per-eighth **`exists_tree`** cap from **3e7** to **6e7** did **not** push the **~251**-split eighth menus into **8M** LRU saturation and did **not** change the **`d=3`** negative — consistent with **depth-3 infeasibility** in this sub-language rather than **budget truncation** at **3e7** for these shards.
