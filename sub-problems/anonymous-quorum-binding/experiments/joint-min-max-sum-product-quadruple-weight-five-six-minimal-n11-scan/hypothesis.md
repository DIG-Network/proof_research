# Hypothesis

**Claim (falsifiable):** For public weights `w_i = i+1` on `[n]`, with shells `|S| ∈ {5,6}` and exact integer quadruple

\[
K(S)=(\min_{i\in S} w_i,\ \max_{i\in S} w_i,\ \sum_{i\in S} w_i,\ \prod_{i\in S} w_i),
\]

the **smallest** `n > 10` admitting a **5-vs-6 cross-shell** key collision is **`n = 11`** (a collision already exists when the universe has eleven validators).

**If false:** The minimal such `n` is **`12`** (no cross-shell collision on `C(11,5) ∪ C(11,6)`; collisions first appear at `n=12`, as in **096**).

**Parent experiments:** `joint-min-max-sum-product-quadruple-weight-five-six-shell-n12` (096, `n=12` **PASS**), `joint-min-max-sum-product-quadruple-weight-five-six-shell-collision` (093, `n=10` **FAIL** / injective).

## Analogy pass (mandatory)

1. **Abstract structure:** Monotone scan of ambient set size `n` for first appearance of a structural coincidence (collision) between two layers of a graded poset under a fixed low-dimensional statistic.

2. **Analogous domains:** (i) **Phase transitions in combinatorics** — a property flips at a critical `n`. (ii) **Birthday paradox** — collision probability hits 1 at finite support size (here deterministic exhaustive). (iii) **Minimal counterexample** — classical proof technique: locate the smallest `n` where injectivity breaks.

3. **Machinery:** Exhaustive maps from `C(n,5)` and `C(n,6)` into `Z^4`; intersect key sets; first `n` with nonempty intersection.

4. **Transfer candidate:** Reuse **093/096** quadruple scan at **`n=11`** only — settles whether the **096** witness family requires the twelfth weight or already arises at **`n=11`**.

**Outcome interpretation:** `PASS` if `n=11` has `|keys_5 ∩ keys_6| ≥ 1`. `FAIL` if `n=11` has empty intersection but `n=12` has nonempty intersection (minimal `n` is **12**).
