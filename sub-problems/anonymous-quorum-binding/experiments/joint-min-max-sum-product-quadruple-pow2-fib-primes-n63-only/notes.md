# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n63-only

## observation

Single-`n` probe at `n=63` mirrors **106** (`n=62`): same exhaustive 5-shell then 6-shell scan per schedule; no witness found for any of the three.

## insight

Combinatorial cost grows with `C(n,5)` and `C(n,6)`; `n=63` is still tractable here (~3 min wall) but the next integer step will be noticeably more expensive — budget explicitly before `n=64`/`n=65` band scans.

## question

Does a collision for **pow2** / **fib** / **primes** ever appear for this **`K`** at some larger `n`, or does this triple remain separated through a much wider band? No theoretical certificate from this experiment alone.

## dead_end

None new — **FAIL** only falsifies the “at least one collides at `n=63`” claim, not the broader summary statistic as a threshold witness.
