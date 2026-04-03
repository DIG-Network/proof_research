# Hypothesis — joint-min-max-sum-product-quadruple-pow2-fib-primes-n56-60-scan

## Analogy pass

1. **Abstract structure:** Same **`K(S) = (min w, max w, Σ w, Π w)`** cross-shell (5 vs 6) collision probe as **101**–**103**. Experiment **103** showed **`pow2_2^i`**, **`fibonacci`**, and **`first_n_primes`** have **no** 5-vs-6 collision for **any** **`n ∈ [51,55]`**; combined with **101**/**102**, **no** collision for **`n ∈ [11,55]`** on these three.

2. **Where else does this structure appear?**
   - **Combinatorics:** **`C(n,5)`** and **`C(n,6)`** grow as **`O(n⁵)`** / **`O(n⁶)`**; the next contiguous band **`[56,60]`** tests whether slow-onset schedules finally collide before **`n=61`**.
   - **Fingerprinting:** **`2^i`** weights grow super-exponentially; Fibonacci and primes grow sub-exponentially — collision onset may differ sharply by schedule.
   - **Experimental continuation:** **`[56,60]`** is the next band after **103**; cost per **`n`** rises with binomial counts.

3. **Machinery:** Per-**`n`** exhaustive comparison: store **`C(n,5)`** keys with one witness; scan **`C(n,6)`** for membership (same as **101**–**103**).

4. **Transfer candidate:** If **any** of the three schedules first collides in **`[56,60]`**, we localize onset; if **none** do, negative evidence extends through **`n=60`**.

## Falsifiable claim

For **`pow2_2^i`**, **`fibonacci`**, and **`first_n_primes`** (same definitions as **098**), there exists **some** **`n` with `56 ≤ n ≤ 60`** such that **`keys_{|S|=5} ∩ keys_{|S|=6} ≠ ∅`** for exact **`K`**.

- **PASS** if **at least one** of the three schedules has **at least one** such collision for **some** **`n ∈ [56,60]`**.
- **FAIL** if **all three** schedules have **no** cross-shell collision for **every** **`n ∈ [56,60]`**.

## Lineage

- **Extends** **`joint-min-max-sum-product-quadruple-pow2-fib-primes-n51-55-scan` (103)** — same three schedules; range **`[56,60]`** only.
