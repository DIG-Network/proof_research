# Experiment entry

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-full-r2-r4-union-min-d`

## Context

**Sub-problem:** verifier-oracle-model

## Hypothesis tested

For **`n=6`**, **`{2,3}`** (**`35`** masks), the full XOR union **`coord + ⋃_{r=2}^{4} XOR_r`** (**`50`** splits) has **`min_d=2`**, by continuation from **`n∈{7,…,14}`**.

## Outcome

**PASS**

## Key finding

Union language reports **`coord_plus_union_rs=[2,…,4] total_splits=50 min_d=2`** with sub-millisecond **`dp_sec`**; baselines **`coord_only min_d=6`**, **`coord_plus_full_6xor min_d=1`**.

## Implications

- Oracle narrative can cite **`n∈{6,…,14}`** jointly for **`min_d=2`** on **`coord + ⋃_{r=2}^{n-2} XOR_r`** for the **`{2,3}`** / majority-adjacent shell pattern at **`n=6`**.
- Optional next: **`n=5`** **`{2}`** only (**`10`** masks), **`r=2..3`**, if the ladder should extend further.

## Analogy pass summary

Parameter continuation / finite-size scaling: same **`min_d`** one step smaller.

## Space definition

None.
