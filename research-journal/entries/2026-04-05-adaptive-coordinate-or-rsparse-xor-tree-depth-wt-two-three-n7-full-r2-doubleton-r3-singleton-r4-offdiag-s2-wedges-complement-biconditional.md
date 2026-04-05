# Journal entry — 2026-04-05

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-offdiag-s2-wedges-complement-biconditional`

**Context:** `verifier-oracle-model` (`n=7`, `{2,3}`, doubleton `r=3` + singleton `r=4`)

**Hypothesis tested:** On off-diagonal cells with **`|T_i ∩ T_j| = 2`**, **`min_d = 2`** iff **`Q ∈ {W(i,j), W(j,i), C(i,j)}`**.

**Outcome:** PASS

**Key finding:** **`C(i,j)`** has **5** elements on this stratum, so it **never** equals a quartic **`Q`**; all **`420`** depth-**`2`** witnesses are **`W_ij`** or **`W_ji`** (**`210`** each). The test is therefore equivalent to **`W_ij ∨ W_ji`**, fixing the **210** **`d2 ∧ ¬pred`** cases from the global stratified rule that used **`W_ij ∨ C_ij`** only on **`s=2`** (journal experiment **163**).

**Implications:**

- The **`s=2`** obstruction in **163** is **exactly** the missing **`W_ji`** disjunct, not a need for **`C`** as a **4-set**.
- Next: glue **`s∈{0,1}`** (**162**) with **`s=2: W∨W_rev`** on the full **20825** off-diagonal grid.

**Analogy pass summary:** Symmetrizing **oriented** wedge labels (both **`W_ij`** and **`W_ji`**) matches **cut reversal** / **DNF completion** patterns — one missing disjunct yields **sound** but **incomplete** predicates.

**Space definition:** none
