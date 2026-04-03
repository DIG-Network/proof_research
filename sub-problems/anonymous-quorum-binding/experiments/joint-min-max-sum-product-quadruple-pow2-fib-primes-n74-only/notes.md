# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n74-only

- **observation:** Single-`n` probe at **`n=74`**; same exhaustive 5-then-6 map logic as **117**.
- **observation:** Total wall time ~581 s for all three schedules on the run recorded in `results.md`; `pow2_2^i` ~227 s, fib ~190 s, primes ~164 s.
- **dead_end:** Hypothesis “at least one schedule collides at **`n=74`**” is **falsified** for **pow2** / **fib** / **primes** on exact **`K`**; the exact-quadruple separation on these schedules extends through **`n=74`** in the combined **101–118** chain.
- **question:** Whether a collision appears at **`n=75`** or only for other weight schedules (e.g. triangular, as in **101**) remains open for the next single-`n` step.

**Next step:** **`n=75`** single-`n` probe, or pivot if compute budget tightens (**`C(n,6)`** grows quickly).
