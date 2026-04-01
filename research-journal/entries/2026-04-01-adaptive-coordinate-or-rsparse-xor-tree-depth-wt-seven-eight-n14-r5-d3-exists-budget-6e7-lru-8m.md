# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-6e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-6e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=5` XOR language, `d=3`-only probe with **6×10⁷** `exists_tree` budget and **8×10⁶** LRU cap (+20% invocations vs **5×10⁷** shard).

## Hypothesis tested

See `hypothesis.md`: a modest budget increase might cross from PARTIAL to a definite `d=3` feasibility bit.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **6×10⁷** invocations exhausted in **~568.8 s** with LRU at cap **8×10⁶**; no certified `min_d` for `d=3`.

## Key finding

**+20%** invocation budget **does not** resolve **`r=5` `d=3`** at **8M** LRU; extra **10M** calls cost **~148 s** wall time vs the **5×10⁷** run — the **50M** cutoff was **not** immediately below a completion threshold.

## Implications

- Next levers: much larger **max-exists-calls**, **unbounded** memo on large-RAM host, **process sharding**, or **algorithmic** change — not marginal +20% scaling.
- Parallels **full-menu** **`r=9` `d=3`** difficulty at **5e7/8M** (also PARTIAL).

## Analogy pass summary

Step-size increase in bounded-memo search; falsified “near-threshold” at +20% budget.

## Space-definition

None.
