# Hypothesis: enrich n=8 sparse menu with full r=5,r=6,r=7 XOR — recover wedge stratum

## Analogy pass

1. **Abstract structure:** The n=8 port of the n=7 wedge certificate used the same *sparse* XOR menu as n=7 (coord + full r=2 + doubleton r=3 + singleton r=4). On that menu the off-diagonal `s∈{0,1,2}` stratum had **no** `min_d=2` witnesses (`stratum_min_d2=0`), so the wedge biconditional was **vacuously** true. Separately, the **full multi-arity union** `r∈{2,3,4,5,6,7}` on the same `{2,3}` mask shell achieves `min_d=2` globally (`total_splits=246`).

2. **Analogous domains:** (i) **Sufficient statistics** — a small summary statistic can fail to separate two hypotheses until extra moments are included. (ii) **Renormalization / relevant operators** — new operators become relevant at larger volume. (iii) **Proof theory** — adding axioms (split rules) can change which goals have short proofs.

3. **Machinery there:** Enlarge the verifier’s split language minimally (here: append *full* higher-arity XOR menus) until the depth-2 feasible set becomes nonempty on the same shell, then retest the same geometric certificate.

4. **Transfer candidate:** Append full `r=5`, `r=6`, and `r=7` XOR split lists to the n=8 sparse cell language. If `min_d=2` witnesses reappear on the off-diagonal stratum, the n=7-style wedge predicate may become **non-vacuous** and testable.

## Falsifiable claim

For `n=8`, language = coordinate + full `r=2` + doubleton `r=3` `{T_i,T_j}` + singleton `r=4` `Q` **plus** full XOR menus for `r=5`, `r=6`, and `r=7`, and for all `i<j` with `s=|T_i∩T_j|∈{0,1,2}`:

`min_d == 2` if and only if `(Q == W_ij) or (Q == W_ji)`.

## Memory / prior context

- Parent (vacuous PASS): `…-n8-full-r2-doubleton-r3-singleton-r4-offdiag-unified-wedge-pair-all-strata-biconditional` (`stratum_min_d2=0`).
- Driver probe: `n8/script.py --union-rs 2,3,4,5,6,7` ⇒ `min_d=2` with `total_splits=246`.
- n=7 reference (non-vacuous): `…-n7-…-offdiag-unified-wedge-pair-all-strata-biconditional` (`1190` matches).
