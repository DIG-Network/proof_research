# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n82-only

**Outcome:** **FAIL**

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision on exact `K=(min,max,Σ,Π)` at `n=82`.

**Measured:**

| Schedule        | Result       | Per-schedule CPU (s) |
|-----------------|--------------|----------------------|
| pow2_2^i        | NO_COLLISION | 409.008              |
| fibonacci       | NO_COLLISION | 360.014              |
| first_n_primes  | NO_COLLISION | 315.350              |

**Total wall time:** ~1084.4 s (~18.1 min) for all three schedules.

**Conclusion:** None of the three schedules collides at `n=82`. Together with experiments **101–125**, there is **no** such 5-vs-6 cross-shell collision for **`n ∈ [11,82]`** on these three schedules under exact **`K`**.

**Reasoning:** Exhaustive enumeration per schedule: build map from `K` on all 5-subsets, scan 6-subsets for a matching `K` from a different shell.
