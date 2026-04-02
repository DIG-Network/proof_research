# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-11e7-lru-10m

**Date:** 2026-04-02  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-11e7-lru-10m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only with **1.1×10⁸** `exists_tree` budget and **10×10⁶** LRU (paired with **`r=5`** **11e7/10M**).

## Hypothesis tested

See `hypothesis.md`.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **1.1×10⁸** invocations exhausted in **~911.5 s** DP with LRU at cap **10M**; no certified completion for `d=3`.

## Key finding

**+10⁷** visits at **10M** LRU **reduced** wall time vs **`r=9`** **10e7/10M** (**911.5** vs **~957** s) — **opposite** marginal sign to **`r=5`** (**838→992** s). Dual **2002** band still **PARTIAL**.

## Implications

**`r=9`** response to extra budget differs from **`r=5`** at this envelope; full-menu **`d=3`** remains **open** for both.

## Analogy pass summary

See `hypothesis.md`.

## Space-definition

None.
