# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n66-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=66` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 105.263                   |
| fibonacci       | NO_COLLISION  | 93.438                    |
| first_n_primes  | NO_COLLISION  | 77.868                    |

**Total wall time:** ~276.6 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=66`. Together with experiments **101–109**, there is **no** such collision for **`n ∈ [11,66]`** on these three schedules under exact **`K`**.
