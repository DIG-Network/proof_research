# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n51-55-scan

**Outcome:** **FAIL** (exit code **1**) — **hypothesis falsified**

The script’s **PASS** condition was: **at least one** of **`pow2_2^i`**, **`fibonacci`**, **`first_n_primes`** has a 5-vs-6 cross-shell collision for **some** **`n ∈ [51,55]`** on exact **`K(S) = (min w, max w, Σ w, Π w)`**. **None** of the three collides in that range. Hence **FAIL**.

## Measured fact (primary)

| Schedule | First collision `n` in `[51,55]` |
|----------|----------------------------------|
| `pow2_2^i` | **none** |
| `fibonacci` | **none** |
| `first_n_primes` | **none** |

**Triangular** was **not** scanned (unchanged from **102**).

Implementation: same as **101**/**102** — store **`C(n,5)`** keys with one witness; scan **`C(n,6)`** for membership.

**Approximate wall time (this run):** full script **~305 s** (**~5.1 min**) for all three schedules × five values of **`n`** (dominated by **`n=55`** per-schedule passes).

## Interpretation

- **101:** **`2^i`**, **Fibonacci**, **primes** — **no** collision through **`n=45`**.
- **102:** same three — **no** collision **`n=46..50`**.
- **103:** same three — **still no** collision **`n=51..55`**.
- **Combined:** **no** 5-vs-6 cross-shell collision on exact **`K`** for these three schedules for **any** **`n ∈ [11,55]`** (given **101**/**102**/**103**).

Onset of **`K`** cross-shell collisions remains **schedule-dependent** (**triangular** **`n=36`**, **squares** **`n=31`** per **099**).
