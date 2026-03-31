# Hypothesis — joint (Σw, Σw²) with M₁,M₂ ≥ 4 and gcd(M₁,M₂)=1

## Analogy pass

1. **Abstract structure:** Prior runs **054–056** show **small moduli** (2, 2), (3, 3), (2, 3) make the **same** 5-shell vs 6-shell pair collide on **two modular statistics**. We ask whether **raising the floor** on both moduli — while keeping **coprimality** to avoid shared-factor coupling — **postpones** the lex-first collision or **changes** the witness.

2. **Where else:**
   - **Coarse graining → fine graining** in renormalization: larger **period** in a quotient space can separate states that looked identical mod a small period.
   - **Nyquist / aliasing:** if “frequency” of the summary is too low, distinct signals fold together; **increasing** effective period can **unfold** until another resonance appears.
   - **Grid refinement** in numerical PDE: coarser mesh smears distinct features; finer mesh resolves them until the next degeneracy.

3. **Machinery:** Lex scan over **(M₁, M₂)** with **M₁,M₂ ≥ m_min**, **gcd(M₁,M₂)=1**, find first **5 vs 6** collision on **(Σw mod M₁, Σw² mod M₂)**.

4. **Transfer candidate:** Set **m_min = 4** (excludes parity-only first coordinate from **056**’s **M₁=2** and excludes **M=3** moduli that matched **Σw²** for the recurring witness). **Hypothesis (falsifiable):** the **lex-first** coprime pair with **min ≥ 4** is **not** **(4,5)** at the same witness, or collision appears only at a **larger** **(M₁,M₂)** — we **measure** empirically up to `scan_max`.

## Falsifiable claim

For **n=10**, **w_i=i+1**, **|S|∈{5,6}**, enumerate lex **(M₁,M₂)** with **4 ≤ M₁,M₂ ≤ scan_max**, **gcd=1**. Report **first** collision or **INCONCLUSIVE** if none in range.
