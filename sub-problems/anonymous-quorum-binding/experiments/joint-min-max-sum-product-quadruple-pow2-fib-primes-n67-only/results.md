# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n67-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=67` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 107.972                   |
| fibonacci       | NO_COLLISION  | 93.927                    |
| first_n_primes  | NO_COLLISION  | 81.839                    |

**Total wall time:** ~283.7 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=67`. Together with experiments **101–110**, there is **no** such collision for **`n ∈ [11,67]`** on these three schedules under exact **`K`**.
