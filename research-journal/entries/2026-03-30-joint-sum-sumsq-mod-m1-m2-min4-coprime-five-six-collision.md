# 2026-03-30 — `joint-sum-sumsq-mod-m1-m2-min4-coprime-five-six-collision`

**Context:** `sub-problems/anonymous-quorum-binding/experiments/joint-sum-sumsq-mod-m1-m2-min4-coprime-five-six-collision/`

**Hypothesis:** Joint **(Σw mod M₁, Σw² mod M₂)** with **M₁,M₂ ≥ 4** and **gcd(M₁,M₂)=1**, lex-first **5 vs 6** collision (**n=10**, **w_i=i+1**).

**Outcome:** PASS

**Key finding:** First hit **(4, 5)**, key **(1, 1)**. **5-set** **(4,5,6,8,9)** vs **6-set** **(0..5)** — **not** the **(4,6,7,8,9)** five-set from **054–056**, though the **six-set** is unchanged. **37≡21≡1 (mod 4)**, **291≡91≡1 (mod 5)**.

**Implications:**

- **Floor 4 + coprime** moves the lex-first collision to **(4,5)** and **changes** the colliding **5-subset** while the **initial-block 6-set** remains a collision partner.
- Still **no** injective **2-coordinate** modular power-sum separator at this scale; next: **min 5** or **3** statistics.

**Analogy pass summary:** Coarse-to-fine / anti-aliasing — larger moduli can **reshuffle** which subset pairs agree first; **(0..5)** six-set stays a recurring **attractor** for **1..6** weight mass.
