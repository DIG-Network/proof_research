# Experiment entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-plus-full-r5-r6-r7-offdiag-unified-wedge-pair-all-strata-biconditional`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}` off-diagonal `s∈{0,1,2}`)

**Hypothesis tested:** After the sparse n=8 wedge port was vacuous (`min_d=2` absent), enrich the same cell language with **full** XOR menus for `r=5,r=6,r=7` (known to participate in a global `min_d=2` union on the `{2,3}` shell) and retest `min_d=2 ⇔ Q∈{W_ij,W_ji}`.

**Outcome:** FAIL

**Key finding:** The enrichment makes **`min_d=2` universal** on all **`107800`** stratum cells while the wedge predicate has **`0`** hits (`Q` is always a 4-set; wedges are not). Hence **`107800`** violations of the form `d2 ∧ ¬pred`. Wall clock **`≈37.4s`**, LRU **`4M`**.

**Implications:**

- Restoring depth-2 witnesses by “adding the missing global splits” does **not** revive the n=7 wedge biconditional — it **collapses** the selector role of `Q`.
- The n=8 story is **biphasic**: sparse menu ⇒ empty `min_d=2` stratum (vacuous PASS); strong menu ⇒ full stratum `min_d=2` (sharp FAIL vs wedges).

**Analogy pass summary:** See `hypothesis.md` (sufficient statistics / relevant operators).
