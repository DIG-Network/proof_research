# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n84-only

- **observation:** Wall time ~1298 s total; per-schedule times scale with `C(84,5)+C(84,6)` work vs `n=83`.
- **dead_end:** None for this run — outcome extends the empirical “no collision” band for **pow2** / **fib** / **primes** on exact **`K`** through **`n=84`**.
- **question:** At what **`n`** (if any) does the first collision appear for these three schedules under exact **`K`**? Still open.
- **next:** Single-**`n=85`** probe is the next step in this thread, or pivot to **triangular** / other schedules or verifier-oracle line.
