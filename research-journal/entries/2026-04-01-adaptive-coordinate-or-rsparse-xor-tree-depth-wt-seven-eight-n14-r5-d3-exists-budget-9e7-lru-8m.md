# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-9e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-9e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only with **9×10⁷** `exists_tree` budget and **8×10⁶** LRU (next step after **8e7** remained PARTIAL ~716 s DP).

## Hypothesis tested

See `hypothesis.md`: **9e7** might complete the root `d=3` decision where **8e7** did not.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **9×10⁷** invocations exhausted in **~826.8 s** DP with LRU at cap; no certified non-PARTIAL completion for `d=3`.

## Key finding

**+10M** over **8e7** cost **~110.7 s** DP (**~827** vs **~716** s), **steeper** than prior **7e7→8e7** marginal (**~72** s), consistent with worsening reuse under **8M** LRU as the walk extends.

## Implications

- Next: **10e7+**, **larger LRU**, **unbounded**/sharded memo on a high-RAM host, algorithmic change, or **anonymous-quorum-binding** thread; pair with **`r=9`** **9e7** for the dual **2002** band.

## Analogy pass summary

Fixed-LRU continuation; **9e7** still does not resolve **`r=5` `d=3`**.

## Space-definition

None.
