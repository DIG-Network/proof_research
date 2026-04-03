# Experiment entry

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12-full-r2-r11-union-min-d`

## Context

**Sub-problem:** verifier-oracle-model

## Hypothesis tested

For **`n=12`**, **`{6,7}`**, the full XOR union **`coord + ⋃_{r=2}^{11} XOR_r`** (**`4082`** splits) has **`min_d=2`**, paralleling **`n=13`** and **`n=14`**.

## Outcome

**PASS**

## Key finding

Union language reports **`coord_plus_union_rs=[2,…,11] total_splits=4082 min_d=2`** with **`dp_sec≈0.024`**; baselines **`coord_only min_d=12`**, **`coord_plus_full_12xor min_d=1`**. So **`min_d=2`** for the full multi-arity XOR menu extends one more step down the **`n`** ladder.

## Implications

- Optional next run: **`n=11`** **`{5,6}`** full union if we want a minimal-`n` anchor for the same statement.
- Oracle narrative can cite **`n∈{12,13,14}`** jointly for **`min_d=2`** on the full **`r=2..n-1`** union.

## Analogy pass summary

Parameter continuation / finite-size scaling: same **`min_d`** across adjacent **`n`** with fixed majority-relative shell geometry.

## Space definition

None.
