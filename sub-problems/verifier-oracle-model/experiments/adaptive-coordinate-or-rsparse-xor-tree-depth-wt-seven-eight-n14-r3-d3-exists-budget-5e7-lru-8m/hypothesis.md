# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, **`coord + r=3`** XOR, **`d=3`-only** probe with **`5×10⁷`** `exists_tree` budget and **`8×10⁶`** LRU cap: the run completes with a definite `d=3` feasibility bit (**PASS** or certified **False**), not **PARTIAL** at the budget.

**Context:** The **`n=14`** row has dense coverage for **`r∈{4..13}`** at **5e7/8M**, but **`r=3`** (**`C(14,3)=364`**) has not been run at this envelope. Low-**`r`** menus are smaller than the **2002** hard pocket; this pins whether **`r=3`** is easy like **`r=10`** (small menu) or unexpectedly heavy like **`r=4`** (1001 splits, PARTIAL at this envelope).

**Lineage:** Extends **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r4-d3-exists-budget-5e7-lru-8m`** (INCONCLUSIVE / PARTIAL at cap) and contrasts **`…-n14-r5-d3-exists-budget-5e7-lru-8m`** (PARTIAL, 2002).

## Analogy pass (abbrev.)

1. **Abstract structure:** Adaptive AND–OR tree DP over XOR-split menus; menu size **`C(14,r)`** and parity geometry set exploration cost.
2. **Analogous domains:** (i) **Sparse vs dense** combinatorial search — fewer splits can still branch badly; (ii) **Low-rank** regimes in coding — small support does not always mean easy decoding; (iii) **Interpolation** — fill a gap between resolved **`r=2`** (**`d=2`** infeasible shard) and **`r=4`**.
3. **Machinery:** Same parent **`script.py`** as other **`r-single`** wrappers; controlled **`r=3`** at proven **5e7/8M** envelope.
4. **Transfer seed:** If **364** finishes **fast** with **`d=3` True**, low-**`r`** is not uniformly hard; if **PARTIAL**, even tiny menus can saturate bounded DP here (compare **`r=4`**).
