# Journal entry

**Date:** 2026-04-02  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-18e7-lru-10m`  
**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `r=5`, `d=3` band)

## Hypothesis tested

**`r=5`** **mirror** of **`r=9`** **`18e7/10M`** **full** **2002** **XOR** **menu** **`d=3`-only** — test **complement-size** **symmetry** **wall** **time** **and** **completion** **vs** **`r=9`** **~1644** **s** **PARTIAL**.

## Outcome

**INCONCLUSIVE** — **PARTIAL** at **180000000** **`exists_tree`** calls; **~1492.22 s** DP (**~24.9 min** wall); LRU **10M** saturated; **no** certified full-menu **`d=3`** verdict.

## Key finding

**`r=5`** **~9.3%** **faster** **than** **`r=9`** **at** **same** **18e7/10M** **envelope** **despite** **identical** **`C(14,5)=C(14,9)=2002`** — **split** **count** **duality** **≠** **DP** **time** **duality** **here**.

## Implications

- **Dual** **2002** **still** **open**; **next** **large** **budget** **step** **(`r=9`** **`24e7/10M`**) **or** **structural** **memo** **change** **preferred** **over** **small** **half-shard** **tweaks**.
- **`r=5`** **not** **harder** **than** **`r=9`** **at** **this** **cap** — **extrapolations** **from** **`r=9`** **marginal** **µs**/call **may** **overestimate** **`r=5`** **wall** **slightly**.

## Analogy pass summary

**Complement** **symmetry** **in** **search** **—** **same** **budget** **ladder** **as** **`r=9`** **18e7** **with** **`--r-single`** **5**.
