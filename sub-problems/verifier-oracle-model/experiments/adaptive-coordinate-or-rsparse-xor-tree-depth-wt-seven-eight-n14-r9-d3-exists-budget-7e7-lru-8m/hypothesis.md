# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** **`r=9`** shares **`C(14,9)=2002`** XOR splits with **`r=5`**. **`r=5`** at **7e7/8M** remained **PARTIAL** ~644 s. **`r=9`** at **6e7/8M** was **PARTIAL** ~562 s. We apply **7e7** to **`r=9`** to compare termination and wall time at the same budget envelope.

2. **Analogous domains:** (a) Dual coordinates on the same combinatorial object. (b) Symmetric roles in a search graph with different heuristic costs. (c) Chiral partners in a physical model — same state space, different dynamics.

3. **Machinery:** Same parent DP, **`--r-single 9`**, **`7e7`**, **8M** LRU.

4. **Transfer seed:** If **`r=9`** finishes while **`r=5`** does not at **7e7**, **`r↔n−r`** does not preserve hardness here (already seen for **`r=4` vs `r=10`** at other budgets). If both **PARTIAL**, the **2002** band is stable under **7e7/8M**.

## Falsifiable claim

**H0:** Under `--max-exists-calls 70000000`, `--lru-maxsize 8000000`, `r=9`, `d=3`-only, the parent exits **2** (PARTIAL).

**H1:** Exit **0** with definite **`d=3 feasible=`** without budget exhaustion.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-6e7-lru-8m` (PARTIAL ~562 s), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-7e7-lru-8m` (PARTIAL ~644 s).
