# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** The **`r=5`** **`d=3`** probe remained **PARTIAL** at **9×10⁷** **`exists_tree`** with **8M** LRU (~827 s DP). Marginal cost **8e7→9e7** was **~111 s** per +10M, steeper than **7e7→8e7**. We add **+10M** to **9e7** (**10⁸** total) at the same LRU to test whether the **2002**-split root probe terminates.

2. **Analogous domains:** (a) Fixed-cache numerical continuation. (b) Working-set thrashing vs eventual convergence. (c) Beam search with fixed beam width.

3. **Machinery:** Same parent DP, **`--r-single 5`**, **`--d-min 3 --d-max 3`**, **`100000000`** max exists calls, **8M** LRU.

4. **Transfer seed:** If **10e7** still **PARTIAL** with marginal DP time still growing super-linearly in +10M steps, the **r=5** band is robustly cache/budget-limited at **8M** LRU; next levers are **larger LRU**, **unbounded**/sharded memo, or algorithmic change.

## Falsifiable claim

**H0:** Under `--max-exists-calls 100000000`, `--lru-maxsize 8000000`, `r=5`, `d=3`-only, the parent exits **2** (PARTIAL).

**H1:** Exit **0** with definite **`d=3 feasible=`** without budget exhaustion mid-probe.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-9e7-lru-8m` (INCONCLUSIVE PARTIAL ~827 s DP), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-8e7-lru-8m` (~716 s).
