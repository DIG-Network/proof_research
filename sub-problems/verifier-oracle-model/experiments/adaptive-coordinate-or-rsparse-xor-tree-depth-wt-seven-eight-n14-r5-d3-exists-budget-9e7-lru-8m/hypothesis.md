# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** The **`r=5`** **`d=3`** probe remained **PARTIAL** at **8×10⁷** **`exists_tree`** with **8M** LRU (~716 s DP). Prior marginal steps **6e7→7e7** and **7e7→8e7** each added ~72–74 s per +10M calls. We add **+10M** to **8e7** (**9×10⁷** total) at the same LRU to test whether the **2002**-split root probe ever terminates without budget exhaustion.

2. **Analogous domains:** (a) Fixed-cache numerical continuation — more iterations with same RAM. (b) Paging / working-set — thrashing vs convergence. (c) Beam search with fixed beam — deeper search may or may not finish.

3. **Machinery:** Same parent DP, **`--r-single 5`**, **`--d-min 3 --d-max 3`**, **`9e7`**, **8M** LRU.

4. **Transfer seed:** If **9e7** still **PARTIAL** with marginal cost still ~linear in +10M, the **r=5** band is robustly budget-limited at **8M** LRU; next levers are **larger LRU**, **unbounded**/sharded memo, or algorithmic change.

## Falsifiable claim

**H0:** Under `--max-exists-calls 90000000`, `--lru-maxsize 8000000`, `r=5`, `d=3`-only, the parent exits **2** (PARTIAL).

**H1:** Exit **0** with definite **`d=3 feasible=`** without budget exhaustion mid-probe.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-8e7-lru-8m` (INCONCLUSIVE PARTIAL ~716 s DP), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-7e7-lru-8m` (~644 s).
