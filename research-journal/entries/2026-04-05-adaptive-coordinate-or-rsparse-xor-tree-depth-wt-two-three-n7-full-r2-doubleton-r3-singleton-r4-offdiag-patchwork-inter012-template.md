# Experiment entry — 2026-04-05

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-offdiag-patchwork-inter012-template`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`, adaptive coordinate + XOR-tree DP)

**Hypothesis tested:** Off-diagonal **`min_d=2`** might satisfy a **patchwork** by **`s=|T_i∩T_j|`**: use **`Q=T_i△T_j`** when **`s∈{0,1}`** and **`Q=(T_i\T_j)∪([7]\(T_i∪T_j))`** when **`s=2`**, with diagonal **`Q=[7]\T_i`**.

**Outcome:** FAIL

**Key finding:** Full **`22050`**-cell run (**`wall_sec≈30.5`**) reproduced **`1225`** depth-**`2`** cells. Only **`525`** off-diagonal cells match the patchwork mask predicate (**vs** **`1190`** true **`min_d=2`** off-diagonal witnesses). **Both directions fail:** many **patchwork-true** cells have **`min_d=3`**; many **`min_d=2`** witnesses violate the template — including **`|∩|=2`** cases where **`Q`** appears to track **`complement(T_i△T_j)`** rather than the ordered wedge.

**Implications:**

- **`(T_i,T_j,s)`** alone does **not** determine the **quartic** label at **`min_d=2`**; any closed classifier likely needs **finer invariants** or a **disjunction** of competing **`|∩|=2`** templates (e.g. wedge **vs** complement-symdiff).
- Mask-equality “charts” can be **sound** only if tied to **DP feasibility**, not **pure set geometry**.

**Analogy pass summary:** Stratified sufficient-statistic thinking suggests **case splits**; this experiment shows the **strata are still too coarse** for a **two-line** formula.

**Space-definition:** none
