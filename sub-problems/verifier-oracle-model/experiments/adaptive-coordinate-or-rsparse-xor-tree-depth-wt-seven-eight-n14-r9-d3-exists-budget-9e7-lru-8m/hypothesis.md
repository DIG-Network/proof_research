# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** **`r=9`** **`d=3`** mirrored **`r=5`** at **8e7/8M** (**PARTIAL** ~694 s DP, faster than **r=5** ~716 s). We mirror the **+10M** budget step to **9e7** to see whether the dual **2002** band stays synchronized and whether **`r=9`** remains cheaper per call at the same cap.

2. **Analogous domains:** Same as paired **r=5** run — fixed-cache continuation; comparative stress test across symmetric **r↔n−r** split count.

3. **Machinery:** **`--r-single 9`**, **`--d-min 3 --d-max 3`**, **`9e7`**, **8M** LRU.

4. **Transfer seed:** If **9e7** **PARTIAL** for both **r=5** and **r=9**, the **2002** band is still open at **+80%** over **5e7** at **8M** LRU.

## Falsifiable claim

**H0:** Parent exits **2** (PARTIAL) at **9×10⁷** **`exists_tree`** with **8M** LRU.

**H1:** Exit **0** with certified completion for **`d=3`**.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-8e7-lru-8m` (INCONCLUSIVE PARTIAL ~694 s DP), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-7e7-lru-8m` (~595 s).
