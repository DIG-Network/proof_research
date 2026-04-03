# Hypothesis — joint-min-max-sum-product-quadruple-four-schedules-extended-n35-scan

## Analogy pass

1. **Abstract structure:** Same shell-separation probe as **097**/**098**/**099**: exact `K(S) = (min w, max w, Σ w, Π w)` on public index weights. We ask how the **onset scale** of 5-vs-6 cross-shell collisions depends on the **growth law** of `w_i` (exponential, quadratic triangular, Fibonacci, primes).

2. **Where else does this structure appear?**
   - **Analytic number theory:** prime gaps and Fibonacci growth change the multiset of “masses” available to subset sums/products.
   - **Combinatorics:** collision first times for injective-looking maps often scale with the effective “degrees of freedom” of the weight vector.
   - **Coding / hashing:** independent schedules behave like different hash families; universality is not expected without proof.

3. **Machinery:** Exhaustive shell comparison per `n` (toy falsifier only).

4. **Transfer candidate:** After **099** showed **square** weights delay collision to **`n=31`**, compare **minimal collision `n`** for **`2^i`**, **triangular**, **Fibonacci**, and **first-`n` primes** on the same **`n ∈ [11,35]`** band as **099**.

## Falsifiable claim

For each of the four schedules **`pow2_2^i`**, **`triangular_(i+1)(i+2)/2`**, **`fibonacci`**, **`first_n_primes`** (as in **098**), there exists **some** integer **`n` with `11 ≤ n ≤ 35`** such that **`keys_{|S|=5} ∩ keys_{|S|=6} ≠ ∅`** for exact **`K`**.

- **PASS** if **all four** schedules exhibit **at least one** such collision for **some** **`n ≤ 35`** (and the script prints the **minimal** such **`n`** per schedule).
- **FAIL** if **any** schedule has **no** cross-shell collision for **every** **`n` in `[11,35]`**.

## Lineage

- **Extends** **`joint-min-max-sum-product-quadruple-weight-schedules-minimal-n-scan` (098)** ( **`n≤18`** only for these four).
- **Sibling** **`joint-min-max-sum-product-quadruple-square-weights-extended-n-scan` (099)** (square schedule on **`[11,35]`**).
