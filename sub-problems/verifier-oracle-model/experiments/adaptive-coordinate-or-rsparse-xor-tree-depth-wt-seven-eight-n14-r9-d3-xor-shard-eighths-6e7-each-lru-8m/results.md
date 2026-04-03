# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-eighths-6e7-each-lru-8m

**Outcome:** **PASS** (journal convention: all eighths complete with definite **`d=3 feasible=False`**; wrapper exits **1** — no witness).

**Setup:** Same eighth index ranges as **r=5** run; `--r-single 9`; otherwise identical (**8M** LRU, **6×10⁷** per eighth, sequential).

**Findings:**

- All **8** subprocesses finished **without** **PARTIAL**.
- Every eighth: **`d=3 feasible=False`**.
- Max **`exists_tree_cache_misses_after_d=3`**: **2 682 926** (**≪ 8M**).
- Sum **`dp_sec`** ≈ **144.87** s; total wall ≈ **188.8** s.

**Interpretation:** **r=9** matches **r=5** on this stress point — **2×** per-eighth budget does **not** induce **8M** LRU saturation on **~250**-split eighths; **`d=3`** remains uniformly **False** on the scanned sub-menus.
