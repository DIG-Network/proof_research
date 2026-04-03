# 2026-04-03 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-eighths-3e7-each-lru-8m

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-eighths-3e7-each-lru-8m`

**Context:** verifier-oracle-model (`n=14`, shells `{7,8}`, **`r=9`**, **`d=3`**, **2002** XOR splits — **dual** row to **`r=5`**)

**Hypothesis tested:** Mirror **`r=5`** **eighth-shard** partition: **8 × 3×10⁷** `exists_tree`, **8M** LRU, contiguous **~251**-split blocks — check **dual** **2002** band for **PARTIAL** vs **`d=3`** completion parity with **`r=5`**.

**Outcome:** **PASS** (clean completion). **All eight** eighths finished **without** **PARTIAL**; **all** **`d=3 feasible=False`**. **~185 s** (~**3.08 min**) sequential. **LRU** **not** saturated (max **~2.68×10⁶** misses).

**Key finding:** **`r=9`** **matches** **`r=5`** **eighth** **phenomenology** — **fast** complete **`False`**, **no** **8M** saturation — with **~1%** **extra** wall vs **`r=5`**, **consistent** with **quarter** **`r=9`** vs **`r=5`** ordering.

**Implications:**

- **2002-band parity** extends to **eighth** sharding at **3e7×8**.
- Still **no** **full-menu** **`d=3`** certificate.

**Analogy pass summary:** **Dual** codes share **alphabet size** (**2002**) but not **DP** constants; **matched** sharding makes **comparison** **fair**.

**Space-definition:** none
