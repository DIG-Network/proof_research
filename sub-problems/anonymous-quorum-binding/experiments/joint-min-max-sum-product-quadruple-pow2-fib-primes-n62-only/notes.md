# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n62-only

## observation

Single-`n` probe at **`n=62`** completes in ~**178** s wall time for all three schedules — comparable to **105** at **`n=61`** (~**179** s), with per-schedule times within a few seconds of the prior step.

## insight

The **`pow2` / `fib` / `primes`** regime under exact **`K=(min,max,Σ,Π)`** remains collision-free for 5-vs-6 cross-shell keys through **`n=62`**; the next meaningful cost jump is **`n=63`** or a band scan **`63..65`**.

## question

At what **`n`** (if any) does the first collision appear for **`pow2_2^i`** alone under this **`K`**, or do these structured weights admit a proof of separation? (Empirical only so far.)

