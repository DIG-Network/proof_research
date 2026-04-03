# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n70-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=70` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 151.248                   |
| fibonacci       | NO_COLLISION  | 130.756                   |
| first_n_primes  | NO_COLLISION  | 112.340                   |

**Total wall time:** ~394.3 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=70`. Together with experiments **101–113**, there is **no** such collision for **`n ∈ [11,70]`** on these three schedules under exact **`K`**.
