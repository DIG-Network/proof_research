# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** Scale **`exists_tree`** budget on the **`n=14`**, **`{7,8}`**, **`r=5`**, **`d=3`-only** probe while holding **10M** LRU fixed (per host **12M** OOM constraint). Prior **11e7/10M** was **PARTIAL** ~992 s — test **+10⁷** more visits (**12×10⁷** total).

2. **Analogous domains:** (a) Continuation of marginal budget ladder (5e7 → … → 11e7). (b) Same dual **2002** band as **`r=9`**.

3. **Machinery:** **`--r-single 5`**, **`--d-min 3 --d-max 3`**, **`120000000`**, **`10000000`** LRU.

4. **Transfer seed:** If **12e7** completes **`d=3`** (**PASS**/**FAIL** line) vs **PARTIAL**, we learn whether the **2002** **`r=5`** instance is budget-limited at **10M** LRU.

## Falsifiable claim

**H0:** **PARTIAL** (exit **2**) or host kill.

**H1:** Exit **0** with definite **`d=3`** verdict without budget exhaustion.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-11e7-lru-10m` (INCONCLUSIVE PARTIAL ~992 s), paired **`r=9`** **12e7/10M** sibling.
