# 2026-04-03 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-eighths-6e7-each-lru-8m

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-eighths-6e7-each-lru-8m`

**Context:** verifier-oracle-model (`n=14`, shells `{7,8}`, **`r=9`**, **`d=3`**, **dual** row to **`r=5`** **6e7** eighth stress)

**Hypothesis tested:** Same **6×10⁷** eighth-shard stress as **`r=5`**; check **arity** asymmetry in **PARTIAL** / **LRU** saturation.

**Outcome:** **PASS** (clean completion). All eight eighths **no** **PARTIAL**; all **`d=3 feasible=False`**. Max misses **2 682 926** (**≪ 8M**). Sum **`dp_sec`** **~145** s; wall **~189** s.

**Key finding:** **`r=9`** matches **`r=5`** — **no** **8M** saturation at **6e7** eighths; slight **DP** sum advantage vs **`r=5`** (**~145** s vs **~152** s).

**Implications:**

- **Eighth** geometry is **arity-stable** under **2×** budget stress.
- **Full-menu** **`d=3`** still open for both arities.

**Analogy pass summary:** Dual codes, same menu cardinality — expect matched memo geometry; timing may differ.

**Space-definition:** none
