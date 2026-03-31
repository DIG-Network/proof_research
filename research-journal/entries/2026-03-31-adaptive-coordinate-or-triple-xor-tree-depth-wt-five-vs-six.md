# 2026-03-31 — adaptive-coordinate-or-triple-xor-tree-depth-wt-five-vs-six

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-triple-xor-tree-depth-wt-five-vs-six/`

**Context:** `verifier-oracle-model` — adaptive decision-tree depth for separating Hamming shells **wt=5** vs **6** on **n=10**, extending **066** (coord + pair-XOR) with **triple-XOR** nodes.

**Hypothesis tested:** Exhaustive memoized `exists_tree` on the full **462**-mask domain determines minimum depth **d** (or times out).

**Outcome:** **PASS**

**Key finding:** **`min_d = 4`** with mixed coordinate + **x_i ⊕ x_j ⊕ x_k** splits (**120** triples). **Strict improvement** over **066**/**084** (**min_d = 5**). **074**’s global **`exists_tree(full,4)=False`** holds only for the **pair-XOR** gate library; **weight-3** **F₂** parity splits break the **d=4** barrier.

**Implications:**
- **Adaptive** **separator** **complexity** on this toy is **sensitive** to **allowed** **linear** **probe** **arity** — not only **coordinate** vs **pair**.
- **053**/**084** **taxonomy** **of** **2-bit** **gates** **does** **not** **bound** **extensions** **with** **3-bit** **XOR** **splits**.

**Analogy pass summary:** **Coding** **(** **wt-3** **parity** **checks** **),** **group** **testing** **(** **3-way** **XOR** **pools** **),** **richer** **decision-tree** **splits** **—** **seed:** **triple** **parity** **as** **new** **internal** **node** **type.**
