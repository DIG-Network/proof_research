# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n80-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=80` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 360.866                   |
| fibonacci       | NO_COLLISION  | 299.050                   |
| first_n_primes  | NO_COLLISION  | 259.536                   |

**Total wall time:** ~919.5 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=80`. Together with experiments **101–123**, there is **no** such collision for **`n ∈ [11,80]`** on these three schedules under exact **`K`**.
