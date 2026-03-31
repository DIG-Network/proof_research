# Hypothesis — quintuple power sums mod five pairwise-coprime moduli

## Analogy pass

1. **Abstract structure:** **059** showed **(p₁,p₂,p₃) mod (M₁,M₂,M₃)** with **gcd(M_i,M_j)=1** still hits an immediate **5-vs-6** collision at lex-first **(2,3,5)**. **078** shows **exact** **(p₁,…,p₅)** is injective on the union. We interpolate: **five** **independent** **moduli** **per** **moment** may still fold at **small** **(M₁,…,M₅)** — or the **fifth** coordinate delays the lex-first collision vs **059**.

2. **Analogues (≥3):**
   - **CRT / mixed-radix:** residues mod coprime moduli are independent in principle, but **each** coordinate is still a **quotient** of **ℤ** — small moduli still alias.
   - **Multi-sensor quantization:** Five independent ADC step sizes; collision when **all** five bins align across two subset types.
   - **059** **direct** **extension** **in** **this** **repo.**

3. **Machinery:** Lexicographic enumeration of **(M₁,…,M₅)** with **M_i ≥ min_m**, **M_i ≤ scan_max**, **pairwise** **gcd=1**; first **5-vs-6** key collision on **(p₁ mod M₁, …, p₅ mod M₅)**.

4. **Transfer seed:** Expect **lex-first** collision at **small** **primes** **/ ** **coprime** **tuple** **near** **(2,3,5,7,11)** **or** **earlier** **in** **lex** **order** **(** **e.g.** **if** **some** **composite** **fits** **)** **—** **unlikely** **the** **fifth** **moment** **prevents** **aliasing** **at** **minimal** **moduli.**

## Falsifiable claims

- **H1:** Lex-first pairwise-coprime **(M₁,…,M₅)** with **min_m=2** yields a **5-vs-6** collision within **`--scan-max`** (default chosen for runtime).
- **H2:** No collision up to **`--scan-max`** → **INCONCLUSIVE** (need larger cap).

Script prints **PASS** on first collision, **INCONCLUSIVE** if none found in range.
