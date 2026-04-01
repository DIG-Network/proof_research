# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, **`coord + r=4`** XOR, **`d=3`-only** probe with **`5×10⁷`** `exists_tree` budget and **`8×10⁶`** LRU cap: the run completes with a definite `d=3` feasibility bit (**PASS** or certified **False**), or exits **PARTIAL** at the budget.

**Context:** **`C(14,4)=C(14,10)=1001`** — binomial dual of **`r=10`**. The **`r=10`** shard at this envelope **PASS**ed with **`min_d=3`** in **~55 s** DP. If **`r=4`** behaves similarly, **low-**`r`** small menus** are symmetrically easy; if **PARTIAL**, **complement/duality in `r`** does not preserve DP hardness at fixed split count.

## Analogy pass (abbrev.)

1. **Abstract structure:** Same AND–OR adaptive tree DP; XOR partition menu indexed by **`r`**-subsets; **`C(n,r)=C(n,n−r)`** pairs share cardinality.
2. **Analogous domains:** (i) **Dual codes** in coding theory (same length, swapped roles); (ii) **Complementary hyperplane arrangements**; (iii) **Symmetry reduction** in enumerative combinatorics.
3. **Machinery:** Identical **1001** split count as **`r=10`**; compare wall time and feasibility bit.
4. **Transfer seed:** **Cardinality symmetry** ⇒ expect **qualitatively similar** finish unless **parity / shell interaction** breaks **`r↔n−r`** equivalence for this DP.
