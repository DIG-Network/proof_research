# Notes — joint-min-max-sum-product-quadruple-weight-schedules-minimal-n-scan

- **Observation:** Reversing the linear weights (`n-i`) does not change the multiset `{1,…,11}`; hence **same** collision at `n=11` as **097**.
- **Observation:** **Squares**, **powers of two**, **triangular**, **Fibonacci**, and **primes** schedules yield **no** cross-shell intersection at `n=11` in the exhaustive shell enumeration.
- **Question:** For those five schedules, does a cross-shell collision ever occur for some `n>18`, and what is the true minimal `n`? Not resolved here (bounded scan only).
- **Dead end (for this run):** Treating “minimal `n` equals 11” as a property of the statistic **alone** — **false**; it depends on the chosen **`w_i`** schedule.
- **Next step:** If needed, extend `n_hi` or target one schedule (e.g. squares) for a dedicated minimal-`n` hunt; or relate growth rate of `w_i` to when product magnitude makes `K` collisions rare vs inevitable.
