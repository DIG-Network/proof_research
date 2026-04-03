# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n74-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=74` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 226.594                   |
| fibonacci       | NO_COLLISION  | 190.005                   |
| first_n_primes  | NO_COLLISION  | 164.362                   |

**Total wall time:** ~581.0 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=74`. Together with experiments **101–117**, there is **no** such collision for **`n ∈ [11,74]`** on these three schedules under exact **`K`**.
