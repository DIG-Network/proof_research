# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-d3-exists-budget-5e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-d3-exists-budget-5e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=6` XOR language, `d=3`-only probe with **5×10⁷** `exists_tree` budget and **8×10⁶** LRU cap (mirror of the **`r=5`** shard that remained PARTIAL at this scale).

## Hypothesis tested

See `hypothesis.md`: compare **`r=6`** to **`r=5`** under identical **(budget, LRU, d-window)**.

## Outcome

**PASS** — parent exit **0**; **`d=3 feasible=True`**, certified **`min_d=3`**; DP ~**435.3 s**, **3003** `coord+6xor` splits; **did not** exhaust **50M** `exists_tree` cap.

## Key finding

**Same** **(5e7, LRU 8M)** that **failed** to decide **`r=5` `d=3`** **suffices** to **certify** **`r=6` `d=3`**. Non-monotone **`r`** difficulty at **`n=14` `{7,8}`**: **`r=6`** is **easier** than **`r=5`** at this resource level.

## Implications

- Treat **`r=6` `d=3`** as **settled** at **`min_d=3`** for this language family (bounded LRU at this scale).
- Keep **`r=5` `d=3`** as the **primary** remaining heavy shard for **`n=14`** unless a larger budget or unbounded memo is applied.

## Analogy pass summary

Controlled **`r`** with fixed memo budget; branching / working-set difference between 5- vs 6-sparse XOR libraries.

## Space-definition

None.
