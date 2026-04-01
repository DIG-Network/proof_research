# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-partition-shard-scan-400

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-partition-shard-scan-400/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `r=9`, `d=3`-only. Mirrors the contiguous XOR-menu shard scan done for `r=5` (same 2002 XOR bipartitions).

## Hypothesis tested

Five contiguous shards partitioning `[0,2002)` finish under **LRU 8M** and **5.5×10⁷** `exists_tree` budget; search for any shard with `d=3 feasible=True`.

## Outcome

**PASS** — all five shards completed; **no** shard reported `feasible=True` at `d=3`.

## Key finding

Each shard saturated **LRU 8M** during the `d=3` probe (8M cache misses printed) yet returned **`feasible=False`** within budget — parallel qualitative behavior to **`r=5`** shard scan. **Does not** prove full-menu `d=3` infeasibility for `r=9`; full-menu **5e7**/**8M** remains **PARTIAL** without root decision.

## Implications

- Strengthens evidence that **`r=9`** behaves like **`r=5`** on **contiguous** XOR-menu slices (hard / negative at `d=3` in every tested block), while **`r=6`/`r=8`** pass on the full menu at the same envelope — **parity structure** dominates over raw split count.
- Next: non-contiguous **`--xor-index-indices`** for `r=9` (as for `r=5`), larger budgets, or different memo policies — not logical closure from shard negatives alone.

## Analogy pass summary

Same divide-and-conquer on the XOR generator menu as `r=5` shard scan; complement-symmetric menu size, asymmetric DP difficulty.

## Space-definition

None.
