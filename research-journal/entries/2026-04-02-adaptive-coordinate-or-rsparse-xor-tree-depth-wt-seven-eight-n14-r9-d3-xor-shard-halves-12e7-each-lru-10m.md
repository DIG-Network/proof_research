# Journal entry

**Date:** 2026-04-02  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-12e7-each-lru-10m`  
**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `coord + r=9` XOR, `d=3`)

## Hypothesis tested

Doubling per-half `exists_tree` budget from **6×10⁷** to **1.2×10⁸** on the two contiguous XOR index halves (`[0:1001)`, `[1001:2002)`) with **10M** LRU might complete at least one half or yield `d=3 feasible=True` as a witness for the full **2002**-split language.

## Outcome

**INCONCLUSIVE** (wrapper exit **2**). Both halves **PARTIAL** at **1.2×10⁸** cap: shard0 **~1034 s** DP, shard1 **~992 s** DP; LRU saturated **10M** each; no `d=3 feasible=True` witness.

## Key finding

Per-half work scales ~linearly with budget at fixed LRU cap; **12e7** per half is still insufficient to escape PARTIAL on **1001** splits for this `r=9` `d=3` probe—stronger evidence that **half-menu completion** at **10M** LRU requires **>** **1.2×10⁸** invocations per **1001**-wide contiguous shard (not a resolution of full-menu `d=3`).

## Implications

- Parallelizing the two halves preserves total compute but reduces wall-clock if host allows.
- Continue treating **dual-2002** `r=9` `d=3` as **open** at practical budgets; consider alternate sharding or other sub-problem threads.

## Analogy pass summary

Partitioned search with doubled per-partition budget; outcome matches linear scaling—no early witness.

## Space definition

N/A
