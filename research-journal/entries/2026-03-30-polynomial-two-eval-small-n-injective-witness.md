# Entry — 2026-03-30 — polynomial-two-eval-small-n-injective-witness

- **Date:** 2026-03-30
- **Experiment:** `sub-problems/anonymous-quorum-binding/experiments/polynomial-two-eval-small-n-injective-witness/`
- **Context:** `anonymous-quorum-binding`

## Hypothesis tested

**n=10,** **p=97:** **when** **2^n** **<** **p²,** **some** **Lagrange** **two**-**evaluation** **map** **is** **injective** **on** **{0,1}^n** **(exhaustive** **(r1,r2)** **search).**

## Outcome

**PASS** **—** **first** **witness** **(10,26);** **95** **injective** **pairs** **out** **of** **3741;** **(90,91)** **still** **collides** **on** **hypercube.**

## Key finding

**024’s** **“two** **evals** **collide”** **is** **consistent** **with** **information** **theory** **(n=16)** **and** **does** **not** **imply** **non-injectivity** **for** **all** **(n,p)** **—** **small** **n** **admits** **good** **(r1,r2).**

## Implications

- **Digest** **should** **qualify** **the** **polynomial** **probe** **thread:** **constant** **k** **evals** **hit** **dimension** **wall** **as** **n** **grows** **at** **fixed** **p;** **small** **n** **toys** **can** **misread** **as** **“k** **points** **always** **ambiguous.”**
- **Main** **binding** **gap** **unchanged:** **large** **validator** **sets** **still** **need** **scaling** **p** **or** **k** **or** **non**-**evaluation** **structure.**

## Analogy pass summary

**Capacity** **vs** **structured** **encoder** **—** **same** **theme** **as** **RIP** **/ ** **incoherence** **in** **sensing.**
