# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n84-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision on exact `K=(min,max,Σ,Π)` at `n=84`.

**Measured:**

| Schedule        | Result       | Per-schedule elapsed (s) |
|-----------------|--------------|--------------------------|
| pow2_2^i        | NO_COLLISION | 483.770                  |
| fibonacci       | NO_COLLISION | 421.120                  |
| first_n_primes  | NO_COLLISION | 393.210                  |

**Total wall time:** ~1298.1 s (~21.6 min) for all three schedules.

**Conclusion:** None of the three schedules collides at `n=84`. Together with experiments **101–127**, there is **no** such 5-vs-6 cross-shell collision for **`n ∈ [11,84]`** on these three schedules under exact **`K`**.

**Reasoning:** Exhaustive enumeration per schedule: build map from `K` on all 5-subsets, scan 6-subsets for a matching `K` from a different shell.
