# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n71-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=71` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 163.684                   |
| fibonacci       | NO_COLLISION  | 143.456                   |
| first_n_primes  | NO_COLLISION  | 127.363                   |

**Total wall time:** ~434.5 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=71`. Together with experiments **101–114**, there is **no** such collision for **`n ∈ [11,71]`** on these three schedules under exact **`K`**.
