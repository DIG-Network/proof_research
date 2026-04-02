# Journal entry

**Date:** 2026-04-02  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-15e7-each-lru-10m`  
**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `r=9`, `d=3` band)

## Hypothesis tested

Raising **both** `exists_tree` budget (**12e7 → 15e7**) and LRU (**8M → 10M**) on **`r=9`** contiguous XOR half-shards might allow at least one half to **finish** without PARTIAL and yield a definite `d=3` status or a **`feasible=True`** witness.

## Outcome

**INCONCLUSIVE** — both halves hit **`max_exists_calls=150000000`** with **LRU currsize=10M** (**~1167** s and **~1118** s DP); **no** `d=3` witness. **~38** min total sequential wall time.

## Key finding

A **+25%** visit cap **on top of** **10M** LRU does **not** escape the PARTIAL barrier for **`r=9`** half-shards; marginal scaling matches **longer** runs, not a phase transition to completion.

## Implications

- Next increments need **larger** step changes (budget **and/or** memory) or **algorithmic** changes—not another small coset tweak.
- **`r=5`** mirror at **15e7/10M** halves is **optional** for symmetry; **`r=9`** already shows the envelope is tight.

## Analogy pass summary

Search-tree resolution vs **working-set** width: widening both still left the frontier **unfinished**—consistent with **superlinear** effective work per extra million calls once the LRU is saturated.
