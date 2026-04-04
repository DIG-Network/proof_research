# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n85-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision on exact `K=(min,max,Σ,Π)` at `n=85`.

**Measured:**

| Schedule        | Result       | Per-schedule elapsed (s) |
|-----------------|--------------|--------------------------|
| pow2_2^i        | NO_COLLISION | 516.167                  |
| fibonacci       | NO_COLLISION | 450.680                  |
| first_n_primes  | NO_COLLISION | 417.613                  |

**Total wall time:** ~1384.5 s (~23.1 min) for all three schedules.

**Conclusion:** None of the three schedules collides at `n=85`. Together with experiments **101–128**, there is **no** such 5-vs-6 cross-shell collision for **`n ∈ [11,85]`** on these three schedules under exact **`K`**.

**Reasoning:** Exhaustive enumeration per schedule: build map from `K` on all 5-subsets, scan 6-subsets for a matching `K` from a different shell.
