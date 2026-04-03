# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n76-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=76` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 268.075                   |
| fibonacci       | NO_COLLISION  | 220.253                   |
| first_n_primes  | NO_COLLISION  | 189.980                   |

**Total wall time:** ~678.3 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=76`. Together with experiments **101–119**, there is **no** such collision for **`n ∈ [11,76]`** on these three schedules under exact **`K`**.
