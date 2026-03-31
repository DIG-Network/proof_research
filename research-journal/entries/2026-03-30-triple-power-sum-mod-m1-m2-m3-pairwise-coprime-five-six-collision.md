# 2026-03-30 — `triple-power-sum-mod-m1-m2-m3-pairwise-coprime-five-six-collision`

**Context:** `sub-problems/anonymous-quorum-binding/experiments/triple-power-sum-mod-m1-m2-m3-pairwise-coprime-five-six-collision/`

**Hypothesis:** Tag **(Σw mod M₁, Σw² mod M₂, Σw³ mod M₃)** with **pairwise coprime** moduli, lex scan (**n=10**, **w_i=i+1**, **|S|∈{5,6}**); first **5 vs 6** collision.

**Outcome:** PASS

**Key finding:** First hit **(2, 3, 5)**, key **(1, 1, 1)** — **5-set (3,4,6,8,9)** vs **6-set (0..5)**. Third moment **does not** break the collision at the **minimal** coprime triple **(2,3,5)**.

**Implications:**

- **Fixed-degree power-sum** modular tags remain **cheaply collidable** with **(0..5)** as partner at **small** **2·3·5** moduli.
- Next stress: **min_m ≥ 4** pairwise coprime triple scan, or **leave** this **homomorphic** line per **unsticking** after many variants.

**Analogy pass summary:** **Moments / tomography** — extra axis can resolve ambiguity, but **first** **lex** **small-mod** triple still **folds** **5 vs 6** for this weight geometry.
