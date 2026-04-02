# 2026-04-02 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-halves-7e7-each-lru-8m

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-halves-7e7-each-lru-8m`

**Context:** verifier-oracle-model (`n=14`, shells `{7,8}`, **2002** XOR splits for `r=5`, `d=3` existence)

**Hypothesis tested:** Sequential contiguous half-shards `[0:1001)` and `[1001:2002)` with **7×10⁷** `exists_tree` and **8M** LRU each might witness **`d=3 feasible=True`** before budget exhaustion.

**Outcome:** **INCONCLUSIVE** (wrapper exit **2**). Both halves **PARTIAL** at **7e7** (~**540 s** and ~**537 s** DP); no witness.

**Key finding:** **Half-menu** runs at the **same** budget as full-menu **7e7/8M** take **~84%** of full-menu wall per half, not ~50%—contiguous XOR blocking does not cut work proportionally; **`r=5`** half-shard witness search still empty at this scale.

**Implications:**

- Aligns with **`r=9`** half-shard **INCONCLUSIVE** pattern: **sufficient-statistic** style witnesses on **50% contiguous** XOR sub-menus remain elusive at **7e7-class** budgets.
- Next pressure points: raise **per-half** budget toward **12e7** with **8M** LRU (sequential only), or other shard geometries already in journal.

**Analogy pass summary:** Monotonic lifting from sub-menu witness; **no** witness found—**INCONCLUSIVE**, not **FAIL** for global `d=3`.

**Space-definition:** none
