# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n72-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=72` under exact `K=(min w, max w, Σw, Πw)`.

**Measured:**

| Schedule        | Result        | Per-schedule elapsed (s) |
|-----------------|---------------|---------------------------|
| pow2_2^i        | NO_COLLISION  | 167.655                   |
| fibonacci       | NO_COLLISION  | 163.901                   |
| first_n_primes  | NO_COLLISION  | 127.999                   |

**Total wall time:** ~459.6 s for all three schedules.

**Conclusion:** None of the three schedules exhibits a 5-vs-6 cross-shell collision at `n=72`. Together with experiments **101–115**, there is **no** such collision for **`n ∈ [11,72]`** on these three schedules under exact **`K`**.
