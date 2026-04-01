# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-partition-shard-scan-offset-100

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-partition-shard-scan-offset-100/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `r=5`, `d=3`-only. Follow-up to contiguous XOR shards from index `0`; this run uses **index offset 100** and slices `100:500`, `500:900`, …, `1700:2002`.

## Hypothesis tested

Phase-shifted contiguous XOR sub-menus (skipping the first 100 bipartitions) might hit a different empirical feasibility profile at `d=3` under the same LRU 8M and 5.5×10⁷ `exists_tree` budget.

## Outcome

**PASS** — all five shards completed; **no** shard reported `feasible=True` at `d=3`.

## Key finding

Behavior matches the **0-origin** 400-wide shards: each 400-split shard saturated **LRU 8M** at `d=3` and returned **`feasible=False`** within budget; the shorter final shard (302 splits) finished with **fewer** cache misses (~3.92×10⁶) and **`feasible=False`**. No evidence that shifting the window by 100 indices surfaces a depth-3 witness.

## Implications

- Another **negative-only** data point for **bounded** `r=5`, `d=3` exploration; full-menu `d=3` remains **open**.
- Next: non-contiguous / random XOR ensembles, larger RAM full DP, other `r` or algorithmic changes — not logical inference from shard negatives alone.

## Analogy pass summary

Phase shift / stratified index offset to reduce boundary bias in an ordered generator list.

## Space-definition

None.
