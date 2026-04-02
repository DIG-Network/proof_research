# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-10e7-lru-10m

**Date:** 2026-04-02  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-10e7-lru-10m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only with **10⁸** `exists_tree` budget and **10×10⁶** LRU (intermediate between **8M** and prior **12M** OOM class).

## Hypothesis tested

See `hypothesis.md`: **10M** LRU might allow **d=3** completion at **10e7** where **8M** did not.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **10⁸** invocations exhausted in **~837.5 s** DP with LRU at cap **10M**; no certified completion for `d=3`.

## Key finding

**8M→10M** **speeds up** **`r=5`** **~916.6→837.5 s** at **10e7** but **still** **PARTIAL** — larger cache **reduces** time **without** changing the budget-limited verdict.

## Implications

- **Next:** unbounded/sharded memo on high-RAM host, algorithmic change, or **anonymous-quorum-binding**; compare **`r=9`** **10e7/10m** for LRU asymmetry.

## Analogy pass summary

Continuation: modest LRU expansion under fixed **10e7** budget.

## Space-definition

None.
