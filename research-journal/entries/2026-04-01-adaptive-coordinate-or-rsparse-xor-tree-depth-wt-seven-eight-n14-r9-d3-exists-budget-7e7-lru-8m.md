# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-7e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-7e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=9` XOR language, `d=3`-only probe with **7×10⁷** `exists_tree` budget and **8×10⁶** LRU cap (mirror of **`r=5`** **7e7** run for the **2002** dual band).

## Hypothesis tested

See `hypothesis.md`: **`r=9`** might complete or show different hardness than **`r=5`** at **7e7/8M**.

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **7×10⁷** invocations exhausted in **~595.3 s** with LRU at cap **8×10⁶**.

## Key finding

Both **`r=5`** and **`r=9`** remain **PARTIAL** at **7e7/8M**; **`r=9`** is **~49 s** faster than **`r=5`** at this envelope (**~595 s** vs **~644 s**).

## Implications

- **2002** full-menu **`d=3`** band still open at **+40%** over **5e7** for **both** dual **`r`** values.
- Next: **8e7+**, **unbounded**/sharded memo, **algorithmic** change, or other research threads.

## Analogy pass summary

Dual-band symmetry test at **7e7**; both sides truncate; **`r=9`** cheaper in wall time.

## Space-definition

None.
