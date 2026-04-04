# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n90-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision on exact `K=(min,max,Σ,Π)` at `n=90`.

**Measured:**

| Schedule        | Result       | Per-schedule elapsed (s) |
|-----------------|--------------|--------------------------|
| pow2_2^i        | NO_COLLISION | 804.256                  |
| fibonacci       | NO_COLLISION | 694.063                  |
| first_n_primes  | NO_COLLISION | 626.495                  |

**Total wall time:** ~2124.8 s (~35.4 min) for all three schedules.

**Conclusion:** None of the three schedules collides at `n=90`. Together with experiments **101–133**, there is **no** such 5-vs-6 cross-shell collision for **`n ∈ [11,90]`** on these three schedules under exact **`K`**.

**Reasoning:** Exhaustive enumeration per schedule: build map from `K` on all 5-subsets, scan 6-subsets for a matching `K` from a different shell.
