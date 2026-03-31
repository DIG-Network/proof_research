# 2026-03-30 — `triple-power-sum-mod-m1-m2-m3-pairwise-coprime-min4-five-six-collision`

**Context:** `sub-problems/anonymous-quorum-binding/experiments/triple-power-sum-mod-m1-m2-m3-pairwise-coprime-min4-five-six-collision/`

**Hypothesis:** Same as **059** but **M₁,M₂,M₃ ≥ 4** and **pairwise coprime**; lex-first **5 vs 6** collision on **(Σw, Σw², Σw³)**.

**Outcome:** PASS

**Key finding:** First triple **(4, 5, 7)**, key **(1, 1, 0)** — **5-set (2,3,5,6,8)** vs **6-set (0..5)**. Excluding **moduli 2** and **3** moves the **first** hit to **(4,5,7)** but **does not** remove **quick** collisions or the **(0..5)** partner.

**Implications:**

- **059** **+** **floor-4** **triple** still **PASS** at **small** **product** **4·5·7**; diminishing returns for **another** **min_m** tweak without **new** **encoding**.
- Digest **notes.md** flags **unsticking:** consider **pivot** off **pure** **moment** **mod** **scans**.

**Analogy pass summary:** **Band-pass** on **moduli** — drops **low** **periods** but **first** **coprime** **triple** **(4,5,7)** **still** **folds** **5 vs 6** with **initial** **six**-**block**.
