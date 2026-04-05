# Journal entry — 2026-04-05

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-offdiag-unified-wedge-pair-all-strata-biconditional`

**Context:** `verifier-oracle-model` (`n=7`, `{2,3}`, doubleton `r=3` + singleton `r=4`)

**Hypothesis tested:** On **all** off-diagonal strata with **`|T_i ∩ T_j| ∈ {0,1,2}`** (**`20825`** cells), **`min_d = 2`** iff **`Q ∈ {W_ij, W_ji}`** (ordered wedge pair only — no **`C_ij`** disjunct).

**Outcome:** PASS

**Key finding:** **`0`** violations on the full off-diagonal union. Counts: **`1190`** depth-**`2`** cells, **`1190`** predicate hits (**`595`** **`W_ij`**, **`595`** **`W_ji`**), **`wall_sec≈30.4`**. This **globally** confirms the glue anticipated after **164**: the **`s=2`** **`C_ij`** term in the formal triple disjunction is **vacuous** for quartics, so **`W_ij ∨ W_ji`** alone matches **`min_d=2`** for every **`s∈{0,1,2}`**.

**Implications:**

- The verifier-facing predicate on this fixed language can be stated **without** stratifying on **`s`** (on off-diagonal pairs).
- Next structural questions: other **`n`**, richer menus, or diagonal **`i=j`** cells (not in this scan).

**Analogy pass summary:** Collapsing piecewise regional certificates when one region’s “extra” disjunct is **empty** on the data type (**`Q`** is always a **4**-set) mirrors **dead-code elimination** / **predicate simplification** in logic.

**Space definition:** none
