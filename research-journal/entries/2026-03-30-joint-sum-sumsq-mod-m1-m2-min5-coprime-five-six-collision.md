# 2026-03-30 — `joint-sum-sumsq-mod-m1-m2-min5-coprime-five-six-collision`

**Context:** `sub-problems/anonymous-quorum-binding/experiments/joint-sum-sumsq-mod-m1-m2-min5-coprime-five-six-collision/`

**Hypothesis:** Joint **(Σw mod M₁, Σw² mod M₂)** with **M₁,M₂ ≥ 5**, **gcd=1**, lex-first **5 vs 6** collision (**n=10**, **w_i=i+1**).

**Outcome:** PASS

**Key finding:** First hit **(5, 6)**, key **(1, 1)** — **5-set (1,4,6,7,8)** vs **6-set (0..5)**. **31≡21≡1 (mod 5)**, **223≡91≡1 (mod 6)**. Rhymes with **057**: first coprime pair above floor is **(m, m+1)** for **m=4** and **m=5**.

**Implications:**

- **Raising min modulus** under **gcd=1** does **not** eliminate quick collisions; **(0..5)** six-set remains a **repeat** partner.
- Next: **triple** modular power sums or **closed-form** analysis of **(k,k+1)** hits.

**Analogy pass summary:** **Resolution ladder** — each floor shift moves the **first** coprime pair to **(m,m+1)** and finds a **new** 5-witness still colliding with the **same** **6-block**.
