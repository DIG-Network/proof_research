# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** Mirror **`r=5`** **10e7/10M** run for the dual **2002** band: **`r=9`**, **`d=3`-only**, **10⁸** **`exists_tree`**, **10M** LRU. Prior **10e7/8M** for **`r=9`** was **PARTIAL** ~850 s — test whether **+25%** LRU changes **`r=9`** termination similarly to **`r=5`**.

2. **Analogous domains:** (a) Paired A/B on symmetric combinatorial menus. (b) Same continuation as r5 10M experiment.

3. **Machinery:** **`--r-single 9`**, **`--d-min 3 --d-max 3`**, **`100000000`**, **`10000000`** LRU.

4. **Transfer seed:** Compare **`r=9`** vs **`r=5`** wall time and **PARTIAL**/**PASS** at **10e7/10M**; asymmetry already seen at **8M**.

## Falsifiable claim

**H0:** **PARTIAL** (exit **2**) or **OOM** at **10M** LRU.

**H1:** Exit **0** with definite **`d=3`** verdict without budget exhaustion.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-10e7-lru-8m` (INCONCLUSIVE ~850 s), paired with **`r=5`** **10e7/10M** sibling.
