# 2026-04-03 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-eighths-6e7-each-lru-8m

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-eighths-6e7-each-lru-8m`

**Context:** verifier-oracle-model (`n=14`, shells `{7,8}`, **`r=5`**, **`d=3`**, **2002** XOR eighths — **2×** per-eighth **`exists_tree`** vs **3e7** baseline)

**Hypothesis tested:** Doubling per-eighth budget to **6×10⁷** (aggregate **4.8×10⁸**) while keeping **~251**-split eighth geometry and **8M** LRU would reveal **LRU saturation** or **PARTIAL** if the **3e7** runs were truncation-limited.

**Outcome:** **PASS** (clean completion). All eight eighths finished **without** **PARTIAL**; all **`d=3 feasible=False`**. Max **`exists_tree_cache_misses_after_d=3`** **2 835 863** (**≪ 8M**). Sum **`dp_sec`** **~152** s; wall **~185** s.

**Key finding:** **6e7** per eighth does **not** engage the extra budget in practice (depth-3 decision finishes earlier), and **does not** approach **8M** LRU misses — **3e7** eighth runs were **not** memo-starved.

**Implications:**

- Further eighth **budget** scaling is unlikely to change **`d=3`** outcomes on this geometry.
- Full-menu **`d=3`** remains the open frontier (**memo-dict** / RAM / DP structure).

**Analogy pass summary:** Cache/working-set vs search budget — doubling cap is slack when the search terminates before cap.

**Space-definition:** none
