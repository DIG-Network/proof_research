# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, **`coord + r=10`** XOR, **`d=3`-only** probe with **`5×10⁷`** `exists_tree` budget and **`8×10⁶`** LRU cap: the run either completes with a definite `d=3` feasibility bit (**PASS** or certified **False**), or exits **PARTIAL** at the budget.

**Context:** **`C(14,10)=C(14,4)=1001`** XOR partitions — **strictly smaller** than the **2002** band (`r=5,9`) and **3003** band (`r=6,8`). Prior **5e6** budget: **`r=10`** was **PARTIAL** alongside **`r=8,9`** (see `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r8-r9-r10-d3-exists-budget-5e6`). At **5e7/8M**, **`r=6`/`r=8`** (**3003**) **PASS**; **`r=5`/`r=9`** (**2002**) **PARTIAL**. This experiment tests whether **smaller menus** (**1001**) finish **easily** (fewer splits) or stay **hard** (parity geometry).

## Analogy pass (abbrev.)

1. **Abstract structure:** Same AND–OR adaptive tree DP; XOR split menu size and parity map vary with **`r`**.
2. **Analogous domains:** (i) **Smaller basis, harder representation** in coding theory; (ii) **Fewer hyperplanes** in arrangement complexity; (iii) **Coarser partitions** in decision-tree learning.
3. **Machinery:** Binomial **`C(14,10)=1001`** vs **`C(14,5)=2002`** vs **`C(14,6)=3003`** as controlled **menu cardinalities**.
4. **Transfer seed:** If **1001** splits **PASS** quickly, **cardinality** alone does not explain hardness; if **PARTIAL**, **small menus** can still **saturate** bounded DP.
