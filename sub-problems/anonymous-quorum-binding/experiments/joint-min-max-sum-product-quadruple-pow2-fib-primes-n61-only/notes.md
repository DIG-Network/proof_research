# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n61-only

## observation

- Per-schedule wall time at `n=61` was ~52–66 s for full 5-then-6 enumeration; total ~3 min for three schedules.

## insight

- The **pow2** schedule dominates runtime (largest weight magnitudes / product bit-length), yet still **no** `K` collision at `n=61`.

## question

- At what `n` (if any) does the first collision appear for **pow2** / **fibonacci** / **primes** under exact `K`? No analytic prediction here — empirical frontier now **`n=61`**.

## dead_end

- **N/A** for this folder: the hypothesis was “collision exists at 61”; result falsifies it for these three schedules, but does **not** close the general injectivity question for all `n`.
