# Journal entry — 2026-04-05

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-full-r2-doubleton-r3-singleton-r4-offdiag-unified-wedge-pair-all-strata-biconditional`

**Context:** `verifier-oracle-model` (`n=6`, `{2,3}`, doubleton `r=3` + singleton `r=4` — port of n=7 experiment **165**)

**Hypothesis tested:** On all off-diagonal strata with **`|T_i ∩ T_j| ∈ {0,1,2}`** (**`2850`** cells), **`min_d = 2`** iff **`Q ∈ {W_ij, W_ji}`** (ordered wedge pair only).

**Outcome:** FAIL

**Key finding:** **`2850`** violations **`d2 ∧ ¬pred`**, **`0`** **`pred ∧ md≠2`**. On this stratum **`min_d=2` holds for every cell** (**`2850/2850`**), but **`W_ij` and `W_ji` are always 3-sets** (never 4), so **no quartic `Q` can equal a wedge** — the n=7 quartic-wedge certificate is **not portable** to **`n=6`**. Wall **`≈0.77s`**, **`4M`** LRU.

**Implications:**

- Verifier-facing closed forms may need **explicit `n`-dependent** typing (3-set vs 4-set geometry).
- Next: seek an **`n=6`**-appropriate certificate for **`min_d=2`** (or a richer menu where depth-2 is not universal), or port to **`n=8`**.

**Analogy pass summary:** Same as hypothesis file: predicate minimization / Boolean lattice wedges; failure is a **type error**: the n=7 predicate asks a 4-set question where the wedge object lives in 3-set space at **`n=6`**.

**Space definition:** none
