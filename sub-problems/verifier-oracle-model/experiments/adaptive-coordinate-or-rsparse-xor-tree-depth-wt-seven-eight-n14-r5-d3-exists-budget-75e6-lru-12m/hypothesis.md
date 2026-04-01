# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, `coord + r=5`, `d=3`-only: scaling **`max_exists_calls`** to **7.5×10⁷** and **`lru-maxsize`** to **12×10⁶** (midpoint between the **5e7/8M** PARTIAL bracket and the **1e8/16M** heavy run) yields either a definite **`d=3 feasible=`** line (PASS/FAIL) or a **clean PARTIAL** with **`exceeded max_exists_calls`** within **~1 h** wall on this host class — i.e. completes the DP cap path without host kill.

**Context:** **5e7/8M** hit budget in **~421 s** with LRU at cap. **1e8/16M** ran **~95 min** then **exit 247** (no PARTIAL line). This shard brackets whether **intermediate** cache+budget finishes or still PARTIALs predictably.

## Analogy pass (abbrev.)

1. **Abstract structure:** Transposition-table search with two coupled caps (visit budget, table size); intermediate settings interpolate eviction vs depth explored.
2. **Analogous domains:** (i) chess engine hash at 12M vs 8M nodes with 1.5× node budget; (ii) numerical continuation stepping between two stable regimes; (iii) cache hierarchy sizing between L2 sizes.
3. **Machinery:** Hit rate vs capacity curve; whether 12M entries + 50% more visits crosses root before cap.
4. **Transfer seed:** **Bracket refinement** — isolate **resource** scaling without changing **`r`** or **`d`**.

**Parent experiments:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-lru-8m` (INCONCLUSIVE PARTIAL); `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-1e8-lru-16m` (INCONCLUSIVE host kill).
