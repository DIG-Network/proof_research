# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-10e7-lru-10m

**Date:** 2026-04-02  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-10e7-lru-10m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only with **10⁸** `exists_tree` budget and **10×10⁶** LRU (mirror **`r=5`** **10e7/10m**).

## Hypothesis tested

See `hypothesis.md`: **`r=9`** might mirror **`r=5`** LRU speedup at **10M**.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **10⁸** invocations exhausted in **~956.7 s** DP with LRU at cap **10M**.

## Key finding

**Opposite** LRU effect vs **`r=5`**: **`r=9`** **8M→10M** **slowed** DP (**~850→957** s) at **10e7**; **`r=9`** **no longer** faster than **`r=5`** at this (**10M**) setting.

## Implications

- Dual **2002** band: LRU scaling is **not** uniform across **`r=5`** vs **`r=9`**; next levers unchanged (more RAM / sharding / algorithm).

## Analogy pass summary

Paired dual-2002 LRU continuation.

## Space-definition

None.
