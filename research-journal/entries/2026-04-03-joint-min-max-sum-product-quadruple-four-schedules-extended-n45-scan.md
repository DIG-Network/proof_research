# Experiment entry — 2026-04-03 — joint-min-max-sum-product-quadruple-four-schedules-extended-n45-scan

**Path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-four-schedules-extended-n45-scan`

**Context:** anonymous-quorum-binding (toy aggregate-tag / shell separation)

**Hypothesis tested:** Each of **`2^i`**, **triangular**, **Fibonacci**, **first-`n` primes** has **some** 5-vs-6 cross-shell collision on exact **`K=(min,max,Σ,Π)`** for **some** **`n ∈ [11,45]`**.

**Outcome:** **FAIL** (hypothesis **falsified**): **three** schedules (**pow2**, **Fibonacci**, **primes**) have **no** collision through **`n=45`**; **triangular** first collides at **`n=36`**.

**Key finding:** **Extends** **100** (`n≤35`). **Triangular** **`(i+1)(i+2)/2`** is the **first** of the four **098** rows to **merge** **5**- and **6**-shells on **`K`**, at **`n=36`**, with explicit witness **`K=(1,666,1576,17446136400)`**. **`2^i`**, **Fibonacci**, **primes** still **separate** through **`n=45`**. **Onset** ordering vs **099** (**squares** at **`n=31`**) is **non-monotone** in naive “growth rate”.

**Implications:**

- **Toy** claims must **name** **`w_i`** and **range** of **`n`**; **“no collision to 35”** did **not** imply **“no collision to 45”** for **triangular**.
- **Next** **band** for **remaining** **three** schedules: **`n=46..50`** or **targeted** search if **full** **scan** is **heavy**.

**Analogy pass summary:** See **`hypothesis.md`** — same **shell** probe as **100**, **`n_hi=45`**, **memory-efficient** **6-scan** against **5-key** map.

**Space definition:** none
