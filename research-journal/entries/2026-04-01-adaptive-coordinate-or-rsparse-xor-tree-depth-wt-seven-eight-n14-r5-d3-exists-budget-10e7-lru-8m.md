# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-10e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-10e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only with **10⁸** `exists_tree` budget and **8×10⁶** LRU (next step after **9e7** remained PARTIAL ~827 s DP).

## Hypothesis tested

See `hypothesis.md`: **10e7** might complete the root `d=3` decision where **9e7** did not.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **10⁸** invocations exhausted in **~916.6 s** DP with LRU at cap; no certified non-PARTIAL completion for `d=3`.

## Key finding

**+10M** over **9e7** cost **~90 s** DP marginal — **less steep** than **8e7→9e7** **~111 s** for **`r=5`**, but still **PARTIAL**.

## Implications

- Next: larger LRU, unbounded/sharded memo, algorithmic change, or **anonymous-quorum-binding**; pair with **`r=9`** **10e7** for the dual **2002** band.

## Analogy pass summary

Fixed-LRU continuation; **10e7** still does not resolve **`r=5` `d=3`**.

## Space-definition

None.
