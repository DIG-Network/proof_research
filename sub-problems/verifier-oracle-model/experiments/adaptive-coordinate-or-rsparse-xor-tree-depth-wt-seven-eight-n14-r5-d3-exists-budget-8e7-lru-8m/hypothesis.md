# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** The **`r=5`** **`d=3`** probe remained **PARTIAL** at **6e7** and **7e7** with **8M** LRU (~569 s then ~644 s). Marginal cost **6e7→7e7** was ~74 s for +10M calls — sublinear in the sense of amortized reuse under LRU pressure. We step **`exists_tree`** budget to **8×10⁷** at the same LRU to see whether the **2002**-split root probe completes or stays truncated.

2. **Analogous domains:** (a) Fixed-memory iterative solvers — more flops without more RAM may or may not converge. (b) Paging / working-set models — larger iteration count with fixed cache size. (c) Resource-bounded search — deeper beam before cutoff.

3. **Machinery:** Same parent DP, **`--r-single 5`**, **`--d-min 3 --d-max 3`**, **`8e7`**, **8M** LRU.

4. **Transfer seed:** If **8e7** still **PARTIAL**, the **r=5** band is stable under **+60%** over **5e7** at **8M** LRU; next levers are **unbounded**/sharded memo or algorithmic change.

## Falsifiable claim

**H0:** Under `--max-exists-calls 80000000`, `--lru-maxsize 8000000`, `r=5`, `d=3`-only, the parent exits **2** (PARTIAL).

**H1:** Exit **0** with definite **`d=3 feasible=`** without budget exhaustion mid-probe.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-7e7-lru-8m` (INCONCLUSIVE PARTIAL ~644 s), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-6e7-lru-8m` (~569 s).
