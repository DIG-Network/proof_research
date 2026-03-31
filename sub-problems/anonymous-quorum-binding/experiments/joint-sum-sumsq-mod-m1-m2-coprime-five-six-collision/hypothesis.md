# Hypothesis — joint (Σw, Σw²) mod (M₁,M₂) with gcd(M₁,M₂)=1

## Analogy pass

1. **Abstract structure:** Two modular residues are **independent observables** of a hidden subset only if the **Chinese remainder** intuition applies: information in **Z/M₁Z × Z/M₂Z** factors cleanly when **M₁ ⊥ M₂**. Pairs with a **common factor** can encode **aligned** congruences (e.g. both even), collapsing effective dimension — as in **054**’s **(2,2)** pathology.

2. **Where else:**
   - **CRT / simultaneous congruences:** Coprime moduli give an isomorphism **Z/M₁M₂Z ≅ Z/M₁Z × Z/M₂Z** for a **single** integer; here we have **two different** statistics (**Σw** vs **Σw²**), but **coprimality** still reduces **shared modulus artifacts**.
   - **Signal processing:** Two channels sampled at **incommensurate** rates avoid **aliasing** at shared small periods.
   - **Lattice density:** **gcd(a,b)>1** lets a sublattice of **Z²** have smaller index along a rational direction — analogous to **redundant** modular constraints.

3. **Machinery:** Restrict **(M₁,M₂)** to **coprime** pairs; scan **lexicographically** for the **first** 5-set vs 6-set collision on **(Σw mod M₁, Σw² mod M₂)**.

4. **Transfer candidate:** After **054** **(2,2)** and **055** **(3,3)**, test whether **gcd=1** pushes the **lex-first** collision to a **larger** pair or **different** witness (bounded scan).

## Falsifiable claim

For **n=10**, **w_i=i+1**, **|S|∈{5,6}**, enumerate **lex** **(M₁,M₂)** with **2≤M₁,M₂≤scan_max** and **gcd(M₁,M₂)=1**. Record the **first** collision; if none in range, **INCONCLUSIVE**.
