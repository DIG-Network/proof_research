# Results — quintuple coprime moduli, **min M_i = 4**

**Outcome:** PASS

**Setup:** Same as **079**, but **`M_i ∈ [4, 25]`** (defaults **`--min-m 4`**, **`--scan-max 25`**), pairwise coprime, lex-first **5-vs-6** collision on **(p₁ mod M₁, …, p₅ mod M₅)**.

**Finding:**

- **FIRST_COLLISION** at **(M₁,…,M₅) = (4, 5, 7, 9, 17)** with **key (0, 4, 1, 8, 10)**.
- **5-set** indices **(1,2,5,7,8)** → weights **(2,3,6,8,9)**, **penta** **(28, 194, 1492, 12050, 99868)**.
- **6-set** indices **(0,2,3,4,6,7)** → weights **(1,3,4,5,7,8)**, **penta** **(28, 164, 1072, 7460, 53968)**.

**Structural note:** **p₁ = 28** **for both** subsets — same **integer** **first** **moment** **(** **distinct** **5-tuples** **in** **078** **),** **so** **p₁ mod 4 = 0** **for** **both** **;** **higher** **moments** **align** **mod** **(5,7,9,17)** **at** **this** **key.**

**vs 060:** Triple **min4** lex-first was **(4,5,7)**. **vs 079:** **min2** lex-first was **(2,3,5,7,13)**. **Raising** **floor** **to** **4** **moves** **first** **collision** **to** **(4,5,7,9,17)** **—** **still** **small** **moduli** **(** **max** **17** **).**
