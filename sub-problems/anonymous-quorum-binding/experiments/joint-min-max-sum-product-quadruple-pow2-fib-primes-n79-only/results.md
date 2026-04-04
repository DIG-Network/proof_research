# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n79-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=79` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 331.973                   |
| fibonacci       | NO_COLLISION  | 303.955                   |
| first_n_primes  | NO_COLLISION  | 249.247                   |

**Total wall time:** ~885.2 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=79`. Together with experiments **101–122**, there is **no** such collision for **`n ∈ [11,79]`** on these three schedules under exact **`K`**.
