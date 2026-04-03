# Hypothesis — joint-min-max-sum-product-quadruple-pow2-fib-primes-n51-55-scan

## Analogy pass

1. **Abstract structure:** Same **`K(S) = (min w, max w, Σ w, Π w)`** cross-shell (5 vs 6) collision probe as **098**–**102**. Experiment **102** showed **`pow2_2^i`**, **`fibonacci`**, and **`first_n_primes`** have **no** 5-vs-6 collision for **any** **`n ∈ [46,50]`**; combined with **101**, **no** collision for **`n ∈ [11,50]`** on these three.

2. **Where else does this structure appear?**
   - **Combinatorics:** **`C(n,5)`** and **`C(n,6)`** grow polynomially in **`n`**; onset of collisions may require larger **`n`** for slowly growing weight schedules.
   - **Fingerprinting:** Super-exponential weights (**`2^i`**) grow key diversity quickly but may still avoid cross-shell collisions longer than naive intuition suggests.
   - **Experimental continuation:** **`[51,55]`** is the next contiguous band after **102** for the three schedules still without collision through **`n=50`**.

3. **Machinery:** Per-**`n`** exhaustive comparison: store **`C(n,5)`** keys with one witness; scan **`C(n,6)`** for membership (same as **101**/**102**).

4. **Transfer candidate:** If **any** of the three schedules first collides in **`[51,55]`**, we localize the next onset; if **none** do, negative evidence extends through **`n=55`**.

## Falsifiable claim

For **`pow2_2^i`**, **`fibonacci`**, and **`first_n_primes`** (same definitions as **098**), there exists **some** **`n` with `51 ≤ n ≤ 55`** such that **`keys_{|S|=5} ∩ keys_{|S|=6} ≠ ∅`** for exact **`K`**.

- **PASS** if **at least one** of the three schedules has **at least one** such collision for **some** **`n ∈ [51,55]`**.
- **FAIL** if **all three** schedules have **no** cross-shell collision for **every** **`n ∈ [51,55]`**.

## Lineage

- **Extends** **`joint-min-max-sum-product-quadruple-pow2-fib-primes-n46-50-scan` (102)** — same three schedules; range **`[51,55]`** only.
