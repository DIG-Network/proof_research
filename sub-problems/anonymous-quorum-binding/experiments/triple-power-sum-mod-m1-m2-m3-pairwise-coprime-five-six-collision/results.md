# Results — `triple-power-sum-mod-m1-m2-m3-pairwise-coprime-five-six-collision`

**Outcome:** PASS

**Setup:** `n = 10`, `w_i = i+1`, **|S| ∈ {5,6}**. Tag **(Σw mod M₁, Σw² mod M₂, Σw³ mod M₃)** with **pairwise coprime** **M₁,M₂,M₃** (all **≥ min_m**). Lexicographic scan.

**Run:** `python script.py --scan-max 100`

**First collision:** **`(M₁, M₂, M₃) = (2, 3, 5)`** — smallest lex triple with **min_m=2** and pairwise coprime **(2,3,5)**. Key **`(1, 1, 1)`**.

| subset | indices | Σw | Σw² | Σw³ |
|--------|---------|-----|------|------|
| 5-set | **(3, 4, 6, 8, 9)** | 35 | 271 | 2261 |
| 6-set | (0, 1, 2, 3, 4, 5) | 21 | 91 | 441 |

**Checks:** `35 ≡ 21 ≡ 1 (mod 2)`; `271 ≡ 91 ≡ 1 (mod 3)`; `2261 ≡ 441 ≡ 1 (mod 5)`.

**Interpretation:** Adding **Σw³ mod M₃** does **not**, at the **first** small coprime triple, separate **5 vs 6** shells: collision still exists at **(2,3,5)**. The **6-set (0..5)** remains a collision partner; the **5-set** is **new** relative to **054–058** witnesses.
