# Hypothesis

**Claim (falsifiable):** On `n=12` with public weights `w_i = i+1`, there exist distinct subsets `S_5`, `S_6` with `|S_5|=5`, `|S_6|=6` such that the **exact integer quadruple**

\[
K(S)=(\min_{i\in S} w_i,\ \max_{i\in S} w_i,\ \sum_{i\in S} w_i,\ \prod_{i\in S} w_i)
\]

agrees on both shells (a **5-vs-6 cross-shell key collision**).

**Parent experiments:** `joint-min-max-sum-product-quadruple-weight-five-six-shell-collision` (093, `n=10`), `joint-min-max-sum-mod-product-mod-m-five-six-first-collision-n12` (095, modular fold at `n=12`).

**Rationale:** At `n=10`, **093** showed `K` is **injective** on `C(10,5)∪C(10,6)`. Enlarging the universe to `n=12` may introduce new 5- and 6-subsets whose statistics collide across shells (injectivity need not monotonically hold in `n`). **095** already showed modular folds of this statistic collapse at `M=2` at `n=12`; this experiment pins whether the **exact** integer quadruple still separates shells.

## Analogy pass (mandatory)

1. **Abstract structure:** Low-dimensional statistic on subset lattice layers; test injectivity on the union of two adjacent cardinality shells as the ambient set grows.

2. **Analogous domains:** (i) **Sufficient statistics** — identifiability when the sample space grows. (ii) **Moment matching** — new supports can create accidental equalities. (iii) **Hash collision search** — birthday-style growth of collision probability with domain size (here exhaustive, not probabilistic).

3. **Machinery:** Exhaustive enumeration on `C(n,k)`; injective iff `|image| = |C(n,5)|+|C(n,6)|` on the union when shells are disjoint in key space, equivalently no cross-shell key agreement.

4. **Transfer candidate:** Reuse the **093** exact-integer scan at larger `n` to see if the "joint extrema + sum + product" certificate is a stable separator or breaks when more subset patterns appear.

**Outcome interpretation:** `PASS` if at least one cross-shell collision exists; `FAIL` if `K` is injective on `C(12,5) ∪ C(12,6)`.
