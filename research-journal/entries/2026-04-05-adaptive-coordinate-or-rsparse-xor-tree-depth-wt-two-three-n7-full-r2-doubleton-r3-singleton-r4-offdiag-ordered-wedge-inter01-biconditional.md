# Journal entry — 2026-04-05

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-offdiag-ordered-wedge-inter01-biconditional`

**Context:** `verifier-oracle-model`

**Hypothesis tested:** On **`i<j`** with **`|T_i∩T_j|∈{0,1}`**, **`min_d=2` ⇔ `Q = W_{i,j}`** where **`W=(T_i\T_j)∪([7]\(T_i∪T_j))`** (ordered wedge using the first triple).

**Outcome:** **FAIL**

**Key finding:** **385** **`min_d=2`** cells have **`Q≠W`** (half of the **770** stratum depth-**2** witnesses); **`wedge_not_d2=0`** — **`Q=W`** never appears with **`min_d≠2`** on this stratum. **`wall_sec≈30.5`**, **`4M`** LRU.

**Implications:**

- **Ordered wedge** is a **strict** improvement over **symmetric diff** as a **one-way** predicate (**no** false positives here), but it is **not** a **biconditional** — **off-diagonal** **`min_d=2`** **still** **splits** **across** **many** **`Q`** **patterns**.
- **Next** **candidates:** **disjunction** **of** **two** **wedges** **`W(i,j)∪W(j,i)`**, **union** **with** **symdiff** **/** **complement** **charts**, **or** **explicit** **small** **DNF** **search**.

**Analogy pass summary:** **Oriented** **cut** **/** **flag** **order** **—** **tested** **whether** **breaking** **triple** **symmetry** **yields** **a** **single** **`Q`** **template** **;** **partial** **success** **(** **sound** **half** **)** **only**.
