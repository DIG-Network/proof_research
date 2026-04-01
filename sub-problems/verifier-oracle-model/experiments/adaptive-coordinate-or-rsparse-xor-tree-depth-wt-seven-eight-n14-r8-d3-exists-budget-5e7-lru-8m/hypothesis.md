# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, **`coord + r=8`** XOR, **`d=3`-only** probe with **`5×10⁷`** `exists_tree` budget and **`8×10⁶`** LRU cap: the run either (a) completes with a definite `d=3` feasibility bit (**PASS** or certified **False**), or (b) exits **PARTIAL** at the budget.

**Context:** **`C(14,8)=C(14,6)=3003`** XOR partitions — **same menu cardinality as `r=6`**, which **PASS**es **`min_d=3`** in ~**435 s** at this envelope, while **`r=5`** and **`r=9`** (each **2002** splits) **PARTIAL** at **5e7/8M**. This experiment tests whether **split count** or **parity pattern** dominates: if **`r=8`** **PASS**es like **`r=6`**, count matters; if it **PARTIAL**s like **`r=5`/`r=9`**, the **XOR functional** dominates.

## Analogy pass (abbrev.)

1. **Abstract structure:** Same AND–OR adaptive tree DP; only the **r-sparse XOR split menu** changes.
2. **Analogous domains:** (i) **Isomorphic sample sizes** in A/B testing with **different treatment maps**; (ii) **Same graph size, different edge law** in percolation; (iii) **Dual codes** with identical length/dimension but different minimum distance.
3. **Machinery:** Binomial symmetry **`C(n,k)=C(n,n−k)`** pairs **`(6,8)`** and **`(5,9)`** on **`n=14`**.
4. **Transfer seed:** **`(r=6,r=8)`** dual pair at **3003** splits vs **`(r=5,r=9)`** at **2002** — compare bounded-DP outcomes to separate **cardinality** from **parity geometry**.
