# Results — joint-min-max-sum-product-quadruple-pow2-fib-primes-n46-50-scan

**Outcome:** **FAIL** (exit code **1**) — **hypothesis falsified**

The script’s **PASS** condition was: **at least one** of **`pow2_2^i`**, **`fibonacci`**, **`first_n_primes`** has a 5-vs-6 cross-shell collision for **some** **`n ∈ [46,50]`** on exact **`K(S) = (min w, max w, Σ w, Π w)`**. **None** of the three collides in that range. Hence **FAIL**.

## Measured fact (primary)

| Schedule | First collision `n` in `[46,50]` |
|----------|----------------------------------|
| `pow2_2^i` | **none** |
| `fibonacci` | **none** |
| `first_n_primes` | **none** |

**Triangular** was **not** scanned (**101** already gives first collision **`n=36`**).

Implementation: same as **101** — store **`C(n,5)`** keys with one witness; scan **`C(n,6)`** for membership.

## Interpretation

- **101:** **`2^i`**, **Fibonacci**, **primes** — **no** collision through **`n=45`**.
- **102:** same three schedules — **still no** collision for **`n=46..50`**.
- **Negative evidence** for early onset of **`K`** cross-shell collisions on these schedules is **strengthened** through **`n=50`**; **onset** remains **schedule-dependent** (**triangular** **`n=36`**, **squares** **`n=31`** per **099**).
