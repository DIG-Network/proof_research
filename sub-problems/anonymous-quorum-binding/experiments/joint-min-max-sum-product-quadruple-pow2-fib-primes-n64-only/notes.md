# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n64-only

- **observation:** `C(64,6)` is ~7.4× `C(63,6)`; total wall ~217 s vs ~188 s for `n=63` (107), consistent with combinatorial growth.
- **dead_end:** (none new) — still no collision for pow2 / fib / primes on this `K` through `n=64`.
- **insight:** The structured-weight “clean” band for this exact quadruple continues one more step; next single-`n` step (`n=65`) is another ~7× jump on the 6-shell enumeration.
- **question:** Whether any collision appears for these schedules before practical limits, or whether injectivity holds for all `n` in this family, is open.
