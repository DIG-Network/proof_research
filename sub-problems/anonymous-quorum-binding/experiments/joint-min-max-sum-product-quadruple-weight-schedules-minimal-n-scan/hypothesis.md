# Hypothesis — joint-min-max-sum-product-quadruple-weight-schedules-minimal-n-scan

## Analogy pass

1. **Abstract structure:** Fix a public weight vector `w ∈ ℤ_{>0}^n` and shells `|S|∈{5,6}`. The tag `K(S)=(min, max, Σ, Π)` maps each subset to a point in `ℤ⁴`. Cross-shell collision means the image sets for `r=5` and `r=6` intersect. The **onset scale** is the smallest `n` (above a fixed floor) where that intersection becomes non-empty — a discrete phase transition in the ambient dimension.

2. **Where else:** (i) Percolation / bootstrap thresholds depend strongly on graph geometry, not just size. (ii) Coincidence of subset sums in additive combinatorics depends on the actual multiset of summands, not only cardinality. (iii) Collision time of hash families under domain reparameterization (different embeddings of the same index set).

3. **Machinery in those domains:** Critical probability or critical size shifts when local structure changes; inverse theorems constrain which sumsets collide; birthday bounds depend on the actual distribution of inputs.

4. **Transfer candidate:** The **097** result pins `n_min=11` for `w_i=i+1`. Re-labeling indices with different positive weights changes which subset tuples share the same `(min,max,Σ,Π)` — so **minimal collision `n` is a property of the schedule**, not a universal constant for this statistic class.

## Falsifiable claim

For exact `K=(min w_i, max w_i, Σ w_i, Π w_i)` on shells 5 and 6, there exists a simple deterministic weight schedule (among a fixed small menu: linear, squares, powers of two, Fibonacci, primes, reversed linear, triangular) such that there is **no** 5-vs-6 cross-shell collision when the universe has **`n=11`** validators (i.e. the `n=11` onset seen for `w_i=i+1` is **not** universal for this statistic).

**Outcome interpretation:**

- **PASS:** At least one listed schedule has **no** cross-shell collision at `n=11` (encoding change postpones or removes the failure at eleven).
- **FAIL:** Every listed schedule already has a cross-shell collision at `n=11`.

The script also reports the first `n∈[11,18]` with a collision when present (bounded scan; absence in-range is reported as `None`).
