# Journal entry — 2026-04-03 — joint-min-max-sum-product-quadruple-pow2-fib-primes-n51-55-scan

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-pow2-fib-primes-n51-55-scan`

**Context:** anonymous-quorum-binding (shell toy: exact **`K=(min,max,Σ,Π)`**, shells 5 vs 6)

**Hypothesis tested:** At least one of **`pow2_2^i`**, **Fibonacci prefix**, **first `n` primes** has a 5-vs-6 cross-shell collision for some **`n ∈ [51,55]`**.

**Outcome:** **FAIL**

**Key finding:** **None** of the three schedules collides in **`[51,55]`**. Together with **101** (**`n≤45`**) and **102** (**`n=46..50`**), there is **no** such collision for **any** **`n ∈ [11,55]`** on these three weight schedules under exact **`K`**.

**Implications:**

- Strengthens **negative** evidence that **`K`** cross-shell collisions are **not** universal at modest **`n`**; onset is **encoding-dependent** (cf. **triangular** **`n=36`**, **squares** **`n=31`**).
- Optional next band would be **`n>55`** (compute cost grows with **`C(n,5)+C(n,6)`**).

**Analogy pass summary:** Same structure as **102** — extend **`n`** window for schedules that stayed clean through **`n=50`**.

**Space-definition:** none
