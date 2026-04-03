# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n72-only

- **observation:** Single-`n` probe at **`n=72`**; same exhaustive 5-then-6 map logic as **115**.
- **observation:** **`C(72,6)`** step is modestly larger than **`n=71`**; wall time ~460 s vs ~435 s for **115** on this runner.
- **dead_end (for this `n`):** Hypothesis “at least one schedule collides at **`n=72`**” is **falsified** for **pow2** / **fib** / **primes** on exact **`K`**.

**Next step:** **`n=73`** single-`n` probe, or pivot if compute budget tightens ( **`C(n,6)`** grows quickly).
