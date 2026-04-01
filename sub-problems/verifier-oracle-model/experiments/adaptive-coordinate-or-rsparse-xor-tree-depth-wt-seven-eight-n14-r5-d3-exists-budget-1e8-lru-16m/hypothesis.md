# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, `coord + r=5`, `d=3`-only: doubling both **`max_exists_calls`** (**5×10⁷ → 10⁸**) and **`lru-maxsize`** (**8×10⁶ → 16×10⁶**) either yields a definite **`d=3 feasible=`** bit (PASS or FAIL) or remains PARTIAL — in the latter case LRU thrashing at 8M is confirmed as a dominant limiter for this shard.

**Context:** Prior run **`…-r5-d3-exists-budget-5e7-lru-8m`** hit **`max_exists_calls`** with LRU **saturated** at 8M after ~420 s — no root decision. **`r=6`** at the same (5e7, 8M) completed with **`min_d=3`**. Hypothesis: **`r=5`** may need a **larger working set** (fewer evictions) **and** more DP budget to finish.

## Analogy pass (abbrev.)

1. **Abstract structure:** Fixed-depth feasibility DP on a large state graph; LRU memo = finite cache on an implicit graph traversal; budget caps total node visits.
2. **Analogous domains:** (i) graph search with transposition table size vs time; (ii) numerical PDE with mesh + timestep refinement both doubled; (iii) SAT CDCL with learned-clause DB cap doubled alongside conflict limit.
3. **Machinery:** Cache hit rate vs eviction rate; whether the frontier of distinct `(mask, depth)` keys fits in 16M when 8M did not.
4. **Transfer seed:** **Joint scaling** of **cache** and **visit budget** — isolate from **`r`** (held at 5).

**Parent experiments:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-lru-8m` (INCONCLUSIVE PARTIAL); `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-d3-exists-budget-5e7-lru-8m` (PASS).
