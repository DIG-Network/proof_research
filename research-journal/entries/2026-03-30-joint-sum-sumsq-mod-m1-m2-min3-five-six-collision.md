# 2026-03-30 — `joint-sum-sumsq-mod-m1-m2-min3-five-six-collision`

**Context:** `sub-problems/anonymous-quorum-binding/experiments/joint-sum-sumsq-mod-m1-m2-min3-five-six-collision/`

**Hypothesis:** After **054**’s lex-first **(2,2)** collision (redundant parity for **w² mod 2**), require **M₁, M₂ ≥ 3** and scan lexicographic pairs for the first **5-set vs 6-set** collision on **(Σw mod M₁, Σw² mod M₂)** with **n=10**, **w_i=i+1**.

**Outcome:** PASS

**Key finding:** First collision is **(M₁,M₂)=(3,3)**, key **(0,1)** — same witness 5-set **(4,6,7,8,9)** vs 6-set **(0..5)** as **054**: **39≡21≡0 (mod 3)**, **319≡91≡1 (mod 3)**. Excluding **M<3** removes coordinate redundancy at 2 but does **not** avoid an immediate **mod-3** joint collision on this geometry.

**Implications:**

- Small **joint** modular tags still collapse quickly; next scans might use **coprime** moduli, **larger min**, or a **third** statistic.
- The **heavy-tail vs initial-block** shell pair is a recurring cheap collision witness in this toy.

**Analogy pass summary:** Redundant observables (Bernoulli mean/variance); gauge duplication; **rank** of discrete summary map — **min modulus 3** restores **independent-looking** coordinates mod small primes but **3** still aligns both sums for this pair.
