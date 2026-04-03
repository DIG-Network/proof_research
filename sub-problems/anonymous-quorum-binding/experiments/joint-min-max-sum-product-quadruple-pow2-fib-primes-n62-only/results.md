# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n62-only

**Outcome:** FAIL (hypothesis: at least one of the three schedules has a 5-vs-6 cross-shell collision at `n=62`; **none** do)

## Measured outputs

| Schedule       | n   | Cross-shell collision | elapsed (s) |
|----------------|-----|------------------------|-------------|
| pow2_2^i       | 62  | no                     | 65.965      |
| fibonacci      | 62  | no                     | 60.832      |
| first_n_primes | 62  | no                     | 51.056      |

**Total wall time:** ~177.9 s (~3.0 min) on runner.

## Interpretation

Exact `K(S)=(min w, max w, Σ w, Π w)` still separates **|S|=5** from **|S|=6** for all three structured schedules at **`n=62`**, extending the negative evidence from **105** (`n=61`) and **101–104** (earlier bands). Combined: **no** collision for these three schedules for **`n∈[11,62]`** under this `K` (triangular weights were handled separately in **101**).

**Note:** Cost grows quickly with `n`; further `n>62` scans should be budgeted explicitly.
