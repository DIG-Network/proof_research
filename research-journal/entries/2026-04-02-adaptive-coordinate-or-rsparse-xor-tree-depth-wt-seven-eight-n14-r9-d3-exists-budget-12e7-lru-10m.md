# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-12e7-lru-10m

**Date:** 2026-04-02  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-12e7-lru-10m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only with **1.2×10⁸** `exists_tree` budget and **10×10⁶** LRU (paired with **`r=5`** **12e7/10M**).

## Hypothesis tested

See `hypothesis.md`.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **1.2×10⁸** invocations exhausted in **~965.3 s** DP with LRU at cap **10M**; no certified completion for `d=3`.

## Key finding

**11e7→12e7** added **~53.8 s** for **`r=9`** (**~911.5 → ~965.3** s) — **milder** marginal than **`r=5`**’s **~84.6 s** at same tier; **`r=9`** remains faster than **`r=5`**.

## Implications

Dual **2002** **`d=3`** band still **open**; **`r=9`** continues to exhibit **favorable** scaling vs **`r=5`** at fixed **10M** LRU.

## Analogy pass summary

See `hypothesis.md`.

## Space-definition

None.
