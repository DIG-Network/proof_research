# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** The **`n=14`**, **`{7,8}`** full XOR menu (**2002** splits) **`d=3`** probe is symmetric under **`r ↔ 9−r`** for the **`r`-sparse** coordinate model. **`r=9`** at **18e7/10M** was **PARTIAL** (**~1644 s**). The **`r=5`** mirror (**complement size **9**) should receive the **same** **18e7/10M** budget to compare wall time and completion vs the **`r=9`** lane.

2. **Analogous domains:** (a) Dual / complement symmetry in combinatorial search. (b) Same DP as **`r=9`** **18e7** experiment with **`--r-single 5`**. (c) Session guidance: run **`r=5`** mirror before another **`+10%`** half-shard tweak.

3. **Machinery:** Parent **`--r-single 5`**, **`d=3`-only**, **`180000000`** **`--max-exists-calls`**, **`10000000`** LRU.

4. **Transfer seed:** If **`r=5`** finishes **faster** or **completes** where **`r=9`** did not, that refines where the **2002** menu is hardest; if **PARTIAL** with similar wall, symmetry suggests **both** lanes need **structural** DP change or **larger** host/LRU.

## Falsifiable claim

**H0:** **PARTIAL** (exit **2**) — budget exhausted before a complete **`d=3`** verdict.

**H1:** Exit **0** with explicit **`d=3 feasible=True|False`** (complete probe under cap).

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-12e7-lru-10m` (INCONCLUSIVE), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-18e7-lru-10m` (INCONCLUSIVE **~1644 s**).
