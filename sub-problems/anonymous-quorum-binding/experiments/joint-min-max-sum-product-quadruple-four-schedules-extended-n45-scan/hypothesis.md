# Hypothesis — joint-min-max-sum-product-quadruple-four-schedules-extended-n45-scan

## Analogy pass

1. **Abstract structure:** Same shell-separation probe as **098**/**099**/**100**: exact `K(S) = (min w, max w, Σ w, Π w)` on public index weights; 5-subsets vs 6-subsets. **100** showed **no** collision for four schedules through **`n=35`**.

2. **Where else does this structure appear?**
   - **Combinatorics / extremal set theory:** collision onset scales with the ambient “size” of the multiset of weights and with growth of products.
   - **Hashing:** longer ranges stress injectivity of a fixed summary statistic.
   - **Experimental design:** extending the domain is the direct falsifier for “collision-free forever” claims.

3. **Machinery:** Exhaustive shell comparison per `n` (toy falsifier). Implementation stores only **`C(n,5)`** witness keys, then scans **`C(n,6)`** for membership — same semantics as full double-dict intersection, lower peak memory for large **`n`**.

4. **Transfer candidate:** If **any** of **`2^i`**, **triangular**, **Fibonacci**, **first-`n` primes** first collides between **`n=36`** and **`n=45`**, we learn the **next** band of **onset**; if **none** collide, **negative** evidence strengthens for those schedules on **`K`**.

## Falsifiable claim

For each of the four schedules **`pow2_2^i`**, **`triangular_(i+1)(i+2)/2`**, **`fibonacci`**, **`first_n_primes`** (as in **098**/**100**), there exists **some** integer **`n` with `11 ≤ n ≤ 45`** such that **`keys_{|S|=5} ∩ keys_{|S|=6} ≠ ∅`** for exact **`K`**.

- **PASS** if **all four** schedules exhibit **at least one** such collision for **some** **`n ≤ 45`** (script prints **minimal** such **`n`** per schedule).
- **FAIL** if **any** schedule has **no** cross-shell collision for **every** **`n` in `[11,45]`**.

## Lineage

- **Extends** **`joint-min-max-sum-product-quadruple-four-schedules-extended-n35-scan` (100)** — widens **`n_hi`** from **35** to **45** with equivalent **`K`** test.
- **Extends** **`joint-min-max-sum-product-quadruple-weight-schedules-minimal-n-scan` (098)** (original **`n≤18`** band for these four).
