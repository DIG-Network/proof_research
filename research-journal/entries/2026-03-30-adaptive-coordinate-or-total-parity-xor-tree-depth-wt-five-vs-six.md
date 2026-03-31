# 2026-03-30 — adaptive-coordinate-or-total-parity-xor-tree-depth-wt-five-vs-six

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-total-parity-xor-tree-depth-wt-five-vs-six/`

**Context:** `verifier-oracle-model` — after **091** **`min_d=3`** with **quad-XOR** **only** **(** **≤4** **bits** **)** **,** **test** **adding** **global** **Hamming** **parity** **⊕_{i=0}^9 x_i** **as** **one** **allowed** **internal** **node** **type.**

**Hypothesis tested:** **`exists_tree(full,1)=True`** **with** **coord** **+** **total** **XOR.**

**Outcome:** **PASS** **`min_d=1`.** **Partition:** **210** **even** **(** **wt=6** **)** **/** **252** **odd** **(** **wt=5** **)** **—** **both** **pure.**

**Key finding:** **Full** **n-bit** **parity** **is** **not** **realizable** **as** **a** **single** **091** **quad** **node** **;** **it** **collapses** **adaptive** **depth** **from** **3** **to** **1** **on** **(10,{5,6}).**

**Implications:**
- **Oracle** **specs** **must** **say** **whether** **an** **n-wide** **XOR** **(** **or** **equivalent** **)** **is** **cheap** **enough** **to** **count** **as** **O(1)** **vs** **bounding** **arity** **per** **probe.**
- **Resolves** **091** **BREAKTHROUGHS** **open** **question** **for** **this** **domain.**

**Analogy pass summary:** **single** **parity-check** **bit** **/** **sufficient** **statistic** **for** **odd-even** **count** **—** **seed:** **global** **syndrome.**
