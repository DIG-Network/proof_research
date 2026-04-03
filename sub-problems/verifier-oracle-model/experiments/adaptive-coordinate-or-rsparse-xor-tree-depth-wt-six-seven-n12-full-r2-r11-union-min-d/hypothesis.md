# Hypothesis

## Analogy pass

1. **Abstract structure:** For fixed majority slice on hypercube shells, we ask whether the minimal adaptive decision-tree depth for a fixed menu of coordinate and XOR splits stays at 2 when the menu is the full multi-arity XOR union (all nontrivial parities), as we step `n` down from 14 and 13.

2. **Analogous domains:** Finite-size scaling in statistical mechanics (critical exponents stable in a window); sensitivity analysis in combinatorial search (depth plateaus when the split family is sufficiently expressive); coding-theoretic “covering radius” style questions (when a structured family of tests separates all relevant patterns at bounded depth).

3. **Machinery in those domains:** Renormalization / continuation arguments; SAT/DP backtracking with a fixed split library; covering designs and separating systems.

4. **Transfer candidate:** **Parameter continuation in `n`:** if `min_d=2` held for `n=13` and `n=14` with full XOR unions, expect the same for `n=12` on `{6,7}` with `r=2..11`.

## Falsifiable claim

For **`n=12`**, masks with popcount in **`{6,7}`**, the language **`coord + ⋃_{r=2}^{11} XOR_r`** has **`min_d = 2`** (with baselines **`coord_only min_d=12`**, **`coord_plus_full_12xor min_d=1`** unchanged).
