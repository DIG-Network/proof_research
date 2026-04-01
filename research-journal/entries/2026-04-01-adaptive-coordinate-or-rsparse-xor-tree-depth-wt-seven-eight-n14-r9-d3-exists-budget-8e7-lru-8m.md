# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-8e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-8e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only with **8×10⁷** `exists_tree` budget and **8×10⁶** LRU (mirror of **r=5** **8e7**; dual to **7e7** **r=9** ~595 s).

## Hypothesis tested

See `hypothesis.md`: **8e7** might complete **`r=9`** `d=3` where **7e7** did not.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **8×10⁷** invocations exhausted in **~693.8 s** DP; LRU at cap.

## Key finding

**+10M** over **7e7** for **`r=9`** cost **~98.5 s** DP (steeper marginal than **`r=5`**'s **~72** s for the same increment). **`r=9`** remains faster than **`r=5`** at **8e7** (**~694** vs **~716** s) but both **PARTIAL**.

## Implications

Dual **2002** band stable at **8e7/8M**; **`r↔n−r`** does not equalize wall time at this budget ( **`r=9`** cheaper ).

## Analogy pass summary

Dual-coordinate mirror; both sides fail to terminate within budget.

## Space-definition

None.
