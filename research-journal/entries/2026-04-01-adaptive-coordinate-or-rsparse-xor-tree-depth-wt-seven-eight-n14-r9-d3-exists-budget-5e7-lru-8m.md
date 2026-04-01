# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-5e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-5e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=9` XOR language, `d=3`-only probe with **5×10⁷** `exists_tree` budget and **8×10⁶** LRU cap (mirror of **`r=5`/`r=6`** at the same envelope).

## Hypothesis tested

See `hypothesis.md`: determine whether **`r=9`** completes like **`r=6`** or PARTIALs like **`r=5`** when **(budget, LRU, d-window)** are fixed.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **5×10⁷** invocations exhausted in **~542 s** with LRU at cap **8×10⁶**; no certified `min_d` for `d=3`.

## Key finding

**`r=9`** behaves like **`r=5`** (hard at this scale), **not** like **`r=6`** (which **PASS**es **`min_d=3`** under the same **5e7/8M** envelope). Despite **`C(14,9)=C(14,5)=2002`** splits, **parity pattern** dominates **menu cardinality** for bounded-DP difficulty.

## Implications

- **`r=9` `d=3`** remains **open** for a **definite** feasibility bit at **standard** bounded resources.
- **`r=6`** “easy window” is **not** explained by **split count alone**; compare **`r=8`**, **`r=10`**, unions.

## Analogy pass summary

Dual binomial pairing (**2002** splits) as a control on **count** while varying **XOR functional**; game-tree memo footprint vs split geometry.

## Space-definition

None.
