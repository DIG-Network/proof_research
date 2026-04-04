# Hypothesis — joint-min-max-sum-product-quadruple-pow2-fib-primes-n88-only

## Analogy pass (mandatory)

1. **Abstract structure:** We test whether the exact public summary  
   `K(S) = (min w, max w, Σ w, Π w)` on a length-`n` public weight vector still separates **|S|=5** from **|S|=6** subsets at **`n=88`** (one step after **131** established **`n=87`**). Experiments **101–131** found **no** 5-vs-6 cross-shell collision for **pow2**, **Fibonacci**, and **first-n primes** through **`n=87`**.

2. **Where else this structure appears:**  
   - **Sufficient statistics / moment problems:** collapsing a high-dimensional subset choice to a few scalars; injectivity is fragile when the statistic is too coarse.  
   - **Coding / hashing:** short fingerprints of combinatorial objects; collisions appear at thresholds depending on structure.  
   - **Combinatorial design:** when two different `k`-subsets of `[n]` share the same multiset statistics.

3. **Machinery in those domains:** information-theoretic lower bounds on fingerprint length; birthday bounds; explicit collision search on structured weights.

4. **Transfer seed:** Empirical continuation of the **exact quadruple** line on **structured schedules** — a **single** `n=88` probe is the minimal extension of **131** (compute cost scales with `C(n,6)`).

## Falsifiable claim

**H:** For **at least one** of the three schedules (`pow2_2^i`, `fibonacci`, `first_n_primes`), there exists a **5-vs-6** cross-shell collision at **`n=88`** (exact integer `K`).

- **PASS (script exit 0):** At least one schedule collides at `n=88`.  
- **FAIL (script exit 1):** **None** of the three collide at `n=88`.

## Lineage

- **Parent:** `joint-min-max-sum-product-quadruple-pow2-fib-primes-n87-only` (131) — **extends** the same `K` and schedule set; **refines** the `n` frontier by one.
