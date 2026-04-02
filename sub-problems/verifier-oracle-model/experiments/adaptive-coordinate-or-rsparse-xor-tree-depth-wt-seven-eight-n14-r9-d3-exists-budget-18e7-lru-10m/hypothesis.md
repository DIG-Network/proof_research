# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** The **`n=14`**, **`{7,8}`**, **`r=9`** full XOR menu (**2002** splits) **`d=3`** decision problem has hit repeated **PARTIAL** at **10M** LRU with budgets **10e7–15e7** (full menu and half-shards). Marginal time per extra **`exists_tree`** call at LRU cap is finite; **1.8×10⁸** is a **~50%** step over **12e7** (prior **r=9** full-menu anchor **~965 s**).

2. **Analogous domains:** (a) Continuation / stress testing of a bounded-work unit (like extending a numerical integration cap). (b) Same DP as prior **r=9** budget ladder experiments. (c) Session guidance: prefer **≥~2×** budget or structural change over **+25%** half-shard tweaks.

3. **Machinery:** Parent **`--r-single 9`**, **`d=3`-only**, **`180000000`** **`--max-exists-calls`**, **`10000000`** LRU (**no** **12M** — **OOM** class on this profile).

4. **Transfer seed:** If **18e7** completes, we get a definite **`d=3`** **`feasible=`** line; if **PARTIAL**, record wall time and LRU state to compare marginal cost vs **12e7** and **15e7** half-shards.

## Falsifiable claim

**H0:** **PARTIAL** (exit **2**) — budget exhausted before a complete **`d=3`** verdict.

**H1:** Exit **0** with explicit **`d=3 feasible=True|False`** (complete probe under cap).

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-12e7-lru-10m` (INCONCLUSIVE **~965 s**), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-15e7-each-lru-10m` (INCONCLUSIVE dual half-shards).
