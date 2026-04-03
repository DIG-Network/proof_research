# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n63-only

**Outcome:** **FAIL** (script exit code 1)

**Hypothesis:** At least one of `pow2_2^i`, Fibonacci prefix, first `n` primes has a 5-vs-6 cross-shell collision at `n=63` on exact integer `K(S) = (min w, max w, Σ w, Π w)`.

**Measured:**

| Schedule        | n   | Cross-shell collision | elapsed_s |
|-----------------|-----|------------------------|-----------|
| pow2_2^i        | 63  | no                     | 71.670    |
| fibonacci       | 63  | no                     | 60.553    |
| first_n_primes  | 63  | no                     | 55.785    |

**Total wall time:** ~188.0 s for all three schedules.

**Conclusion:** **None** of the three schedules exhibits a 5-vs-6 collision at `n=63`. Together with experiments **101–106**, there is **no** such collision for **`n ∈ [11,63]`** on these three schedules under this exact **`K`**.
