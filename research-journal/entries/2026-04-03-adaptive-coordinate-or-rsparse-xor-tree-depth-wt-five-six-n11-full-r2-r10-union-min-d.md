# Experiment entry

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n11-full-r2-r10-union-min-d`

## Context

**Sub-problem:** verifier-oracle-model

## Hypothesis tested

For **`n=11`**, **`{5,6}`**, the full XOR union **`coord + ⋃_{r=2}^{10} XOR_r`** (**2035** splits) has **`min_d=2`**, by continuation from **`n∈{12,13,14}`**.

## Outcome

**PASS**

## Key finding

Union language reports **`coord_plus_union_rs=[2,…,10] total_splits=2035 min_d=2`** with **`dp_sec≈0.008`**; baselines **`coord_only min_d=11`**, **`coord_plus_full_11xor min_d=1`**. The parent **`n=11`** driver was upgraded to match the **`n=12`** CLI (**`--union-rs`**, LRU memo cap, etc.) so the same wrapper pattern applies across **`n`**.

## Implications

- Oracle narrative can cite **`n∈{11,12,13,14}`** jointly for **`min_d=2`** on the full **`r=2..n-1`** XOR union on the majority shells.
- Optional next: port **`n=10`** / **`n=9`** drivers if continuing the ladder.

## Analogy pass summary

Parameter continuation / finite-size scaling: same **`min_d`** across **`n`** with fixed majority-relative shell encoding.

## Space definition

None.
