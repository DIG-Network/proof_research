# Experiment entry — 2026-04-04 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-min-r3-splits-for-min-d2

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-min-r3-splits-for-min-d2/`

**Context:** verifier-oracle-model (adaptive coordinate + XOR split-menu depth)

**Hypothesis:** With `n=5`, shell `{2,3}`, and the **full** `r=2` XOR menu fixed, **at least two** `r=3` XOR splits are needed to reach **`min_d=2`** (minimal augment size **≥ 2**).

**Outcome:** **FAIL** (hypothesis falsified)

**Key finding:** **One** triple-XOR split suffices: witness **`r3_indices=[0]`** (**triple `(0,1,2)`** in lex order), giving **`11`** XOR splits total (**`10`** pair + **`1`** triple) and **`min_d=2`**, vs **`min_d=3`** with **no** triple splits. Parent driver gained **`--union-r3-indices`** to restrict the `r=3` sub-menu.

**Implications:**

- Refines the prior “`r=3` load-bearing” read: **some** triple parity is required **relative to pair-only**, but **not** a large **minimal** set of distinct triple splits in this slice.
- Suggests **critical parity** / **generator** viewpoint: one well-chosen **`r=3`** split can substitute for **many** in the separability certificate.

**Analogy pass summary:** Generator minimality vs individual necessity — menu-level “need for `r=3`” does not imply **many** triple splits are each indispensable.

**Space definition:** none
