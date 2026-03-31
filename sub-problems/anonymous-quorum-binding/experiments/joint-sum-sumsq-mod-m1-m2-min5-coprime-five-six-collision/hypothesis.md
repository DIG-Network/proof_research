# Hypothesis — joint (Σw, Σw²) with M₁,M₂ ≥ 5 and gcd(M₁,M₂)=1

## Analogy pass

1. **Abstract structure:** **057** showed that **M₁,M₂ ≥ 4** with **gcd=1** moves the lex-first collision to **(4,5)** and swaps the **5-witness** while the **6-set (0..5)** persists. We stress the **modulus floor** again to see whether collisions **track** a predictable **(m, m+1)** pattern or **break** the **initial-block 6-set** partnership.

2. **Where else:**
   - **Resolution ladder** in imaging: each step removes one class of alias until the next dominant artifact appears.
   - **Finite field towers:** raising the **conductor** / **modulus** in arithmetic statistics changes which congruences synchronize first.
   - **Pigeonhole density:** larger moduli shrink the **image** size **M₁M₂** relative to **C(10,5)+C(10,6)** labels — but **threshold collision** is about **two families**, not uniform random hashing.

3. **Machinery:** Lex scan **(M₁, M₂)** with **M₁,M₂ ≥ 5**, **gcd=1**, first **5 vs 6** collision on **(Σw mod M₁, Σw² mod M₂)**.

4. **Transfer candidate:** **m_min = 5** — first coprime lex pair is **(5,6)** (skip **(5,5)**). Record **first collision** and witnesses up to `scan_max`.

## Falsifiable claim

For **n=10**, **w_i=i+1**, **|S|∈{5,6}**, lex **(M₁,M₂)** with **5 ≤ M₁,M₂ ≤ scan_max**, **gcd=1**: report **first** collision or **INCONCLUSIVE**.
