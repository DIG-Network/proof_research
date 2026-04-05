# Experiment entry — 2026-04-05

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-offdiag-wedge-or-reversewedge-inter01-biconditional`

**Context:** verifier-oracle-model (`n=7`, `{2,3}` doubleton-triple + singleton-quartic grid)

**Hypothesis tested:** On off-diagonal stratum `|T_i∩T_j|∈{0,1}`, `min_d=2` iff `Q ∈ {W(i,j), W(j,i)}` for ordered wedges `W(a,b)=(T_a\T_b)∪([7]\(T_a∪T_b))`.

**Outcome:** PASS

**Key finding:** Exhaustive `13475` stratum cells: `770` have `min_d=2`, exactly `770` satisfy the disjunction; `385` use `W_ij`, `385` use `W_ji`, never both (`pred_both=0`). Zero violations either way. Symmetrizing the ordered wedge fixes the incompleteness of experiment 161.

**Implications:**
- The `|∩|∈{0,1}` slice admits a clean **two-chart** certificate for depth `2` (either orientation).
- Suggests pursuing a **unified stratified** rule across `|∩|∈{0,1,2}` next, or documenting this law and pivoting per digest.

**Analogy pass summary:** Symmetric closure / union of directed acceptance regions; minimal symmetric envelope of a sound one-way predicate.

**Space definition:** none
