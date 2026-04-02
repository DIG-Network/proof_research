# Journal entry

**Date:** 2026-04-02  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-18e7-lru-10m`  
**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `r=9`, `d=3` band)

## Hypothesis tested

**~1.5×** **`exists_tree`** cap (**12e7 → 18e7**) at **10M** LRU on the **full** **`r=9`** XOR menu (**2002** splits) might complete the **`d=3`** probe (session guidance: prefer **≥~2×** budget step over small half-shard tweaks).

## Outcome

**INCONCLUSIVE** — **PARTIAL** at **180000000** **`exists_tree`** calls; **~1644.56 s** DP (**~27.4 min** wall); LRU **10M** saturated; **no** certified full-menu **`d=3`** verdict.

## Key finding

**+6×10⁷** calls over **12e7/10M** added **~679 s** — full **2002** menu remains **unfinished** at **18e7**; **`d=3 feasible=False`** in the log is **budget-truncated**, not a proof **`min_d>3`**.

## Implications

- **Dual 2002** band still **open** for a **complete** **`d=3`** answer without **DP**/**ordering** innovation, **>10M** LRU (if memory allows), or **>18e7** budget on a patient host.
- Marginal **~11 µs**/extra call at LRU cap helps extrapolate **24e7**/**30e7** wall (**rough** linearity assumption).

## Analogy pass summary

Same **bounded-work-unit** extension as prior **`r=9`** budget ladder; this run is the **largest completed full-menu** **`r=9`** **`d=3`** shard at **10M** LRU in the journal to date.
