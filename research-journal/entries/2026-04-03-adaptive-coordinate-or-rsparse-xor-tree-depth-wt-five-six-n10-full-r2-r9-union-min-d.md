# Experiment entry

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n10-full-r2-r9-union-min-d`

## Context

**Sub-problem:** verifier-oracle-model

## Hypothesis tested

For **`n=10`**, **`{5,6}`**, the full XOR union **`coord + ⋃_{r=2}^{9} XOR_r`** (**1012** splits) has **`min_d=2`**, by continuation from **`n∈{11,12,13,14}`**.

## Outcome

**PASS**

## Key finding

Union language reports **`coord_plus_union_rs=[2,…,9] total_splits=1012 min_d=2`** with **`dp_sec≈0.003`**; baselines **`coord_only min_d=10`**, **`coord_plus_full_10xor min_d=1`**. The **`n=10`** driver was upgraded to the same CLI as **`n=11`** (**`--union-rs`**, LRU cap, etc.).

## Implications

- Oracle narrative can cite **`n∈{10,11,12,13,14}`** jointly for **`min_d=2`** on the full **`r=2..n-1`** XOR union on the majority shells.
- Optional next: port **`n=9`** driver and repeat full-union **`min_d`**.

## Analogy pass summary

Parameter continuation / finite-size scaling: same **`min_d`** across **`n`** with fixed majority-relative shell encoding.

## Space definition

None.
