# Experiment entry — 2026-04-02

**Slug:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-12e7-each-lru-8m`  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-12e7-each-lru-8m/`  
**Context:** verifier-oracle-model (`n=14`, shells `{7,8}`, **2002**-split **`r=9`** XOR band)

## Hypothesis tested

Mirror **`r=5`** **12e7/8M** contiguous half-shard run for **`r=9`**: sequential subprocesses on **`[0:1001)`** and **`[1001:2002)`** might yield **`d=3 feasible=True`** on at least one half (witness for full menu by monotonicity).

## Outcome

**INCONCLUSIVE** (wrapper exit **2**). Both halves **PARTIAL** at **1.2×10⁸** `exists_tree` with **8M** LRU; **~974** s + **~912** s DP; **no** witness.

## Key finding

**Aggregate** half-shard wall tracks **`r=5`** (**~1886** s vs **~1853** s DP) even though **`r=9`** is often **faster** than **`r=5`** on **full** 2002 at comparable caps—**half-menu** geometry breaks the simple speed ordering.

## Implications

- **8M** LRU **12e7** contiguous halves are a **practical** mirror pair for **`r∈{5,9}`** without **10M** parallel OOM risk; both stay **PARTIAL**.
- **Dual 2002** **`d=3`** completion still **open**; next steps are **higher budget**, **different sharding**, or **off-host** RAM.

## Analogy pass summary

Paired **A/B** on **`C(14,r)=2002`** with **fixed** shard geometry and **8M** cap—tests whether **`r↔9`** parity pattern changes **half-shard** tractability; **answer:** **not** at this scale (both **PARTIAL**, similar total time).
