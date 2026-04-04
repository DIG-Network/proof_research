# Notes — joint-min-max-sum-product-quadruple-pow2-fib-primes-n91-only

- **Implementation:** At `n=91`, `C(91,5) ≈ 4.3×10^7` makes an in-RAM `dict` of 5-keys infeasible (OOM in this environment). The script builds keys in a temp SQLite file (`WITHOUT ROWID`, batched `INSERT OR IGNORE`), then scans all 6-subsets with point lookups. All four `K` components are stored as **TEXT** because Fibonacci sums and several products exceed SQLite 64-bit `INTEGER`.
- **First run:** Process was killed (exit 137) with pure in-memory approach; SQLite path fixed that.
- **Early SQLite bug:** `OverflowError` on insert until `ksum` (and ultimately all of `kmin,kmax,ksum,kprod`) were TEXT.
- **Next minimal thread step:** single-`n` probe **`n=92`** (even larger `C(n,5)` / `C(n,6)`; expect multi-hour wall and large temp DB).
