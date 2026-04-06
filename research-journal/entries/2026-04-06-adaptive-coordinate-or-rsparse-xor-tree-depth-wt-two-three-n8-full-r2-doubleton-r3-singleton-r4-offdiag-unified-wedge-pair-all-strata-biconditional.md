# Journal entry — 2026-04-06

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-offdiag-unified-wedge-pair-all-strata-biconditional`

**Context:** `verifier-oracle-model` (`n=8`, `{2,3}`, doubleton `r=3` + singleton `r=4`)

**Hypothesis tested:** Port of n=7 **165**: on all off-diagonal strata **`|T_i ∩ T_j| ∈ {0,1,2}`** (**`107800`** cells), **`min_d = 2`** iff **`Q ∈ {W_ij, W_ji}`**.

**Outcome:** PASS (vacuous)

**Key finding:** **`stratum_min_d2=0`**, **`stratum_pred=0`**, **`0`** violations. The biconditional holds because **no** cell in the stratum satisfies either side: this menu at n=8 never reaches depth 2 on the scanned off-diagonal slice, and quartics never equal a wedge mask. Unlike n=7 (**`1190`** genuine matches), this adds **no** new verifier-facing certificate—only confirms **strong n-dependence** of the depth-2 phenomenon.

**Implications:**

- Extend the **n=8** language (extra XOR splits / arities) before expecting wedge-shaped certificates analogous to n=7.
- Treat “PASS” scripts as requiring **non-empty positive class** when claiming structural laws.

**Analogy pass summary:** Finite-size scaling: a certificate that is tight at one `n` can disappear (empty regime) at another without contradicting logic—only the **support** of the law moves.

**Space definition:** none
