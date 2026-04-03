# Hypothesis

**Claim (falsifiable):** On `n=10` with public weights `w_i = i+1`, there exist distinct subsets `S_5`, `S_6` with `|S_5|=5`, `|S_6|=6` such that the **exact integer quadruple**

\[
K(S)=(\min_{i\in S} w_i,\ \max_{i\in S} w_i,\ \sum_{i\in S} w_i,\ \prod_{i\in S} w_i)
\]

agrees on both shells (a **5-vs-6 cross-shell key collision**).

**Parent experiments:** `min-max-sum-triple-weight-five-six-shell-collision` (091), `joint-min-max-product-weight-five-six-shell-collision` (092), `integer-sum-product-joint-five-six-collision` (063).

**Rationale:** 091 and 092 show `(min,max,sum)` and `(min,max,prod)` each admit many exact cross-shell collisions **separately**. 063 shows `(sum,prod)` alone has cross-shell collisions. This experiment asks whether **jointly** pinning extrema **and** both mass statistics still leaves room for 5-vs-6 ambiguity — a natural "maximal summary in this family" probe before leaving the `(min,max,·,·)` track.

## Analogy pass (mandatory)

1. **Abstract structure:** Map each subset to a low-dimensional statistic vector; ask whether the statistic is **injective** on the union of two adjacent cardinality shells (threshold-adjacent layers of the subset lattice).

2. **Analogous domains:** (i) **Sufficient statistics** — when does a fixed-length summary identify a sample up to equivalence? (ii) **Moment problems** — matching mixed moments across different supports. (iii) **Computer vision shape descriptors** — bounding box + area + "volume" can still fail to separate configurations.

3. **Machinery in those domains:** Injectivity from dimension counting / uniqueness theorems; when it fails, explicit **witness pairs** (same descriptor, different configuration).

4. **Transfer candidate:** Combine the two third-coordinate failures (091 vs 092) by **stacking** `(sum, prod)` while keeping `(min,max)` — test whether redundancy eliminates cross-shell ambiguity or whether witness pairs still exist.

**Outcome interpretation:** `PASS` if at least one cross-shell collision exists; `FAIL` if `K` is injective on `C(10,5) ∪ C(10,6)` (no 5-vs-6 key collision).
