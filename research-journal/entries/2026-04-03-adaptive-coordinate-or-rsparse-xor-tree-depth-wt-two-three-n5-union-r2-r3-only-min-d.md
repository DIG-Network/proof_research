# Experiment: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-union-r2-r3-only-min-d

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-union-r2-r3-only-min-d`  
**Context:** verifier-oracle-model  

## Hypothesis (short)

For `n=5` with **`{2,3}`** shell (**20** masks), **`coord + XOR_2 ∪ XOR_3`** only (**20** splits, no **`r=4`**) still has **`min_d=2`**.

## Outcome: **PASS**

Parent reports **`min_d=2`**; wrapper exits **0**.

## Key finding

**`r=4`** XOR splits are **not** required for the **`min_d=2`** certificate on this shell: **weight-3 masks** plus **binary and ternary** XOR parity tests alone force depth **2**. This refines the post-`shell2-union-r2-r4` narrative: the depth bump is **not** “`r=4` interacting with weight-3” but **weight-3 masks with the smaller arity menu**.

## Implications

- Cite **`{2,3}` + `r=2..3` only** when explaining **minimal** menu for **`n=5`** **`min_d=2`**.
- The **`25`-split** **`r=2..4`** union on **`{2,3}`** is **redundant** for this particular depth fact (though it may matter for other statistics).

## Analogy pass summary

See `hypothesis.md` (factorial ablation / matched split-count design).
