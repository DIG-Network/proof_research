# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n61-only

**Outcome:** FAIL (hypothesis: at least one of the three schedules has a 5-vs-6 cross-shell collision at `n=61`; **none** do)

## Measured outputs

| Schedule       | n   | Cross-shell collision | elapsed (s) |
|----------------|-----|------------------------|-------------|
| pow2_2^i       | 61  | no                     | 66.307      |
| fibonacci      | 61  | no                     | 60.212      |
| first_n_primes | 61  | no                     | 52.423      |

**Total wall time:** ~179.0 s (~3.0 min) on runner.

## Interpretation

Exact `K(S)=(min w, max w, Σ w, Π w)` still separates **|S|=5** from **|S|=6** for all three structured schedules at **`n=61`**, extending the negative evidence from **104** (`n∈[56,60]`) and **101–103** (earlier bands). Combined: **no** collision for these three schedules for **`n∈[11,61]`** under this `K` (triangular weights were handled separately in **101**).

**Note:** `n=61` is substantially more expensive than `n=60` (combinations grow quickly); further `n>61` scans should be budgeted explicitly.
