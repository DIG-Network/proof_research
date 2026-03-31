# Results — `joint-sum-sumsq-mod-m1-m2-min4-coprime-five-six-collision`

**Outcome:** PASS

**Setup:** `n = 10`, `w_i = i+1`, all `|S| ∈ {5,6}`. Lex **(M₁, M₂)** with **4 ≤ M₁, M₂ ≤ scan_max**, **`gcd(M₁,M₂) = 1`**. Joint key **(Σw mod M₁, Σw² mod M₂)**.

**Run:** `python script.py --scan-max 400`

**First collision:** **`(M₁, M₂) = (4, 5)`**, key **`(1, 1)`**.

| subset | indices | Σw | Σw² |
|--------|---------|-----|------|
| 5-set | **(4, 5, 6, 8, 9)** | 37 | 291 |
| 6-set | (0, 1, 2, 3, 4, 5) | 21 | 91 |

**Checks:** `37 ≡ 21 ≡ 1 (mod 4)`; `291 ≡ 91 ≡ 1 (mod 5)`.

**Contrast with 054–056:** The **6-set** is still the **initial block** **(0..5)**, but the **5-set** is **not** the previous heavy-tail **(4,6,7,8,9)** — here **index 5** is included and **7** excluded (**(4,5,6,8,9)**). So **raising** **min modulus to 4** with **coprimality** **delays** collision to the **first** admissible pair **(4,5)** and **changes** the colliding 5-subset while keeping the same 6-subset.
