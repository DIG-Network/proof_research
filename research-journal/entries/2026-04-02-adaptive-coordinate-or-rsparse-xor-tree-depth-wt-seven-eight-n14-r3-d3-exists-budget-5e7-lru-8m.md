# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r3-d3-exists-budget-5e7-lru-8m

**Date:** 2026-04-02  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r3-d3-exists-budget-5e7-lru-8m/`  
**Context:** verifier-oracle-model  

## Hypothesis tested

On `n=14`, `{7,8}`, `coord + r=3` XOR, `d=3`-only at **5e7/8M**, the DP completes with a definite feasibility bit (not PARTIAL).

## Outcome: PASS

**Key finding:** Full **`C(14,3)=364`** menu certifies **`d=3 feasible=False`** in ~82 s DP; LRU saturated (8M misses) but search finished — unlike **`r=5`/`r=9`** PARTIAL at the same envelope. Fills the missing low-**`r`** point: **`r=3`** rules out depth 3; **`r=4`** still PARTIAL at 5e7/8M.

## Implications

- **`C(14,r)`** alone does not sort **`d=3`** hardness (**364** definite **False** vs **1001** PARTIAL vs **3432** trivial **True**).
- Next: optional **`d=4`-only** probe for **`r=3`** to pin **`min_d`**, or continue **`r=5`/`r=9`** on a larger host (no parallel 10M×2 XOR).

## Analogy pass summary

See `hypothesis.md` — sparse XOR menu / low-rank coding analogy; gap-fill between **`r=2`** and **`r=4`** regimes.
