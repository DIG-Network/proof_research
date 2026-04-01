# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r10-d3-exists-budget-5e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r10-d3-exists-budget-5e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=10` XOR, `d=3`-only with **5×10⁷** `exists_tree` budget and **8×10⁶** LRU cap. **C(14,10)=C(14,4)=1001** splits (not 2002).

## Hypothesis tested

Whether **`r=10`** at this envelope **PARTIAL**s like high-**r** hard cases or **PASS**es; whether **smaller** menus than **2002** are automatically easy.

## Outcome

**PASS** — **`d=3 feasible=True`**, **`min_d=3`**, DP **~54.6 s** (build **~2.4 s**), well within budget.

## Key finding

**`r=10`** is **easy** at **5e7/8M** despite **5e6**-budget **PARTIAL** in the **`r∈{8,9,10}`** spot check — **scaling budget** matters. **1001** splits finish **faster** than **3003**-split **`r=6`/`r=8`**, while **2002**-split **`r=5`/`r=9`** still **PARTIAL** at this envelope: **hardness is not sorted by `C(14,r)`** alone.

## Implications

- **Dual check:** run **`r=4`** (**1001**) for binomial symmetry with **`r=10`**.
- **Session narrative fix:** **`r=10`** is **not** “same count as **`r=5`/`r=9`**” — those are **2002**.

## Analogy pass summary

**Menu size** vs **split geometry:** smaller **C(n,r)** can be **easier** DP if the **parity map** cooperates; **2002** band remains the **stuck** region at **5e7/8M**.

## Space-definition

None.
