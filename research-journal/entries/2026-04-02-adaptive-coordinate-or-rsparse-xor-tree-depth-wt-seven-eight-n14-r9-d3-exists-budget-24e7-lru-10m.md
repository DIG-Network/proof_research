# Journal entry

**Date:** 2026-04-02  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-24e7-lru-10m`  
**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `r=9`, `d=3` band)

## Hypothesis tested

**+33%** **`exists_tree`** cap (**18e7 → 24e7**) at **10M** LRU on the full **`r=9`** XOR menu (**2002** splits) might complete the **`d=3`** probe (session extrapolation **~45 min** class).

## Outcome

**INCONCLUSIVE** — **PARTIAL** at **240000000** **`exists_tree`** calls; **~2118.20 s** DP (**~35.3 min** wall); LRU **10M** saturated; **no** certified full-menu **`d=3`** verdict.

## Key finding

**+6×10⁷** calls over **18e7/10M** added **~473.6 s** — full **2002** menu remains **unfinished** at **24e7**; **`d=3 feasible=False`** in the log is **budget-truncated**, not sound for **`min_d>3`**. Wall came in **below** naive linear extrapolation from **18e7**.

## Implications

- **Dual 2002** band still **open** for a **complete** **`d=3`** answer without **>24e7** budget, **>10M** LRU, or **DP** innovation.
- Pair **`r=5` `24e7/10M`** to test whether complement symmetry shifts wall time like at **18e7** (**~9%** faster **`r=5`**).

## Analogy pass summary

Same **bounded-work-unit** extension as **`r=9` 18e7** parent; this run is the **largest completed full-menu** **`r=9`** **`d=3`** shard at **10M** LRU in the journal to date (**24e7**).
