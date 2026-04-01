# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=5` XOR language, `d=3`-only probe with **5×10⁷** `exists_tree` budget and **8×10⁶** LRU cap.

## Hypothesis tested

See `hypothesis.md`: scale up invocation budget and LRU to move past the **5×10⁶** partial plateau or obtain a definite `d=3` bit.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **5×10⁷** invocations exhausted in **~420.6 s** with LRU at cap **8×10⁶**; no certified `min_d` for `d=3`.

## Key finding

**10×** the **5×10⁶** budget is still insufficient for this shard under bounded LRU; effective rate ~**1.2×10⁵** inv/s in the long run (vs ~7.7×10⁴ on the shorter 5e6 probe).

## Implications

- Keep **`r=5`/`r=6` `d=3`** as **open**; mirror this **(5e7, LRU 8M)** probe for **`r=6`**.
- Unbounded memo / sharding / algorithmic change remain the paths to a **definite** bit.

## Analogy pass summary

Resource scaling for memoized game-tree search; invocation count as portable progress metric.

## Space-definition

None.
