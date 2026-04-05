# Hypothesis — stratified `|∩|` predicate for `min_d=2` (full off-diagonal grid)

## Analogy pass

1. **Abstract structure:** Depth-2 feasibility in a fixed XOR/adaptive-coordinate language is a **piecewise algebraic** condition on the labels `(T_i, T_j, Q)`. Prior work shows the feasible `Q` depends on how the two triples meet (`|T_i ∩ T_j|`).

2. **Where else:** (i) **Stratified manifolds** — global statements glue smooth laws on strata; (ii) **Case analysis in coding theory** — minimum distance certificates split by intersection pattern of supports; (iii) **Piecewise linear classifiers** — decision boundaries change when discrete features cross thresholds.

3. **Machinery there:** Local invariants on each stratum; global correctness iff strata partition the state space and predicates are mutually exclusive on overlaps (here overlaps are empty by `|∩|`).

4. **Transfer candidate:** Combine the **proven** `s ∈ {0,1}` law (`Q ∈ {W(i,j), W(j,i)}`, experiment 162) with the **candidate** `s = 2` law (`Q ∈ {W(i,j), C}` with `C = [7] \ (T_i △ T_j)`, experiment 159) into one **global** predicate on all off-diagonal cells (`i < j`). If the `s=2` piece were exact, this would be a unified three-chart disjunction (two orientations + complement chart).

## Falsifiable claim

On the `n=7`, `{2,3}` grid (`coord + full r=2 + doubleton r=3 + singleton r=4`), for every cell with **distinct** triple indices `i < j`:

`min_d = 2` **if and only if** `P_s(Q)` holds, where `s = |T_i ∩ T_j|` and:

- `s ∈ {0,1}`: `P_s(Q) := (Q = W(i,j)) ∨ (Q = W(j,i))` with `W(a,b) = (T_a \ T_b) ∪ ([7] \ (T_a ∪ T_b))`.
- `s = 2`: `P_s(Q) := (Q = W(i,j)) ∨ (Q = C(i,j))` with `C(i,j) = [7] \ (T_i △ T_j)`.

## Memory / prior constraints (desk check)

- Experiment **162** (PASS): `s ∈ {0,1}` stratum satisfies the wedge ∨ reverse-wedge biconditional.
- Experiment **159** (FAIL): on `s = 2` alone, `min_d = 2` has **420** witnesses vs only **210** hits on `{W, C}` — **strictly more** depth-2 fibers than the two-chart `{W,C}` predicate.

**Expectation:** The global biconditional **fails** because the `s=2` patch remains incomplete; this experiment **quantifies** whether *any* `s=2` depth-2 witness satisfies the `s∈{0,1}` charts (should be no — disjoint `Q` families) and confirms the global obstruction is entirely the `s=2` fiber mismatch.
