# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-11e7-lru-10m

**Date:** 2026-04-02  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-11e7-lru-10m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only with **1.1×10⁸** `exists_tree` budget and **10×10⁶** LRU (+10% visits over **10e7/10M**; **12M** LRU avoided).

## Hypothesis tested

See `hypothesis.md`.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **1.1×10⁸** invocations exhausted in **~992.5 s** DP with LRU at cap **10M**; no certified completion for `d=3`.

## Key finding

**+10⁷** visits (**+10%** over **10e7**) at **10M** LRU added **~154 s** for **`r=5`** (**992.5** vs **~838** s) — still **PARTIAL**; marginal **~15.4 µs** per extra call at LRU cap.

## Implications

- **10M** LRU remains the safe ceiling vs **12M** OOM on this host; scaling **exists** budget alone does not clear **`d=3`** at **11e7**.
- **Next:** larger **exists** steps, **sharded** XOR scans, **binding** track, or high-RAM **`lru-maxsize 0`** with risk awareness.

## Analogy pass summary

See `hypothesis.md`.

## Space-definition

None.
