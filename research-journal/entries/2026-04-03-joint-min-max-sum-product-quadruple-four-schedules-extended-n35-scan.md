# Experiment entry — 2026-04-03 — joint-min-max-sum-product-quadruple-four-schedules-extended-n35-scan

**Path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-four-schedules-extended-n35-scan`

**Context:** anonymous-quorum-binding (toy aggregate-tag / shell separation)

**Hypothesis tested:** Each of **`2^i`**, **triangular**, **Fibonacci**, **first-`n` primes** has **some** 5-vs-6 cross-shell collision on exact **`K=(min,max,Σ,Π)`** for **some** **`n ∈ [11,35]`**.

**Outcome:** **FAIL** (hypothesis **falsified**): **no** schedule collides in the scanned band.

**Key finding:** **All four** schedules remain **collision-free** on **`K`** between **`|S|=5`** and **`|S|=6`** for **every** **`n` from 11 through 35** (exhaustive per-**`n`** set intersection). **098** had only **`n≤18`**; this **extends** the **negative** evidence to **`n=35`**. **099** showed **square** weights first fail at **`n=31`** — **onset** is **not** monotone in “how fast” weights grow in any simple way.

**Implications:**

- **Schedule-dependent** **certificates** must **cite** **`w_i`**; **“no collision up to 18”** does **not** predict **“collision by 35”**.
- **Promising** **toy** **direction:** **slow**/**structured** **schedules** may **preserve** **`K`** **separation** **longer** than **linear**/**square** **on** **this** **statistic**.

**Analogy pass summary:** See **`hypothesis.md`** — **same** **shell** **overlap** **probe** as **098**/**099**, **wider** **`n`** **for** **four** **remaining** **098** **rows**.

**Space definition:** none
