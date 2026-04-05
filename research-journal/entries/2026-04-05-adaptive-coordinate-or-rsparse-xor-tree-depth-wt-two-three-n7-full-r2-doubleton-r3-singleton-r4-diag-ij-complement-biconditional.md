# Journal entry — 2026-04-05

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-diag-ij-complement-biconditional`

**Context:** `verifier-oracle-model` (`n=7`, `{2,3}`, doubleton `r=3` + singleton `r=4`, **diagonal** `i=j`)

**Hypothesis tested:** On all **`1225`** diagonal cells (duplicate triple **`T_i`** twice), **`min_d = 2`** iff **`Q`** is the **complement** of **`T_i`** in **`[7]`**.

**Outcome:** PASS

**Key finding:** **`0`** violations; **`35`** depth-**`2`** cells and **`35`** complement hits; **`wall_sec≈1.68`**. Matches the singleton-triple + singleton-quartic complement law — repeating the same **`r=3`** split does not create new **`min_d=2`** certificates on the diagonal.

**Implications:**

- Diagonal slice is **decoupled** from the off-diagonal wedge classification (exp. 165); any global predicate for the full **`22050`** grid must **piecewise** combine complement (diag) vs wedge pair (off-diag).
- Cross-**`n`** checks remain the next stress test for generality.

**Analogy pass summary:** Diagonal of a product space as a **fixed locus** where a simpler **boundary** law (complement) holds, while the interior (off-diagonal) needs richer charts (wedges).

**Space definition:** none
