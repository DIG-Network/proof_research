# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n73-only

- **observation:** Single-`n` probe at **`n=73`**; same exhaustive 5-then-6 map logic as **116**.
- **observation:** `pow2_2^i` at `n=73` took longer per schedule than at `n=72` on one runner (~236 s vs ~168 s for pow2), consistent with growth in `C(73,6)` vs `C(72,6)`; total wall time ~554 s for all three schedules on the run recorded in `results.md`.
- **dead_end:** Hypothesis “at least one schedule collides at **`n=73`**” is **falsified** for **pow2** / **fib** / **primes** on exact **`K`**; the exact-quadruple separation on these schedules extends through **`n=73`** in the combined **101–117** chain.
- **question:** Whether a collision appears at **`n=74`** or only for other weight schedules (e.g. triangular, as in **101**) remains open for the next single-`n` step.

**Next step:** **`n=74`** single-`n` probe, or pivot if compute budget tightens (**`C(n,6)`** grows quickly).
