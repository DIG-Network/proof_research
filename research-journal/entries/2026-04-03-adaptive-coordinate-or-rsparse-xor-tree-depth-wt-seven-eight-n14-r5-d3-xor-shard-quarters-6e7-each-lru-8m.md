# 2026-04-03 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-quarters-6e7-each-lru-8m

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-quarters-6e7-each-lru-8m`

**Context:** verifier-oracle-model (`n=14`, shells `{7,8}`, **`r=5`**, **`d=3`**, **2002** XOR splits)

**Hypothesis tested:** Four contiguous quarter-shards (**~501** splits each, last **499**) with **6×10⁷** `exists_tree` and **8M** LRU per quarter (**2.4×10⁸** total budget, matching two **12×10⁷** half-shard runs) might either witness **`d=3 feasible=True`** or at least clarify whether **finer sharding** escapes **PARTIAL** vs **12e7** halves.

**Outcome:** **PASS** (clean completion). **All four** quarters finished **without** budget **PARTIAL**; **all** **`d=3 feasible=False`**. **~1491 s** (~**24.9 min**) sequential. **LRU** **8M** **saturated** each quarter.

**Key finding:** **Quarter** menus **complete** at **`d=3`** where **half** menus at **12e7** **did not** — **finer contiguous XOR blocking** turns **budget-truncated** search into **definite infeasibility** for **`d=3`** on these sub-menus. Still **no** implication for **full** **2002** **`min_d`** (sub-menu negatives are **not** sound global lower bounds).

**Implications:**

- **Useful envelope:** **~500-split** **`r=5`** shards + **6e7/8M** give **decisive **`d=3`** **False** without **PARTIAL**.
- **Full-menu `d=3`** remains **open**; next pressure remains **algorithmic** / **larger RAM dict** / **other `r`** — not **quarter witness** for **`r=5`**.

**Analogy pass summary:** Domain decomposition changes **reachable** states under **fixed** memo cap; **quarters** **resolve** where **halves** **stall**.

**Space-definition:** none
