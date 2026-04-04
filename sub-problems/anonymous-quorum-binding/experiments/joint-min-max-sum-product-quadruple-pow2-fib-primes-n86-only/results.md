# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n86-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision on exact `K=(min,max,Σ,Π)` at `n=86`.

**Measured:**

| Schedule        | Result       | Per-schedule elapsed (s) |
|-----------------|--------------|--------------------------|
| pow2_2^i        | NO_COLLISION | 604.124                  |
| fibonacci       | NO_COLLISION | 515.192                  |
| first_n_primes  | NO_COLLISION | 446.731                  |

**Total wall time:** ~1566.0 s (~26.1 min) for all three schedules.

**Conclusion:** None of the three schedules collides at `n=86`. Together with experiments **101–129**, there is **no** such 5-vs-6 cross-shell collision for **`n ∈ [11,86]`** on these three schedules under exact **`K`**.

**Reasoning:** Exhaustive enumeration per schedule: build map from `K` on all 5-subsets, scan 6-subsets for a matching `K` from a different shell.
