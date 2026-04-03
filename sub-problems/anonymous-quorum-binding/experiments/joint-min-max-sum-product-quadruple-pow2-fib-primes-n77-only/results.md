# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n77-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=77` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 287.704                   |
| fibonacci       | NO_COLLISION  | 257.736                   |
| first_n_primes  | NO_COLLISION  | 210.458                   |

**Total wall time:** ~755.9 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=77`. Together with experiments **101–120**, there is **no** such collision for **`n ∈ [11,77]`** on these three schedules under exact **`K`**.
