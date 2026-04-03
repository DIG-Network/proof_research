# Results — joint-min-max-sum-product-quadruple-weight-schedules-minimal-n-scan

**Outcome:** **PASS**

**Setup:** Exact `K(S)=(min w_i, max w_i, Σ w_i, Π w_i)` on shells `|S|∈{5,6}`. Seven deterministic schedules over validator indices `0..n-1`, checked at **`n=11`** and scanned for first collision in **`n∈[11,18]`**.

**Findings:**

- **`w_i=i+1`** and **`w_i=n-i`** (reverse linear): **collision at `n=11`**, same sample key **`(1,11,31,2640)`** (reverse is the same multiset as linear, so identical `K` statistics).
- **`w_i=(i+1)²`, `w_i=2^i`, triangular `w_i=(i+1)(i+2)/2`, first 11 Fibonacci numbers, first 11 primes:** **no** 5-vs-6 cross-shell collision at **`n=11`**. In the bounded scan **`[11,18]`**, **no** collision was found for these five schedules (first collision `n` reported as `None` in-range).

**Conclusion:** The **`n=11`** onset for exact quadruple shell collision established under **`w_i=i+1`** (**097**) is **not universal** across public weight schedules; several natural schedules avoid any cross-shell collision at eleven validators (and through `n=18` in this scan).
