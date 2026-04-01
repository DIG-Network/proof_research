# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r11-d3-exists-budget-2e7

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r11-d3-exists-budget-2e7/`

## Context

verifier-oracle-model — **`n=14`**, **`{7,8}`**, **`r=11`**, **`d=3`-only**, **`--max-exists-calls 2×10⁷`** (follow-up to **`r=11`** **PARTIAL** at **5×10⁶** in **`…-r11-r12-r13-d3-exists-budget-5e6`**).

## Hypothesis tested

**More** **`exists_tree`** budget would allow **`d=3`** **feasible=True** for **`r=11`**.

## Outcome

**FAIL** (hypothesis falsified).

## Key finding

**`d=3`** probe **finished** with **`feasible=False`**; **~8.29×10⁶** distinct **`exists_tree`** states (**<< 2×10⁷**). So **`r=11`** **PARTIAL** at **5e6** was **incomplete search** on an **infeasible** **`d=3`** instance, **not** “ **`d=3`** **yes** **blocked** **by** **cap** **.”** **`min_d≥4`** for **coord+11xor** on this slice — distinct from **`r∈{5,6,8,9,10}`** where **`d=3`** may still be **open** / **budget**-limited.

## Implications

- **Narrative** for **`r=11`**: classify as **depth** **barrier** (**`d≥4`**), not only **split-count** / **memo** **pressure**.
- **Next:** **`r=11`** **`d=4`-only** probe (separate experiment) if **`min_d(11)`** is needed; **`r=5,6`** **`d=3`** remains the other **priority** **hard** **region**.

## Analogy pass summary

**Resource scaling** vs **decision** **boundary** — **more** **compute** **does** **not** **flip** **infeasible** **to** **feasible** **.**

## Space-definition

None.
