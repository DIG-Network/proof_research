# Results — joint-min-max-sum-product-quadruple-four-schedules-extended-n45-scan

**Outcome:** **FAIL** (exit code **1**) — **hypothesis falsified**

The script’s **PASS** condition was: **every** of the four schedules has a 5-vs-6 cross-shell collision for **some** `n ∈ [11,45]`. **Three** schedules still have **no** collision in that range; only **triangular** collides (first at **`n=36`**). Hence **FAIL** under the stated convention.

## Measured fact (primary)

For exact **`K(S) = (min w, max w, Σ w, Π w)`**, **`|S| ∈ {5,6}`**:

| Schedule | First collision `n` in `[11,45]` |
|----------|----------------------------------|
| `pow2_2^i` | **none** |
| `triangular_(i+1)(i+2)/2` | **`n=36`** |
| `fibonacci` | **none** |
| `first_n_primes` | **none** |

**Triangular witness** at **`n=36`:**

- **`K = (1, 666, 1576, 17446136400)`**
- **5-set** indices **`(0, 20, 23, 26, 35)`** — weights **`[1, 231, 300, 378, 666]`**
- **6-set** indices **`(0, 1, 10, 19, 34, 35)`** — weights **`[1, 3, 66, 210, 630, 666]`**

Implementation: build **`C(n,5)`** keys with one witness per key; scan **`C(n,6)`** and test membership (equivalent to full set intersection, lower peak memory than storing all 6-keys).

## Interpretation

- **100** had **no** collision for any of the four through **`n=35`**.
- **Triangular** is the **first** of these four to **lose** **`K`** separation between **5**- and **6**-shells, at **`n=36`** — **between** **square** weights (**099**, first at **`n=31`**) and **still-separated** **`2^i`**, **Fibonacci**, **primes** through **`n=45`**.
- **Onset** remains **strongly schedule-dependent**; extending **`n`** does **not** collapse all structured schedules on the same band.
