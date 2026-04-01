# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, **`coord + r=7`** XOR, **`d=3`-only** probe with **`5×10⁷`** `exists_tree` budget and **`8×10⁶`** LRU cap: the run either completes with a definite `d=3` feasibility bit (**PASS** or certified **False**), or exits **PARTIAL** at the budget.

**Context:** **`C(14,7)=3432`** XOR partitions — **strictly between** the **3003** band (**`r=6`/`r=8`**: **PASS** at this envelope) and the **2002** band (**`r=5`/`r=9`**: **PARTIAL**). **`r=7`** was **easy** at **5e6** (~0.4 s); this run tests whether the **larger** **5e7/8M** envelope still **finishes** for the **full** **3432** menu (scaling from the cheap partial probe).

**Lineage:** Extends **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-d3-exists-budget-5e7-lru-8m`** (PASS, 3003 splits) and **`…-n14-r8-d3-exists-budget-5e7-lru-8m`** (PASS, 3003); contrasts **`…-n14-r5-d3-exists-budget-5e7-lru-8m`** / **`…-n14-r9-d3-exists-budget-5e7-lru-8m`** (PARTIAL, 2002).

## Analogy pass (abbrev.)

1. **Abstract structure:** Same AND–OR adaptive tree DP; XOR split menu size **`C(14,r)`** and parity map set the state-graph geometry.
2. **Analogous domains:** (i) **Phase boundaries** — a parameter crosses a band where a search completes vs stalls; (ii) **Critical slowing down** near a transition; (iii) **Interpolation** between two known regimes (3003 vs 2002).
3. **Machinery:** Binomial **`C(14,7)=3432`** as controlled menu size between proven **PASS** (**3003**) and **PARTIAL** (**2002**) at **5e7/8M**.
4. **Transfer seed:** If **3432** **PASS**es like **3003**, **hardness** is **not** monotone in **`|menu|`** in the **2002–3432** window; if **PARTIAL**, **2002** is not the **only** hard cardinality — **intermediate** menus can **saturate** bounded DP too.
