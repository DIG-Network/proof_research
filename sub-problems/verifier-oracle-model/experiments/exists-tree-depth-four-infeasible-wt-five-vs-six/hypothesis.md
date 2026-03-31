# Hypothesis — no depth-4 mixed coord/XOR tree on full wt {5,6} set (n=10)

## Analogy pass

1. **Abstract structure:** **066** **certified** **minimum** **separator** **depth** **5** **for** **mixed** **`x_i`** **/** **`x_i⊕x_j`** **nodes** **on** **the** **462** **masks.** **The** **DP** **/** **search** **in** **066** **established** **existence** **at** **5** **but** **did** **not** **necessarily** **emit** **a** **standalone** **`exists_tree(S,4)`** **check** **on** **the** **full** **`S`.** **We** **want** **a** **direct** **boolean** **certificate** **that** **budget** **4** **is** **insufficient** **(** **same** **`exists_tree`** **recursion** **as** **067** **).**

2. **Where else:**
   - **Lower** **bound** **proofs** **in** **decision** **tree** **complexity** **(** **adversary** **or** **potential** **method** **—** **here** **we** **use** **exhaustive** **memoized** **DP** **).**
   - **Minimum** **Steiner** **depth** **in** **hypergraphs** **—** **threshold** **jump** **at** **a** **critical** **depth.**
   - **Phase** **transitions** **in** **search:** **below** **a** **parameter** **no** **solution;** **at** **or** **above** **solutions** **appear.**

3. **Machinery:** **Memoized** **`exists_tree(S,** **d)`** **from** **067;** **evaluate** **`exists_tree(full,** **4)`** **and** **sanity** **`exists_tree(full,** **5)`.**

4. **Transfer candidate:** **`exists_tree(full,4)** **=** **False`** **⇒** **any** **protocol** **that** **reuses** **this** **feasibility** **predicate** **cannot** **present** **a** **valid** **depth-4** **plan** **on** **this** **domain** **(** **tight** **with** **066** **).**

## Falsifiable claim

**Let** **`full`** **=** **`{** **m** **∈** **`{0,1}^{10}`** **:** **wt(m)** **∈** **`{5,6}`** **}`.** **With** **`exists_tree`** **exactly** **as** **in** **`mixed-coordinate-xor-tree-witness-wt-five-vs-six`:** **`exists_tree(full,** **4)** **=** **False`** **and** **`exists_tree(full,** **5)** **=** **True`.**
