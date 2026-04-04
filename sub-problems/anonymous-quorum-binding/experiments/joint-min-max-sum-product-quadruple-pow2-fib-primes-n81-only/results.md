# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n81-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=81` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 376.451                   |
| fibonacci       | NO_COLLISION  | 328.660                   |
| first_n_primes  | NO_COLLISION  | 292.286                   |

**Total wall time:** ~997.4 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=81`. Together with experiments **101–124**, there is **no** such collision for **`n ∈ [11,81]`** on these three schedules under exact **`K`**.
