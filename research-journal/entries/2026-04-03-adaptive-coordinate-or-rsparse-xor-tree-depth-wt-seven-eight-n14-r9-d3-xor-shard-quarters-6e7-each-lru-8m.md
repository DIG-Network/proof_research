# 2026-04-03 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-quarters-6e7-each-lru-8m

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-quarters-6e7-each-lru-8m`

**Context:** verifier-oracle-model (`n=14`, shells `{7,8}`, **`r=9`**, **`d=3`**, **2002** XOR splits)

**Hypothesis tested:** Mirror the completed **`r=5`** quarter-shard protocol: four contiguous blocks **`[0:501), …, [1503:2002)`**, **6×10⁷** `exists_tree` + **8M** LRU per quarter — check whether **`r=9`** shows the same **complete **`d=3`** negative** pattern (vs **PARTIAL** half-shards) or an arity asymmetry.

**Outcome:** **PASS** (clean completion). **All four** quarters finished **without** budget **PARTIAL**; **all** **`d=3 feasible=False`**. **~1419 s** (~**23.6 min**) sequential — slightly faster than **`r=5`** **~1491 s** at the same geometry.

**Key finding:** **`r=9`** **replicates** **`r=5`** **quarter-scale** behavior: **finer contiguous XOR blocking** yields **definite **`d=3`** infeasibility** on **~500-split** sub-menus at **6e7/8M**, where **12e7** half-shards were **PARTIAL**. Arity **does not** break this completion envelope for **`C(14,9)=C(14,5)=2002`**.

**Implications:**

- **Dual 2002-band:** both **`r=5`** and **`r=9`** have **matching** quarter-shard **`d=3`** **False** certificates at this budget class.
- **Full-menu `d=3`** for the **2002** XOR languages remains **open**; next pressure unchanged (**algorithmic** / **larger-RAM dict** / avoid **OOM** full-menu **`10⁸`** dict).

**Analogy pass summary:** Empirical **A/B** on **complement-isomorphic** menu size — **parity** of **completion** vs **PARTIAL** at **quarter** scale.

**Space-definition:** none
