# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r8-r9-r10-d3-exists-budget-5e6

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r8-r9-r10-d3-exists-budget-5e6/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, **5×10⁶** `exists_tree` budget, `d=3`-only, **`r∈{8,9,10}`** (spot check after **`r=7`** easy band).

## Hypothesis tested

**`r=8,9,10`** each **PARTIAL** (exit 2) like **`r=5,6`**, not quick certification like **`r=7`**.

## Outcome

**PASS** — all three legs exit **2**; LRU **≈5×10⁶**; **`min_d=None`** in parent summary.

## Key finding

**`r=7`** is an **isolated easy window** at this budget: **`r=8`** re-enters the **heavy partial** class despite **more** splits than **`r=7`**; **`r=9,10`** also **saturate** the **5×10⁶** budget in **~31–35 s** DP time.

## Implications

- **`min_d(r)`** / bounded-budget **tractability** over **`r`** is **not** explained by a simple “interior `r` hard, high `r` easy” rule.
- **`r=5,6`** **`d=3`** resolution remains the **priority** hard region; **`r=9`** long-run **`d=3`** is separate from this **fixed-budget** classification.

## Analogy pass summary

Parameterized barrier heights: **neighboring** **`r`** can fall in **different** computational phases.

## Space-definition

None.
