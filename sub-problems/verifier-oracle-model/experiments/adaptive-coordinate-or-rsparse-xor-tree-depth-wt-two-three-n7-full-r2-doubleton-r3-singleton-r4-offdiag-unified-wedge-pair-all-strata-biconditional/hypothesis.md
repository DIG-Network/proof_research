# Hypothesis: unified wedge pair for all off-diagonal strata (n=7 shell {2,3,4})

## Analogy pass

1. **Abstract structure:** The verifier-oracle model assigns a minimum XOR-split depth `min_d` to each cell `(T_i, T_j, Q)` in a fixed language. Off-diagonal pairs `(i,j)` stratify by `s = |T_i ∩ T_j|`. Earlier work found **stratified** certificates: for `s ∈ {0,1}`, `min_d=2` iff `Q` is one of the two ordered wedges `W_ij` or `W_ji`; for `s=2`, the symmetric envelope required also the complement-of-symmetric-difference mask `C_ij` unless the reverse wedge is included.

2. **Analogous domains:** (i) Piecewise definitions in dynamical systems (different normal forms per region). (ii) Case analysis in combinatorial optimization. (iii) Stratified sufficient statistics in statistics (different minimal summaries per stratum).

3. **Machinery there:** Patch together region-specific predicates; unify only when a single formula holds across regions.

4. **Transfer candidate:** After experiment 164 showed that on `s=2`, `W_ij ∨ W_ji ∨ C_ij` is equivalent to `W_ij ∨ W_ji` (because `C` is redundant when `|C|=5` forces `pred_c=0`), the **global** off-diagonal law might be the **same** predicate for all `s ∈ {0,1,2}`: `Q ∈ {W_ij, W_ji}`.

## Falsifiable claim

For `n=7`, language = coordinate partition + full `r=2` XOR + doubleton `{T_i,T_j}` on `r=3` + singleton `Q` on `r=4`, and for all off-diagonal pairs with `i<j` and `s = |T_i ∩ T_j| ∈ {0,1,2}`:

`min_d == 2` if and only if `(Q == W_ij) or (Q == W_ji)`.

## Memory / prior context

- Parent: experiment 164 (PASS on `s=2` with `W∨W_rev∨C`, noted equivalence to `W∨W_rev`).
- Experiment 162 (PASS) established `W∨W_rev` on `s∈{0,1}`.
- This experiment tests whether the **unified** predicate (no `C` branch) holds on the **full** off-diagonal union.
