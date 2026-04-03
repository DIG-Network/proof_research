# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n64-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=64` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 80.703                    |
| fibonacci       | NO_COLLISION  | 72.834                    |
| first_n_primes  | NO_COLLISION  | 63.036                    |

**Total wall time:** ~216.6 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=64`. Together with experiments **101–107**, there is **no** such collision for **`n ∈ [11,64]`** on these three schedules under exact **`K`**.
