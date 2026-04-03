# Hypothesis — joint-min-max-sum-product-quadruple-pow2-fib-primes-n46-50-scan

## Analogy pass

1. **Abstract structure:** Same **`K(S) = (min w, max w, Σ w, Π w)`** cross-shell (5 vs 6) collision probe as **098**/**100**/**101**. Experiment **101** showed **`pow2_2^i`**, **`fibonacci`**, and **`first_n_primes`** have **no** 5-vs-6 collision for **any** **`n ∈ [11,45]`**; **triangular** already collides at **`n=36`** and is excluded here.

2. **Where else does this structure appear?**
   - **Combinatorics:** extending **`n`** increases key space and product magnitudes; collisions may appear only past a threshold.
   - **Hashing / fingerprinting:** a fixed tuple statistic may stay injective longer for slowly growing weights (**Fibonacci**, **primes**) than for super-exponential (**`2^i`**).
   - **Experimental continuation:** the next band **`[46,50]`** is the minimal extension suggested by **101** for the three still-separated schedules.

3. **Machinery:** Per-**`n`** exhaustive comparison: store **`C(n,5)`** keys with one witness; scan **`C(n,6)`** for membership.

4. **Transfer candidate:** If **any** of the three schedules first collides in **`[46,50]`**, we pin down the **next onset band**; if **none** do, **negative** evidence strengthens through **`n=50`**.

## Falsifiable claim

For **`pow2_2^i`**, **`fibonacci`**, and **`first_n_primes`** (same definitions as **098**), there exists **some** **`n` with `46 ≤ n ≤ 50`** such that **`keys_{|S|=5} ∩ keys_{|S|=6} ≠ ∅`** for exact **`K`**.

- **PASS** if **at least one** of the three schedules has **at least one** such collision for **some** **`n ∈ [46,50]`** (script prints minimal such **`n`** per schedule that collides).
- **FAIL** if **all three** schedules have **no** cross-shell collision for **every** **`n ∈ [46,50]`**.

## Lineage

- **Extends** **`joint-min-max-sum-product-quadruple-four-schedules-extended-n45-scan` (101)** — continues **`n`** for the three schedules with **no** collision through **`n=45`**; range **`[46,50]`** only.
