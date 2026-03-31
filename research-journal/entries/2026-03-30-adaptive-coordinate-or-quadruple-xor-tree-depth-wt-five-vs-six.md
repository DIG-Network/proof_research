# 2026-03-30 — adaptive-coordinate-or-quadruple-xor-tree-depth-wt-five-vs-six

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-quadruple-xor-tree-depth-wt-five-vs-six/`

**Context:** `verifier-oracle-model` — adaptive depth for **wt=5** vs **6** on **n=10**, extending **090** (coord + triple-XOR, **`min_d=4`**) with **quadruple-XOR** nodes.

**Hypothesis tested:** **`exists_tree`** with **coord + all 4-XOR** splits yields **`min_d ∈ {3,4}`**.

**Outcome:** **PASS** (**`min_d=3`** — **strict** improvement over **090**).

**Key finding:** **d=1,2** false; **d=3** true **(~0.39 s).** **Arity** **ladder** **on** **this** **fixed** **instance:** **pair-XOR** **5** **→** **triple** **4** **→** **quad** **3.**

**Implications:**
- **Verifier-oracle** **toy:** **allowed** **F₂** **parity** **arity** **at** **one** **node** **is** **a** **sharp** **knob** **for** **separator** **depth** **—** **not** **saturated** **at** **triple.**
- **090** **/** **074** **narratives** **should** **cite** **gate** **library** **explicitly** **when** **stating** **minimal** **depth.**

**Analogy pass summary:** **LDPC** **/** **hyperplane** **arrangements** **/** **decision-tree** **richness** **—** **seed:** **weight-4** **parity** **splits.**
