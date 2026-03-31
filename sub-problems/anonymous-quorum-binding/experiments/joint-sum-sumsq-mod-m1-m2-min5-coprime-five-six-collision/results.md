# Results — `joint-sum-sumsq-mod-m1-m2-min5-coprime-five-six-collision`

**Outcome:** PASS

**Setup:** `n = 10`, `w_i = i+1`, all `|S| ∈ {5,6}`. Lex **(M₁, M₂)** with **5 ≤ M₁, M₂ ≤ scan_max**, **`gcd(M₁,M₂) = 1`**. Joint **(Σw mod M₁, Σw² mod M₂)**.

**Run:** `python script.py --scan-max 500`

**First collision:** **`(M₁, M₂) = (5, 6)`**, key **`(1, 1)`** (first coprime lex pair with both ≥5 is **(5,6)** — **(5,5)** skipped).

| subset | indices | Σw | Σw² |
|--------|---------|-----|------|
| 5-set | **(1, 4, 6, 7, 8)** | 31 | 223 |
| 6-set | (0, 1, 2, 3, 4, 5) | 21 | 91 |

**Checks:** `31 ≡ 21 ≡ 1 (mod 5)`; `223 ≡ 91 ≡ 1 (mod 6)`.

**Pattern with 057:** **057** gave **(4,5)** as first **min 4** coprime hit; **058** gives **(5,6)** as first **min 5** coprime hit — consecutive **(m, m+1)** with **gcd=1**. The **6-set (0..5)** is again one side of the collision; the **5-set** is **neither** **057**’s **(4,5,6,8,9)** nor **054–056**’s **(4,6,7,8,9)**.
