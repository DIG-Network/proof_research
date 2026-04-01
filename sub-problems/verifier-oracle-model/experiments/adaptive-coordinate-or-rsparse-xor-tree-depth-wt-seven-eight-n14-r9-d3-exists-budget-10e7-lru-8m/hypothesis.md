# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** Mirror **`r=9`** **`d=3`** continuation: **PARTIAL** at **9×10⁷** / **8M** LRU (~815 s DP). Compare marginal **9e7→10e7** to **`r=5`** at the same step and to prior **`r=9`** steps.

2. **Analogous domains:** Same as **`r=5`** twin: fixed-cache continuation, working-set effects, beam search with fixed beam.

3. **Machinery:** **`--r-single 9`**, **`d=3`-only**, **`100000000`** max exists calls, **8M** LRU.

4. **Transfer seed:** If **`r=9`** stays faster than **`r=5`** at **10e7** but both **PARTIAL**, the dual **2002** band remains open; if one finishes, we get a certified **`d=3`** verdict for that parity class.

## Falsifiable claim

**H0:** Parent exits **2** (PARTIAL) at **10e7**/8M.

**H1:** Exit **0** with definite **`d=3 feasible=`** without budget exhaustion.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-9e7-lru-8m` (~815 s DP PARTIAL), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-8e7-lru-8m`.
