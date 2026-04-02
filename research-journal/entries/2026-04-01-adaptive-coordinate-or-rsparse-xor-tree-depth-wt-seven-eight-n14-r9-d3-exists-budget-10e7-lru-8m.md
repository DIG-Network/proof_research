# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-10e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-10e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only with **10⁸** `exists_tree` budget and **8×10⁶** LRU (mirror **`r=5`** **10e7**; prior **9e7** ~815 s DP PARTIAL).

## Hypothesis tested

See `hypothesis.md`: **10e7** might complete **`r=9` `d=3`** where **9e7** did not.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **~850.2 s** DP; LRU at cap.

## Key finding

**+10M** over **9e7** added only **~35 s** DP for **`r=9`** vs **~90 s** for **`r=5`** — **asymmetric** marginal at this step. **`r=9`** still **faster** overall (~850 s vs ~917 s).

## Implications

- Dual **2002** band still open at **10e7**/8M; **`r=9`** shows milder marginal growth **9e7→10e7** than **`r=5`**.

## Analogy pass summary

Mirror **`r=5`** continuation; **`r=9`** still **PARTIAL** at **10e7**.

## Space-definition

None.
