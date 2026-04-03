# Journal entry — 2026-04-03 — joint-min-max-sum-product-quadruple-pow2-fib-primes-n56-60-scan

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-pow2-fib-primes-n56-60-scan`

**Context:** anonymous-quorum-binding (shell toy: exact **`K=(min,max,Σ,Π)`**, shells 5 vs 6)

**Hypothesis tested:** At least one of **`pow2_2^i`**, **Fibonacci prefix**, **first `n` primes** has a 5-vs-6 cross-shell collision for some **`n ∈ [56,60]`**.

**Outcome:** **FAIL**

**Key finding:** **None** of the three schedules collides in **`[56,60]`**. Together with **101** (**`n≤45`**) and **102**/**103** (**`n=46..55`**), there is **no** such collision for **any** **`n ∈ [11,60]`** on these three weight schedules under exact **`K`**.

**Implications:**

- Further strengthens encoding-dependent onset: these schedules remain collision-free on this **`K`** through **`n=60`** while other public schedules (e.g. triangular, squares) collide earlier.
- Next optional band **`n>60`** is increasingly expensive (**`C(n,6)`**).

**Analogy pass summary:** Same structure as **103** — extend **`n`** window for schedules that stayed clean through **`n=55`**.

**Space-definition:** none
