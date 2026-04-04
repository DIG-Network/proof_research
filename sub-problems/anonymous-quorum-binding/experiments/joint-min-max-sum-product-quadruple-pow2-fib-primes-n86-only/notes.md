# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n86-only

- **observation:** Wall time ~1566 s total; per-schedule times scale with `C(86,5)+C(86,6)` work vs `n=85`.
- **dead_end:** None for this run — outcome extends the empirical “no collision” band for **pow2** / **fib** / **primes** on exact **`K`** through **`n=86`**.
- **question:** At what **`n`** (if any) does the first collision appear for these three schedules under exact **`K`**? Still open.
- **next:** Single-**`n=87`** probe is the next step in this thread, or pivot to **triangular** / other schedules or verifier-oracle line.
