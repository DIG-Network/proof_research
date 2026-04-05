# Journal entry — 2026-04-05

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-offdiag-symdiff-inter01-biconditional`

**Context:** `verifier-oracle-model`

**Hypothesis tested:** On the off-diagonal stratum **`|T_i∩T_j| ∈ {0,1}`** of the **`n=7`**, **`{2,3}`**, **`22050`**-cell grid, **`min_d = 2` ⇔ `Q = T_i ⊕ T_j`**.

**Outcome:** **FAIL**

**Key finding:** The biconditional fails in **three** disjoint ways: **`140`** **`min_d=2`** cells with **`|∩|=0`** ( **`Q`** cannot equal **6-bit** symdiff); **`630`** **`|∩|=1`** **`min_d=2`** cells with **`Q ≠ symdiff`**; **`315`** **`|∩|=1`** cells with **`Q=symdiff`** but **`min_d=3`**. Stratum **`13475`** cells; **`wall_sec≈32`**, **`4M`** LRU.

**Implications:**

- The **`s∈{0,1}`** **symdiff** rule from the **patchwork** template is **not** salvageable as a **standalone** **`min_d=2`** **characterization** — failure is **not** only from **`s=2`**.
- **Off-diagonal** **`min_d=2`** **likely** **requires** **richer** **predicates** **(** **ordering** **,** **DNF** **,** **or** **pivot** **)** **than** **symdiff** **alone**.

**Analogy pass summary:** **Syndrome / XOR** template tested **in** **isolation** **on** **intersection** **stratum** **;** **cardinality** **obstruction** **at** **`s=0`** **predicts** **instant** **failure** **if** **any** **`min_d=2`** **exists** **there** **—** **confirmed** **(** **`140`** **witnesses** **)**.
