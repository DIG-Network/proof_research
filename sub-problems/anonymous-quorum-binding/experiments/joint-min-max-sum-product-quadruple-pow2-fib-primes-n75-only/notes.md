# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n75-only

- **Observation:** Exhaustive 5-vs-6 cross-shell search for exact integer `K=(min,max,Σ,Π)` at `n=75` found **no** collision for **pow2**, **Fibonacci**, or **first-`n` primes** (same pattern as **118** at `n=74`).
- **Timing:** `C(75,6)` is one step larger than `C(74,6)`; total wall ~637 s vs ~581 s for **118**.
- **Next step:** Single-`n` probe **`n=76`** continues the frontier; alternatively pivot to **verifier-oracle-model** open questions.
