# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n91-only

**Outcome:** FAIL

**Summary:** For `n=91`, exhaustive 5-vs-6 cross-shell search on exact `K=(min w, max w, Σ w, Π w)` found **no** collision for any of the three schedules (`pow2_2^i`, Fibonacci prefix, first-`n` primes). Implementation uses a temporary SQLite table for 5-subset keys (TEXT columns for all four `K` components so bigint sums/products fit); peak on-disk DB ~6.9 GiB per schedule. Measured wall times: pow2 ~5111 s, fibonacci ~4813 s, first_n_primes ~3914 s; **total ~13838 s (~3.85 h)**.

Together with experiments **101–134**, there is **no** 5-vs-6 collision for these three schedules under exact `K` for **`n ∈ [11,91]`**.
