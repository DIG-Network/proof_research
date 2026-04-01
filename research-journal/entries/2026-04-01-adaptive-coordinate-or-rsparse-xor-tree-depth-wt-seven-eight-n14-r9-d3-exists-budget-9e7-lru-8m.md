# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-9e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-9e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only with **9×10⁷** `exists_tree` budget and **8×10⁶** LRU (paired with **`r=5`** **9e7** after dual **PARTIAL** at **8e7**).

## Hypothesis tested

See `hypothesis.md`: **9e7** might complete **`r=9`** `d=3` where **8e7** did not.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **9×10⁷** invocations exhausted in **~815.3 s** DP with LRU at cap.

## Key finding

**+10M** over **8e7** added **~121.5 s** DP (**~815** vs **~694** s) — **steeper** than **`r=5`**'s **8e7→9e7** marginal (**~111** s) and than **`r=9`**'s own **7e7→8e7** step (**~98.5** s). **`r=9`** still **faster** than **`r=5`** at **9e7** (**~815** s vs **~827** s).

## Implications

- Same next levers as **`r=5`**; marginal cost growth suggests **8M** LRU is increasingly punitive for the **2002** menus as budgets grow.

## Analogy pass summary

Mirrored **r=5** continuation; dual band stays **PARTIAL** at **9e7/8M**.

## Space-definition

None.
