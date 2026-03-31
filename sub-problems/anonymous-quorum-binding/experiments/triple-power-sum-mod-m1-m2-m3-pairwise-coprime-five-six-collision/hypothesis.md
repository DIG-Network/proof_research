# Hypothesis — triple (Σw, Σw², Σw³) mod pairwise coprime (M₁,M₂,M₃)

## Analogy pass

1. **Abstract structure:** **054–058** collapse **5 vs 6** shells using **one** or **two** modular power sums on fixed public weights. **Moment matching:** a distribution on **k** points is not determined by **d** moments for **d** too small; adding **another** moment **raises** the **algebraic degree** of the summary map.

2. **Where else:**
   - **Method of moments** / **cumulants:** each higher moment can separate mixtures that share lower moments.
   - **Tomography:** extra **projection** (extra measurement axis) breaks **ghost** ambiguities from **underdetermined** **2D** views.
   - **CRT product ring:** **Z/M₁Z × Z/M₂Z × Z/M₃Z** with **pairwise coprime** **Mᵢ** avoids **shared** **period** artifacts between coordinates (same motivation as **056**, extended to **3** factors).

3. **Machinery:** Tag each subset **S** by **(Σw mod M₁, Σw² mod M₂, Σw³ mod M₃)** with **gcd(Mᵢ,Mⱼ)=1** for **i≠j**. Lex-scan **(M₁,M₂,M₃)** from a minimum bound; report **first** **5-set vs 6-set** collision or bounded **INCONCLUSIVE**.

4. **Transfer candidate:** If **two** coordinates still agree for **(0..5)** **vs** some **5-set**, **Σw³** may **break** that alignment at the **first** small coprime triple — **or** collision may persist (data).

## Falsifiable claim

For **n=10**, **w_i=i+1**, **|S|∈{5,6}**, lex **(M₁,M₂,M₃)** with **min ≤ Mᵢ ≤ scan_max** and **pairwise coprime**, find **first** collision on the **triple** tag, or report **INCONCLUSIVE** if none in range.
