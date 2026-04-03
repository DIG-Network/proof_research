# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n73-only

- **observation:** `pow2_2^i` at `n=73` took longer per schedule than at `n=72` (~236 s vs ~168 s), consistent with growth in `C(73,6)` vs `C(72,6)`.
- **dead_end:** None of the three structured schedules produced a 5-vs-6 cross-shell collision at this `n`; the exact-quadruple separation on these schedules extends through **`n=73`** in the combined **101–117** chain.
- **question:** Whether a collision appears at **`n=74`** or only for other weight schedules (e.g. triangular, as in **101**) remains open for the next single-`n` step.
