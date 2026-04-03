# Hypothesis — joint-min-max-sum-product-quadruple-pow2-fib-primes-n66-only

## Analogy pass (mandatory)

1. **Abstract structure:** We test whether the exact public summary  
   `K(S) = (min w, max w, Σ w, Π w)` on a length-`n` public weight vector still separates **|S|=5** from **|S|=6** subsets when `n` advances one step past **109** (`n=65`). Experiments **101–109** found **no** 5-vs-6 cross-shell collision for **pow2**, **Fibonacci**, and **first-n primes** through **`n=65`**.

2. **Where else this structure appears:**  
   - **Sufficient statistics / moment problems:** collapsing a high-dimensional subset choice to a few scalars; injectivity is fragile when the statistic is too coarse.  
   - **Coding / hashing:** short fingerprints of combinatorial objects; collisions appear at thresholds depending on structure.  
   - **Combinatorial design:** when two different `k`-subsets of `[n]` share the same multiset statistics.

3. **Machinery in those domains:** information-theoretic lower bounds on fingerprint length; birthday bounds; explicit collision search on structured weights.

4. **Transfer seed:** Empirical continuation of the **exact quadruple** line on **structured schedules** — a **single** `n=66` probe is the minimal extension of **109** (compute cost scales with `C(n,6)`).

## Falsifiable claim

**H:** For **at least one** of the three schedules (`pow2_2^i`, `fibonacci`, `first_n_primes`), there exists a **5-vs-6** cross-shell collision at **`n=66`** (exact integer `K`).

- **PASS (script exit 0):** At least one schedule collides at `n=66`.  
- **FAIL (script exit 1):** **None** of the three collide at `n=66`.

## Lineage

- **Parent:** `joint-min-max-sum-product-quadruple-pow2-fib-primes-n65-only` (109) — **extends** the same `K` and schedule set; **refines** the `n` frontier by one.
