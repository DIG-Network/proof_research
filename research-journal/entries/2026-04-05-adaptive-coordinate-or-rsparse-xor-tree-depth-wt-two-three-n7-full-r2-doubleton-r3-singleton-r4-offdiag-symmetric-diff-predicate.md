# Experiment entry — 2026-04-05

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-doubleton-r3-singleton-r4-offdiag-symmetric-diff-predicate`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`, adaptive coordinate + XOR-tree DP)

**Hypothesis tested:** Off-diagonal `min_d=2` cells in the `coord + full r=2 + doubleton r=3 + singleton r=4` grid might satisfy a **set law** `|T_i∩T_j|=1` and `Q = T_i △ T_j`, extending the singleton complement story.

**Outcome:** FAIL (hypothesis falsified)

**Key finding:** Full **`22050`**-cell scan (**`wall_sec≈31.3`**) reproduced **`1225`** depth-2 cells. The symmetric-difference predicate fails **both ways:** many **`min_d=2`** witnesses have **`|T_i∩T_j|=2`** or have **`Q ≠ T_i△T_j`** when `|∩|=1`; and **`315`** cells satisfy `|∩|=1` and `Q=T_i△T_j` yet have **`min_d=3`**. So **`Q=T_i△T_j`** is neither necessary nor sufficient.

**Implications:**

- Any closed classification of the **`1190`** off-diagonal witnesses must allow **`|T_i∩T_j|∈{1,2}`** and cannot be a single symmetric set formula without case-splitting (lex order `(i,j)` may matter).
- Next: test **ordered** patchwork templates (e.g. `(T_i \ T_j) ∪ ([7]\(T_i∪T_j))` for `|∩|=2`) or search for a short disjunction exact classifier.

**Analogy pass summary:** Parity/syndrome intuition suggests XOR-of-supports; DP feasibility is **not** equivalent to a single quartic label matching that XOR.

**Space-definition:** none
