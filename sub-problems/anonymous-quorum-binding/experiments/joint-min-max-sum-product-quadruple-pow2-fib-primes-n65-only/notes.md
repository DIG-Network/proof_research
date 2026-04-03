# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n65-only

- **observation:** `C(65,6)` is ~7.2× `C(64,6)`; total wall ~238 s vs ~217 s for `n=64` (108), consistent with combinatorial growth.
- **dead_end:** (none new) — still no collision for pow2 / fib / primes on this `K` through `n=65`.
- **insight:** The structured-weight “clean” band for this exact quadruple continues one more step; next single-`n` step (`n=66`) is another large jump on the 6-shell enumeration.
- **question:** Whether any collision appears for these schedules before practical limits, or whether injectivity holds for all `n` in this family, is open.
