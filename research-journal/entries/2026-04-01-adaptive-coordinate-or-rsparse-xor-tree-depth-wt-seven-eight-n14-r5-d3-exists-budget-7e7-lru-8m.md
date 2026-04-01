# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-7e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-7e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=5` XOR language, `d=3`-only probe with **7×10⁷** `exists_tree` budget and **8×10⁶** LRU cap (next step after **6×10⁷** remained PARTIAL ~569 s).

## Hypothesis tested

See `hypothesis.md`: **7e7** budget might complete the root `d=3` decision where **6e7** did not.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **7×10⁷** invocations exhausted in **~643.7 s** with LRU at cap **8×10⁶**; no certified non-PARTIAL `min_d` for `d=3`.

## Key finding

**+40%** over the original **5×10⁷** shard (**7e7**) **still** does **not** resolve **`r=5` `d=3`** at **8M** LRU. Extra **10M** calls beyond **6e7** cost **~74 s** (less marginal cost than the **5e7→6e7** step).

## Implications

- Continue **8e7+**, **unbounded**/sharded memo on larger RAM, **algorithmic** change, or pivot to **anonymous-quorum-binding** / other threads.
- Mirror experiment for **`r=9`** at **7e7/8M** still needed for dual **2002** band symmetry.

## Analogy pass summary

Continuation along the same bounded-memo trajectory; falsified “next +10M finishes” for **r=5** at **7e7**.

## Space-definition

None.
