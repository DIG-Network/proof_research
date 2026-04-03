# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n78-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=78` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 313.152                   |
| fibonacci       | NO_COLLISION  | 291.856                   |
| first_n_primes  | NO_COLLISION  | 247.006                   |

**Total wall time:** ~852.1 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=78`. Together with experiments **101–121**, there is **no** such collision for **`n ∈ [11,78]`** on these three schedules under exact **`K`**.
