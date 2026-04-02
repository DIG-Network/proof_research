# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** Extend the **`r=9`** full **2002** XOR menu probe by **+6×10⁷** **`exists_tree`** calls (**18e7 → 24e7**) at fixed **10M** LRU — same marginal-cost regime as **12e7 → 18e7**, testing whether the menu completes before budget exhaustion.

2. **Analogous domains:** (a) Fixed-cache scaling of exhaustive DP frontiers. (b) Prior **`r=9`** budget ladder (**10e7 … 18e7**) at **10M** LRU.

3. **Machinery:** **`--r-single 9`**, **`--d-min 3 --d-max 3`**, **`240000000`**, **`10000000`** LRU.

4. **Transfer seed:** Linear wall extrapolation from **18e7 ~1644.6 s** suggests **~45 min** class; if completion is near, this step may yield exit **0**; if LRU saturation dominates, expect **PARTIAL** again.

## Falsifiable claim

**H0:** **PARTIAL** (exit **2**) or host kill.

**H1:** Exit **0** with definite **`d=3`** verdict without budget exhaustion.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-18e7-lru-10m` (INCONCLUSIVE PARTIAL ~1644.56 s at **180M**/**10M**).
