# 2026-03-30 — `joint-sum-sumsq-mod-m1-m2-coprime-five-six-collision`

**Context:** `sub-problems/anonymous-quorum-binding/experiments/joint-sum-sumsq-mod-m1-m2-coprime-five-six-collision/`

**Hypothesis:** Restrict joint tag **(Σw mod M₁, Σw² mod M₂)** to **gcd(M₁,M₂)=1** (CRT-style independence of moduli) and scan **lex** from **M₁,M₂≥2** for first **5 vs 6** collision (**n=10**, **w_i=i+1**).

**Outcome:** PASS

**Key finding:** Lex-first coprime pair is **(2,3)**, key **(1,1)** — **same** witnesses **(4,6,7,8,9)** vs **(0..5)** as **054/055**: parity matches mod **2**, **Σw²** matches mod **3**. **Coprimality** drops **(2,2)** and **(3,3)** but **not** this collision.

**Implications:**

- **gcd=1** is **insufficient** to separate these shells with **two** small modular statistics on fixed weights.
- Next stress: **min(M₁,M₂)≥4** with **gcd=1**, or **third** residue.

**Analogy pass summary:** CRT / incommensurate sampling / lattice subindex — **coprime** moduli avoid **shared factor** redundancy; **(2,3)** is the minimal such pair and still aligns both statistics for the recurring witness.
