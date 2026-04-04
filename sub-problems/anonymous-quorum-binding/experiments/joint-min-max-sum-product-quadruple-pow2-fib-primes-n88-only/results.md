# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n88-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision on exact `K=(min,max,Σ,Π)` at `n=88`.

**Measured:**

| Schedule        | Result       | Per-schedule elapsed (s) |
|-----------------|--------------|--------------------------|
| pow2_2^i        | NO_COLLISION | 687.631                  |
| fibonacci       | NO_COLLISION | 638.051                  |
| first_n_primes  | NO_COLLISION | 522.655                  |

**Total wall time:** ~1848.3 s (~30.8 min) for all three schedules.

**Conclusion:** None of the three schedules collides at `n=88`. Together with experiments **101–131**, there is **no** such 5-vs-6 cross-shell collision for **`n ∈ [11,88]`** on these three schedules under exact **`K`**.

**Reasoning:** Exhaustive enumeration per schedule: build map from `K` on all 5-subsets, scan 6-subsets for a matching `K` from a different shell.
