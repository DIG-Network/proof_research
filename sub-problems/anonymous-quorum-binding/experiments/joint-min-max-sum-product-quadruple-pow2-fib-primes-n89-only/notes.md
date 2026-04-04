# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n89-only

- **observation:** Wall time ~1918 s total; per-schedule times scale with `C(89,5)+C(89,6)` work vs `n=88`.
- **dead_end:** None for this run — outcome extends the empirical “no collision” band for **pow2** / **fib** / **primes** on exact **`K`** through **`n=89`**.
- **question:** At what **`n`** (if any) does the first collision appear for these three schedules under exact **`K`**? Still open.
- **next:** Single-**`n=90`** probe is the next step in this thread, or pivot to **triangular** / other schedules or verifier-oracle line.
