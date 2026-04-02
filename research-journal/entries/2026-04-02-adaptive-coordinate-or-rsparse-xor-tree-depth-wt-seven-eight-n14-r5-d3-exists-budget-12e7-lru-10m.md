# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-12e7-lru-10m

**Date:** 2026-04-02  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-12e7-lru-10m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only with **1.2×10⁸** `exists_tree` budget and **10×10⁶** LRU (paired with **`r=9`** **12e7/10M**).

## Hypothesis tested

See `hypothesis.md`.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **1.2×10⁸** invocations exhausted in **~1076.6 s** DP with LRU at cap **10M**; no certified completion for `d=3`.

## Key finding

**11e7→12e7** added **~84.6 s** for **`r=5`** at **10M** LRU (**~992 → ~1076.6** s) — marginal cost in line with prior **+10⁷** steps; still **PARTIAL**.

## Implications

Budget scaling alone at **10M** LRU has not closed **`r=5`** **`d=3`**; consider **sharding**, alternate menus, or **binding** track.

## Analogy pass summary

See `hypothesis.md`.

## Space-definition

None.
