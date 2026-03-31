# 2026-03-30 — `xor-public-weight-five-six-collision`

**Context:** `sub-problems/anonymous-quorum-binding/experiments/xor-public-weight-five-six-collision/`

**Hypothesis (unsticking — encoding change):** For **n=10**, **w_i=i+1**, **H(S)=⨁_{i∈S} w_i**. Does some **|S|=5** and **|S|=6** share the same **H**?

**Outcome:** PASS

**Key finding:** **H=7** for **5-set (4,5,6,8,9)** and **6-set (0..5)** — **same** **5-set** **as** **057**’s **modular** **witness**, **same** **recurring** **six-block**.

**Implications:**

- **Bitwise** **XOR** **does** **not** **separate** **these** **shells** **here**; **cheap** **public** **scalar** **combines** **(additive** **or** **XOR)** **remain** **unsafe** **as** **stand-alone** **threshold** **tags** **in** **this** **toy**.
- **Next:** **binding** **must** **tie** **to** **commitment** **/ ** **signatures**, **use** **non-public** **weights,** **or** **leave** **scalar** **family**.

**Analogy pass summary:** **GF(2)**-style **mixing** **vs** **additive** **moments** — **still** **collides** **on** **structured** **initial-block** **vs** **tail** **geometry**.
