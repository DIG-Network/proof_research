# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** **`r=9`** mirrors **`r=5`** on **`C(14,9)=2002`** XOR splits. At **7e7/8M**, **`r=9`** finished **PARTIAL** in ~595 s vs **`r=5`** ~644 s. We apply the same **+10M** **`exists_tree`** step (**8e7**) as **`r=5`** to compare wall time and termination at the next budget envelope.

2. **Analogous domains:** (a) Dual coordinates on the same finite menu. (b) Symmetric load under the same cache policy. (c) Chiral pair in a search landscape with different constant factors.

3. **Machinery:** Same parent DP, **`--r-single 9`**, **`8e7`**, **8M** LRU, **`d=3`-only**.

4. **Transfer seed:** If both **8e7** runs **PARTIAL**, the **2002** band is jointly stable at **8e7/8M**; if one completes, **`r↔n−r`** asymmetry reappears at this scale (cf. **`r=4` vs `r=10`** at other budgets).

## Falsifiable claim

**H0:** Under `--max-exists-calls 80000000`, `--lru-maxsize 8000000`, `r=9`, `d=3`-only, the parent exits **2** (PARTIAL).

**H1:** Exit **0** with definite **`d=3 feasible=`** without budget exhaustion.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-7e7-lru-8m` (INCONCLUSIVE PARTIAL ~595 s), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-8e7-lru-8m` (paired budget step).
