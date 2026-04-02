# 2026-04-02 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-6e7-each-lru-10m

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-6e7-each-lru-10m`

**Context:** verifier-oracle-model (`n=14`, shells `{7,8}`, dual **2002** XOR band for `r=5` and `r=9`, `d=3` existence)

**Hypothesis tested:** Contiguous half-shards `[0:1001)` and `[1001:2002)` of the `r=9` XOR menu, **6×10⁷** `exists_tree` each and **10M** LRU, might yield a **`d=3 feasible=True`** witness before budget exhaustion.

**Outcome:** **INCONCLUSIVE** (wrapper exit **2**). Both halves **PARTIAL** at **6e7** (~**509 s** and ~**479 s** DP); no witness.

**Key finding:** **50% contiguous** sub-menus at **half** the per-run budget of prior **12e7** full-menu attempts do not shortcut the **`d=3`** question; second half reached budget **~30 s** faster than the first (asymmetric hardness along index order or process effects).

**Implications:**

- To match full-menu **12e7** cap **per half**, expect **~2× ~965 s** wall if sequential (~**32 min**), or run parallel processes.
- Non-contiguous / random shards already explored elsewhere; contiguous **two-half** split at **6e7** adds no positive witness.

**Analogy pass summary:** Monotonic “superset of splits” lifting; sought sufficient-statistic-style witness on a **half** menu — **not found** at this budget.

**Space-definition:** none
