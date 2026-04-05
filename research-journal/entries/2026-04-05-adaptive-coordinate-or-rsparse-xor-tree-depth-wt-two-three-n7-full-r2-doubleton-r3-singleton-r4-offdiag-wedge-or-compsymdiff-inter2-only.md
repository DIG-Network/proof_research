# Experiment entry — 2026-04-05

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-offdiag-wedge-or-compsymdiff-inter2-only`

**Context:** `verifier-oracle-model` — `n=7`, shell `{2,3}`, doubleton `r=3` + singleton `r=4` grid (`22050` cells).

**Hypothesis tested:** On off-diagonal pairs with **`|T_i ∩ T_j| = 2`**, **`min_d = 2`** iff the quartic mask **`Q`** equals the **ordered wedge** **`W`** or the **complement of symmetric difference** **`C = [7] \ (T_i △ T_j)`**.

**Outcome:** **FAIL**

**Key finding:** Among **`7350`** stratum cells, **`420`** have **`min_d=2`** but only **`210`** satisfy **`Q ∈ {W,C}`**. So **half** of depth-2 witnesses in this overlap class escape the proposed two-chart union. Many violations share a fixed quartic index (**`k=34`**, mask **`(3,4,5,6)`**) across varying **`T_j`** with the same doubleton overlap on **`T_i`**. On this grid **`C`** is a **5-set** whenever **`|T_i △ T_j|=2`**, so the **`210`** predicate hits are **wedge-only** in practice; the failure is **not** from mis-identifying **`C`** as a quartic.

**Implications:**

- **`|∩|=2`** alone does **not** reduce **`min_d=2`** to a **two-formula** disjunction in **`(T_i,T_j)`** — the DP certificate depends on **additional** structure (likely **quartic choice / global menu coupling**).
- Next credible moves: **richer atom families** or **admit `k`**, or return to **`|∩|∈{0,1}`** predicates from session planning; alternate track **anonymous-quorum-binding**.

**Analogy pass summary:** Treating depth-2 as **union of two explicit charts** in overlap stratum — falsified by a **2×** excess of witnesses over the union.

**Space definition:** none
