# Results — `triple-power-sum-mod-m1-m2-m3-pairwise-coprime-min4-five-six-collision`

**Outcome:** PASS

**Setup:** Same triple tag as **059** — **(Σw mod M₁, Σw² mod M₂, Σw³ mod M₃)** with **pairwise coprime** **M₁,M₂,M₃**, **4 ≤ Mᵢ ≤ scan_max**, lex order.

**Run:** `python script.py --scan-max 200`

**First collision:** **`(M₁, M₂, M₃) = (4, 5, 7)`**, key **`(1, 1, 0)`**.

| subset | indices | Σw | Σw² | Σw³ |
|--------|---------|-----|------|------|
| 5-set | **(2, 3, 5, 6, 8)** | 29 | 191 | 1379 |
| 6-set | (0, 1, 2, 3, 4, 5) | 21 | 91 | 441 |

**Checks:** `29 ≡ 21 ≡ 1 (mod 4)`; `191 ≡ 91 ≡ 1 (mod 5)`; `1379 ≡ 441 ≡ 0 (mod 7)`.

**Contrast 059:** **059** used **min_m=2**, first triple **(2,3,5)**. Here **min_m=4** yields first admissible lex triple **(4,5,7)** (pairwise coprime; **(4,5,6)** fails **gcd(4,6)>1**, etc.). **6-set (0..5)** remains a collision partner; **5-set** is new vs **059**’s **(3,4,6,8,9)**.
