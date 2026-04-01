# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r4-d3-exists-budget-5e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r4-d3-exists-budget-5e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=4` XOR, `d=3`-only with **5×10⁷** `exists_tree` budget and **8×10⁶** LRU cap. **C(14,4)=C(14,10)=1001** splits (binomial dual of **`r=10`**).

## Hypothesis tested

Whether **`r=4`** mirrors **`r=10`** ease at the same split count and envelope.

## Outcome

**INCONCLUSIVE** — **PARTIAL** at **50M** **`exists_tree`** cap, **LRU** saturated **8M**, **~467 s** DP (**exit 2**). No certified **`min_d`**.

## Key finding

**Menu cardinality symmetry does not imply DP symmetry:** **`r=4`** and **`r=10`** both have **1001** XOR partitions, but **`r=10`** **PASS**ed in **~55 s** while **`r=4`** hits the **same** budget ceiling as the hard **2002**-split band (order of magnitude **~420–470 s** to cap). **Low-**`r`** sparse XOR** can be **much harder** than **high-**`r`** dual** for this adaptive separation DP.

## Implications

- Do **not** use **`C(n,r)=C(n,n−r)`** to predict **runtime** or **feasibility** at fixed **`(n,wt shells)`**.
- **`r=7`** (**3432**) remains the next **>**3003 menu probe per prior plan; **`r=4`** may need **stronger** resources for a **definite** verdict.

## Analogy pass summary

**Dual codes** share **length** but **not** always **decoder complexity** — here **dual **`r`**** shares **split count** but **not** **DP** **trajectory**.

## Space-definition

None.
