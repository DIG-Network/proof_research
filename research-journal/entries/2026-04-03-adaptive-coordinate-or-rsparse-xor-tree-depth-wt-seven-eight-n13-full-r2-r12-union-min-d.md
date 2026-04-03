# Experiment entry

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n13-full-r2-r12-union-min-d`

## Context

**Sub-problem:** verifier-oracle-model

## Hypothesis tested

For **`n=13`**, **`{7,8}`**, the full XOR union **`coord + ⋃_{r=2}^{12} XOR_r`** (**`8177`** splits) has **`min_d=2`**, paralleling **`n=14`** full **`r=2..13`** union (**`min_d=2`**).

## Outcome

**PASS**

## Key finding

Union language reports **`coord_plus_union_rs=[2,…,12] total_splits=8177 min_d=2`** with **`dp_sec≈0.057`**; baselines **`coord_only min_d=13`**, **`coord_plus_full_13xor min_d=1`**. So **`min_d=2`** for the full multi-arity XOR menu is not **`n=14`-specific** for this majority slice.

## Implications

- Continue **`min_d`** / shell scans at **`n=12`** **`{6,7}`** if we want another step down the **`n`** ladder.
- Oracle narrative can cite **`n=13`** and **`n=14`** together when stating **`min_d=2`** for the full **`r=2..n-1`** union.

## Analogy pass summary

Finite-size scaling / parameter continuation: same **`min_d`** across adjacent **`n`** with fixed majority geometry.

## Space definition

None.
