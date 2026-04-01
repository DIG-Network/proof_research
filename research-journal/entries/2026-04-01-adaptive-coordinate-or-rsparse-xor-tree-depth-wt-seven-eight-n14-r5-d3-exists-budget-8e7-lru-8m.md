# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-8e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-8e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only with **8×10⁷** `exists_tree` budget and **8×10⁶** LRU (next step after **7e7** remained PARTIAL ~644 s).

## Hypothesis tested

See `hypothesis.md`: **8e7** might complete the root `d=3` decision where **7e7** did not.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **8×10⁷** invocations exhausted in **~716.1 s** DP with LRU at cap; no certified non-PARTIAL completion for `d=3`.

## Key finding

**+10M** over **7e7** cost **~72 s** DP (**~716** vs **~644** s), similar to the **6e7→7e7** marginal step. **+60%** over **5e7** at **8M** LRU still does not resolve **`r=5` `d=3`**.

## Implications

- Next: **9e7+**, **unbounded**/sharded memo, or algorithmic change; paired **`r=9`** **8e7** documents the dual **2002** band at the same envelope.

## Analogy pass summary

Fixed-LRU continuation; falsified completion at **8e7** for **r=5**.

## Space-definition

None.
