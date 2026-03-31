# Hypothesis — triple power sums mod pairwise coprime (M₁,M₂,M₃), all Mᵢ ≥ 4

## Analogy pass

1. **Abstract structure:** **059** showed the **lex-first** pairwise-coprime triple **(2,3,5)** still admits a **5 vs 6** collision on **(Σw, Σw², Σw³)**. **057/058** showed raising **min modulus** on **two** coordinates shifts the **first** hit to **(m,m+1)**-style pairs. Here we **exclude moduli < 4** on **all three** axes to avoid **2,3** residue classes that make **(0..5)** especially **synchronizable**.

2. **Where else:**
   - **Band-pass filtering:** drop **low-frequency** modes that dominate **alias** structure.
   - **Prime-lattice sieving:** forbidding **small** **prime** **factors** in **modulus** choice changes **which** **congruences** **activate** first.
   - **Numerical stability:** larger **moduli** **spread** **wrapped** **moments** before **wrap** **coincidence**.

3. **Machinery:** Same **triple** tag as **059**, lex scan with **M₁,M₂,M₃ ≥ 4** and **pairwise coprime**; report **first** **5 vs 6** collision or bounded **INCONCLUSIVE**.

4. **Transfer candidate:** If **min 4** delays collision past a reasonable **scan_max**, we get **evidence** that **three** **moments** **can** **separate** shells **until** **moduli** grow — if **PASS** at **small** **(4,*,*)** triple, same **negative** **binding** **story** **continues**.

## Falsifiable claim

**n=10**, **w_i=i+1**, **|S|∈{5,6}**: lex-first collision for **pairwise-coprime** **(M₁,M₂,M₃)** with **4 ≤ Mᵢ ≤ scan_max**, or **INCONCLUSIVE** if none.
