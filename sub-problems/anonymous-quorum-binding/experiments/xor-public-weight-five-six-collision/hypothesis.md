# Hypothesis — XOR of public weights `(i+1)` collides across |S|=5 vs |S|=6

## Analogy pass (unsticking: **encoding change**)

1. **Abstract structure:** **054–060** studied **additive** **moments** **mod** **M** — homomorphic summaries that **commute** with **integer** **addition** on **selected** **weights**. **Persona** **unsticking:** change the **encoding** so the verifier’s **compact** statistic is **not** a **linear** **functional** of **indicator** **weights**.

2. **Where else:**
   - **GF(2)** **parity** and **CRC**-style **mixing** use **XOR** to **spread** **bit** **dependencies** **nonlinearly** (carry-free addition in **bits**).
   - **Cryptographic** **combining** of **blocks** (**OFB**/**CTR**-adjacent **heuristics**) uses **XOR** to **avoid** **ring** **homomorphism** onto **small** **moduli**.
   - **Error** **detection:** **XOR** **checksums** detect **some** **swap**/**duplicate** **patterns** **additive** **sums** **miss** — different **algebra**.

3. **Machinery:** For each subset **S**, define **H(S) = ⨁_{i∈S} (i+1)** (bitwise **XOR** of **public** **weights**). Ask whether **H(S₅) = H(S₆)** for **some** **|S₅|=5**, **|S₆|=6** when **n=10**.

4. **Transfer candidate:** If **no** **collision**, **XOR** **separates** **the** **two** **shells** **in** **this** **toy** — **weak** **positive** **evidence** that **non-additive** **folds** **can** **avoid** **the** **moment-mod** **attractor**. If **collision** **exists**, **XOR** **alone** **still** **fails** **as** **a** **threshold** **certificate**.

## Falsifiable claim

**n=10**, **w_i=i+1**: **either** exhibit **S₅, S₆** with **equal** **XOR** (**PASS** **on** **“collision** **exists”**), **or** **exhaustively** **verify** **no** **equal** **XOR** (**FAIL** **on** **“collision** **exists”** — i.e. **XOR** **injective** **between** **the** **two** **families** **here**).
