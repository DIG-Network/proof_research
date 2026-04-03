# Results — joint-min-max-sum-product-quadruple-four-schedules-extended-n35-scan

**Outcome:** **FAIL** (exit code **1**) — **hypothesis falsified**

The script’s **PASS** condition was: **every** of the four schedules has a 5-vs-6 cross-shell collision for **some** `n ∈ [11,35]`. **None** of the four exhibited any collision in that entire range, so the run **FAIL**s under the stated convention (same as **099** when a “no collision” hypothesis is false).

## Measured fact (primary)

For exact **`K(S) = (min w, max w, Σ w, Π w)`**, **`|S| ∈ {5,6}`**:

| Schedule | First collision `n` in `[11,35]` |
|----------|-------------------------------------|
| `pow2_2^i` | **none** |
| `triangular_(i+1)(i+2)/2` | **none** |
| `fibonacci` | **none** |
| `first_n_primes` | **none** |

Exhaustive check per `n`: build all `C(n,5)` and `C(n,6)` keys, intersect sets.

## Interpretation

- **098** had only **`n ≤ 18`** for these four — **no** collision there.
- **099** found **square** weights first collide at **`n=31`**.
- Here, **`2^i`**, **triangular**, **Fibonacci**, and **first-`n` primes** still **separate** the two shells on **`K`** through **`n=35`** in this toy scan.

So **onset of `K`-collision is highly schedule-dependent**: some growth laws remain collision-free on **`[11,35]`** while **linear** fails at **`11`** and **squares** at **`31`**.
