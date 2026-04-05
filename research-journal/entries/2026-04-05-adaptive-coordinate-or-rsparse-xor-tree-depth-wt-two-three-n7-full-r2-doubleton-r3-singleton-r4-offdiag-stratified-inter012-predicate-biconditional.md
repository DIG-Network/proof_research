# Experiment entry — 2026-04-05

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-offdiag-stratified-inter012-predicate-biconditional`

**Context:** verifier-oracle-model (`n=7`, `{2,3}` doubleton-triple + singleton-quartic grid)

**Hypothesis tested:** Global off-diagonal biconditional: `min_d=2` iff stratified predicate — `s∈{0,1}`: `Q∈{W_ij,W_ji}`; `s=2`: `Q∈{W_ij,C_ij}`.

**Outcome:** FAIL

**Key finding:** `20825` off-diagonal cells: `1190` have `min_d=2`, predicate hits `980`. Exactly `210` violations, all `min_d=2` with `¬pred`; `0` false positives. Violations are `s=2` cells where `Q=W_ji` but the `s=2` branch omitted `W_ji` (only `W_ij∨C_ij`). Confirms the global gap is the oriented `s=2` chart, not the `s∈{0,1}` law.

**Implications:**
- Next: test `s=2` with **symmetric** wedges plus `C`, e.g. `Q∈{W_ij,W_ji,C_ij}`, or a minimal proven envelope.
- Stratified patching must **carry reverse-wedge** into the `|∩|=2` stratum if `C` alone is used as the third chart.

**Analogy pass summary:** Gluing local classifiers across strata — orientation matters when the local cell geometry breaks symmetry.

**Space definition:** none
