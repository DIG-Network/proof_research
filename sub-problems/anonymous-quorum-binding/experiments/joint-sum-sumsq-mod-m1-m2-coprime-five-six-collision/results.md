# Results — `joint-sum-sumsq-mod-m1-m2-coprime-five-six-collision`

**Outcome:** PASS

**Setup:** `n = 10`, `w_i = i+1`, all `|S| ∈ {5,6}`. Lexicographic `(M₁, M₂)` with `2 ≤ M₁, M₂ ≤ scan_max`, **`gcd(M₁,M₂) = 1`** only. Joint key `(Σw mod M₁, Σw² mod M₂)`.

**Run:** `python script.py --scan-max 200` (first hit unchanged for larger cap since it occurs at minimum coprime lex pair).

**First collision:** `(M₁, M₂) = (2, 3)`, `gcd = 1`, key **`(1, 1)`**.

| subset | indices | Σw | Σw² |
|--------|---------|-----|------|
| 5-set | (4, 6, 7, 8, 9) | 39 | 319 |
| 6-set | (0, 1, 2, 3, 4, 5) | 21 | 91 |

**Checks:** `39 ≡ 21 ≡ 1 (mod 2)`; `319 ≡ 91 ≡ 1 (mod 3)`.

**Interpretation:** **Coprimality** removes pairs like **(2,2)** and **(3,3)** from the scan, but the **lex-first admissible** pair **(2,3)** still collides on the **same** 5-shell vs 6-shell witness as **054/055**. So **CRT-style independence of moduli** does not stop **small** coprime pairs from agreeing on **both** statistics for this fixed weight geometry.
