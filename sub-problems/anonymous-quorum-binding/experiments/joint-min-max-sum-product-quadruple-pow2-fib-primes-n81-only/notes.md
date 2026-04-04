# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n81-only

- **observation:** Single-`n` step from **124** (`n=80` → `n=81`); `C(81,6)/C(80,6) = 76/75` multiplicative growth in 6-subset enumeration vs `n=80`.
- **observation:** Per-schedule times increased modestly vs **124** (~997 s total wall vs ~919 s).
- **dead_end:** Hypothesis “at least one schedule collides at `n=81`” is **falsified** for **pow2** / **fib** / **primes** on this exact **`K`**.
- **question:** **`n=82`** is the next single-`n` probe; cost scales again with **`C(n,6)`**.
