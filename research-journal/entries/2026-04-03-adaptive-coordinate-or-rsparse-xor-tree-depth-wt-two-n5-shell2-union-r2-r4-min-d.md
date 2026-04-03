# Experiment: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5-shell2-union-r2-r4-min-d

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5-shell2-union-r2-r4-min-d`  
**Context:** verifier-oracle-model  

## Hypothesis (short)

For `n=5` with **weight-2-only** masks (**10** masks), **coord + XOR union `r=2..4`** (**25** splits) still has **`min_d=1`** — i.e. adding **`r=4`** to the union **without** enlarging the mask shell does **not** reproduce the **`min_d=2`** seen for **`{2,3}` shell + `r=2..4`**.

## Outcome: **PASS**

Parent driver reports **`min_d=1`** for the union language; wrapper exits **0**.

## Key finding

At **`n=5`**, the same **25-split** XOR union menu (**`r=2..4`**) yields **`min_d=1`** on the **10-mask** shell and **`min_d=2`** on the **20-mask** `{2,3}` shell. The depth bump is **not** attributable to **`r=4` splits alone**; it implicates the **weight-3 mask extension** of the alphabet (interaction with the union), sharpening the “shell-dependent” localization of the earlier `n=5` story.

## Implications

- Attribute the **`{2,3}` + `r=2..4`** FAIL primarily to **shell expansion**, not arity-menu width alone.
- Optional follow-up: **`{2,3}`** shell with union **`r=2..3` only** to test whether **weight-3 masks** force **`min_d=2`** even before adding **`r=4`**.

## Analogy pass summary

See `hypothesis.md` (interaction / one-factor-at-a-time ablation; main effect vs interaction in discrete languages).
