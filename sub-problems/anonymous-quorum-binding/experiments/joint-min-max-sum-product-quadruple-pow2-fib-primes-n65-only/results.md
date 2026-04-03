# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n65-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=65` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 89.800                    |
| fibonacci       | NO_COLLISION  | 79.945                    |
| first_n_primes  | NO_COLLISION  | 68.010                    |

**Total wall time:** ~237.8 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=65`. Together with experiments **101–108**, there is **no** such collision for **`n ∈ [11,65]`** on these three schedules under exact **`K`**.
