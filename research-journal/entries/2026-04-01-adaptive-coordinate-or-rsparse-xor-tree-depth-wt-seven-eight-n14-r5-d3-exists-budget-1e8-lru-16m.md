# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-1e8-lru-16m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-1e8-lru-16m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=5` XOR language, `d=3`-only probe with **10⁸** `exists_tree` budget and **16×10⁶** LRU cap (2× over the 5e7/8M partial run).

## Hypothesis tested

See `hypothesis.md`: joint scaling of cache and visit budget to escape LRU saturation at 8M or obtain a definite `d=3` feasibility bit.

## Outcome

**INCONCLUSIVE** — automation/host terminated the run (~95 min wall) before any `feasible=` or `PARTIAL: exceeded max_exists_calls` line; wrapper exit **247**, not parent **0/1/2**.

## Key finding

Doubling **(budget, LRU)** did **not** reproduce a clean **PARTIAL** within the available wall clock here; the **16M** LRU configuration appears **slower per unit time** than **8M** at 5e7 (larger working set / eviction dynamics), so **longer** runs or **unbounded** memo on large RAM remain the honest next steps.

## Implications

- **`r=5` `d=3`** remains **undecided** at this scale in this environment.
- Prefer **incremental** brackets or **`lru-maxsize 0`** with explicit **timeout** on a **large-RAM** host over another **2×** jump on a **time-capped** worker.

## Analogy pass summary

Joint refinement of transposition-table size and node visit budget in game-tree search.

## Space-definition

None.
