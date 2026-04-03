# Experiment entry

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5-full-r2-r3-union-min-d`

## Context

**Sub-problem:** verifier-oracle-model

## Hypothesis tested

For **`n=5`**, **`{2}`** (**`10`** masks), the full XOR union **`coord + ⋃_{r=2}^{3} XOR_r`** (**`20`** splits) has **`min_d=2`**, by continuation from **`n∈{6,…,14}`**.

## Outcome

**FAIL**

## Key finding

Union language reports **`min_d=1`** (same as **`coord_only`** and **`coord_plus_full_5xor`**); the **`min_d=2`** certificate **does not** extend to **`n=5`** on this shell. Wrapper exits **`1`** when union **`min_d≠2`**.

## Implications

- Oracle narrative should **not** cite **`n≥5`** for the same **`min_d=2`** full-union fact; **`n=6`** is the **lower** end of that ladder for this pattern.
- Optional: probe **`n=5`** with a **different** mask shell if a separate certificate is needed.

## Analogy pass summary

Finite-size boundary: small domain collapses the **`min_d=2`** phenomenon seen from **`n=6`** upward.

## Space definition

None.
