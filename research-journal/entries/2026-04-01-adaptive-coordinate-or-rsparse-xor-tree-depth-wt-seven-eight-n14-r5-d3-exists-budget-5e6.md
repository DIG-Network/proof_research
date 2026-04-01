# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e6

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e6/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=5` XOR language, `d=3`-only probe with unbounded LRU.

## Hypothesis tested

A **5×10⁶** cap on `exists_tree` invocations completes within **≤120 s** and yields a definite `d=3` feasibility bit (see `hypothesis.md`).

## Outcome

**FAIL** — budget exhausted in **~38.6 s** (exit **2** from parent); no `min_d` decision.

## Key finding

**5×10⁶** `exists_tree` calls are negligible versus the work implied by **2 h** wall-clock timeouts that never left `probing d=3 …`. Calibrated rate ~**7.7×10⁴** invocations/s on the automation host for this partial phase.

## Implications

- Use **invocation budgets** (and LRU `currsize`) as a **portable partial-progress** metric alongside wall-clock timeouts.
- The **`r=5`, `d=3`** decision remains **open**; strategy unchanged: longer runs / sharding / algorithmic change.

## Analogy pass summary

Counted combinatorial search nodes (DP calls) like branch-and-bound diagnostics rather than relying on wall-clock alone.

## Space-definition

None.
