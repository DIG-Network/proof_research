# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-6e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-6e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=9` XOR language, `d=3`-only probe with **6×10⁷** `exists_tree` budget and **8×10⁶** LRU cap — **mirror** of the **`r=5`** **6e7** run (**C(14,9)=C(14,5)=2002**).

## Hypothesis tested

See `hypothesis.md`: whether **`r=9`** behaves like **`r=5`** under the same +20% budget over **5e7/8M** (PARTIAL vs completion).

## Outcome

**INCONCLUSIVE** — parent exit **2** (PARTIAL); **6×10⁷** invocations exhausted in **~562.3 s** DP with LRU at cap **8×10⁶**; no certified `min_d` for `d=3`.

## Key finding

**+20%** budget **does not** close **`r=9` `d=3`** at **8M** LRU, matching **`r=5`** at **6e7/8M**. The **2002** band stays **structurally open** for **both** dual **`r`** values — **r↔n−r** does **not** rescue **`d=3`** completion at this envelope.

## Implications

- Same next levers as **`r=5`**: much larger **`max-exists-calls`**, **unbounded** memo on high-RAM host, **sharding**, or **algorithmic** change.
- Strengthens the view that **+20%** scaling is **not** a near-threshold fix for the hard **2002** **`d=3`** pair.

## Analogy pass summary

Dual-coordinate stress test on the same 2002 menu; symmetric **PARTIAL** outcome.

## Space-definition

None.
