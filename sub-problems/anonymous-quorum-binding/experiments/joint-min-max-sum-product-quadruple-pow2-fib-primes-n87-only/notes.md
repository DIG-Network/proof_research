# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n87-only

- **observation:** Wall time ~1636 s total; per-schedule times scale with `C(87,5)+C(87,6)` work vs `n=86`.
- **dead_end:** None for this run — outcome extends the empirical “no collision” band for **pow2** / **fib** / **primes** on exact **`K`** through **`n=87`**.
- **question:** At what **`n`** (if any) does the first collision appear for these three schedules under exact **`K`**? Still open.
- **next:** Single-**`n=88`** probe is the next step in this thread, or pivot to **triangular** / other schedules or verifier-oracle line.
