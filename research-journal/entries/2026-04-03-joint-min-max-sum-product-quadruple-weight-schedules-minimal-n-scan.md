# Experiment entry — 2026-04-03 — joint-min-max-sum-product-quadruple-weight-schedules-minimal-n-scan

**Path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-weight-schedules-minimal-n-scan`

**Context:** anonymous-quorum-binding (toy shell-separation / aggregate-tag track)

**Hypothesis tested:** The **`n=11`** 5-vs-6 cross-shell collision for exact `K=(min,max,Σ,Π)` under **`w_i=i+1`** (**097**) is not forced at **`n=11`** for every simple deterministic public weight schedule — some schedules avoid collision at eleven.

**Outcome:** **PASS** (hypothesis **confirmed**)

**Key finding:** **Linear** and **reverse-linear** (`n-i`) schedules **collide** at **`n=11`** (same multiset, same sample **`K=(1,11,31,2640)`**). **Squares** `(i+1)²`, **powers of two** `2^i`, **triangular** weights, **Fibonacci** (first `n` terms), and **first `n` primes** have **no** cross-shell collision at **`n=11`**. Bounded scan **`n∈[11,18]`** found **no** collision for those five schedules in-range.

**Implications:**

- **097** is **schedule-specific** at the `n=11` scale; “first failure at eleven validators” is not an invariant of the quadruple statistic over all positive weight assignments.
- Toy **linkability / shell-separation** claims must name the **public weight rule**, not only **`n`**.

**Analogy pass summary:** Phase-transition onset depends on the embedding of indices into weights (same shell cardinalities, different multiset geometry).

**Space definition:** none
