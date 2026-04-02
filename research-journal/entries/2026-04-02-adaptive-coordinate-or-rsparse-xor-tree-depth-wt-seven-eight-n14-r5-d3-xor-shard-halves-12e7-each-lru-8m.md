# 2026-04-02 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-halves-12e7-each-lru-8m

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-halves-12e7-each-lru-8m`

**Context:** verifier-oracle-model (`n=14`, shells `{7,8}`, **2002** XOR splits for `r=5`, `d=3` existence)

**Hypothesis tested:** Sequential contiguous half-shards `[0:1001)` and `[1001:2002)` with **12×10⁷** `exists_tree` and **8M** LRU each might witness **`d=3 feasible=True`** before budget exhaustion (extension of **7e7** half-shards, both PARTIAL).

**Outcome:** **INCONCLUSIVE** (wrapper exit **2**). Both halves **PARTIAL** at **12e7** (~**927 s** and ~**926 s** DP); no witness.

**Key finding:** **+71%** budget over **7e7** half-shards adds **~72%** wall per half (**~387 s** extra) with **8M** LRU saturated—still **no** completion; contiguous **50%** XOR menus remain **insufficient** as witness menus at this scale.

**Implications:**

- **8M** LRU **12e7** half-shards are **stable** on this host (**~31 min** total sequential)—useful envelope for further **`r=9`** half-shard trials without **10M** parallel footprint.
- **`r=5`** **`d=3`** for full **2002** remains **open**; next comparative pressure is **`r=9`** under similar **8M** / half-shard geometry.

**Analogy pass summary:** Monotonic lifting from sub-menu witness; **no** witness—**INCONCLUSIVE**, not **FAIL** for global `d=3`.

**Space-definition:** none
