# Experiment entry

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-r5-union-min-d`

## Context

**Sub-problem:** verifier-oracle-model

## Hypothesis tested

For **`n=7`**, **`{2,3}`**, the full XOR union **`coord + ⋃_{r=2}^{5} XOR_r`** (**112** splits) has **`min_d=2`**, by continuation from **`n∈{8,…,14}`**.

## Outcome

**PASS**

## Key finding

Union language reports **`coord_plus_union_rs=[2,…,5] total_splits=112 min_d=2`** with **`dp_sec≈0.001`**; baselines **`coord_only min_d=7`**, **`coord_plus_full_7xor min_d=1`**.

## Implications

- Oracle narrative can cite **`n∈{7,8,9,10,11,12,13,14}`** jointly for **`min_d=2`** on the full **`r=2..n-1`** XOR union on the majority-adjacent shells.
- Optional next: **`n=6`** **`{2,3}`** port if the ladder should extend further down.

## Analogy pass summary

Parameter continuation / finite-size scaling: same **`min_d`** one step smaller.

## Space definition

None.
