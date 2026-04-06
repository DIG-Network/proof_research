# Hypothesis: unified wedge pair for all off-diagonal strata (n=8 shell {2,3,4})

## Analogy pass

1. **Abstract structure:** Same verifier-oracle cell language as n=7: fixed coordinate + full r=2 XOR + a doubleton of r=3 splits (two triple masks) + one r=4 split (one quad). Off-diagonal pairs stratify by `s = |T_i ∩ T_j|`. At n=7 the predicate `Q ∈ {W_ij, W_ji}` matched `min_d=2` on all `s ∈ {0,1,2}`; n=6 failed the same unified certificate (quartic hits absent).

2. **Analogous domains:** (i) Renormalization group flow — behavior can change with system size even when local rules match. (ii) Finite-size scaling in statistical mechanics — critical exponents stabilize only past a threshold `n`. (iii) Monotonicity of proof complexity in parameterized combinatorics.

3. **Machinery there:** Identify a scaling window where a certificate holds; outside it, new disjuncts or strata appear.

4. **Transfer candidate:** If n=8 resembles n=7 more than n=6 in the XOR-split geometry (larger symmetric group, more quartic patterns), the n=7 unified wedge law may **restore** at n=8.

## Falsifiable claim

For `n=8`, language = coordinate partition + full `r=2` XOR + doubleton `{T_i,T_j}` on `r=3` + singleton `Q` on `r=4`, and for all off-diagonal pairs with `i<j` and `s = |T_i ∩ T_j| ∈ {0,1,2}`:

`min_d == 2` if and only if `(Q == W_ij) or (Q == W_ji)`.

## Memory / prior context

- Parent: n=7 experiment `...-n7-...-offdiag-unified-wedge-pair-all-strata-biconditional` (PASS).
- n=6 port of the same test (FAIL): quartic `W_ij∨W_ji` never hit; `min_d=2` universal on stratum.
- This experiment is the direct n=8 port to test size dependence of the unified certificate.
