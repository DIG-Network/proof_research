# Results — `joint-sum-sumsq-mod-m1-m2-min3-five-six-collision`

**Outcome:** PASS

**Setup:** `n = 10`, `w_i = i+1`, all `|S| = 5` and `|S| = 6` subsets. Search lexicographic `(M₁, M₂)` with `M₁, M₂ ∈ [3, scan_max]` (default `scan_max = 80`; verification run used `120` — first hit still `(3,3)`).

**First collision:** `(M₁, M₂) = (3, 3)`, key `(0, 1)`.

| subset | indices | Σw | Σw² |
|--------|---------|-----|------|
| 5-set | (4, 6, 7, 8, 9) | 39 | 319 |
| 6-set | (0, 1, 2, 3, 4, 5) | 21 | 91 |

**Checks:** `39 ≡ 21 ≡ 0 (mod 3)`, `319 ≡ 91 ≡ 1 (mod 3)`.

**Command:** `python script.py --scan-max 120`

**Interpretation:** Excluding `M < 3` removes the trivial `(2,2)` parity redundancy from **054**, but the **same** 5-shell vs 6-shell witness already collides at **`(3,3)`** via divisibility by 3 on sums and matching quadratic residues mod 3. So “non-redundant moduli” in the sense of **min ≥ 3** does **not** yield injective joint tags in this small-mod scan.
