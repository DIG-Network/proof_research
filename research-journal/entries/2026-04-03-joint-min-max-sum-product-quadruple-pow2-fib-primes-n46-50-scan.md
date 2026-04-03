# Journal entry — 2026-04-03 — joint-min-max-sum-product-quadruple-pow2-fib-primes-n46-50-scan

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-pow2-fib-primes-n46-50-scan`

**Context:** anonymous-quorum-binding (shell toy / public weight statistics)

**Hypothesis tested:** At least one of **`pow2_2^i`**, **`fibonacci`**, **`first_n_primes`** has a 5-vs-6 cross-shell collision for exact **`K=(min,max,sum,product)`** for **some** **`n ∈ [46,50]`**.

**Outcome:** **FAIL**

**Key finding:** **All three** schedules have **no** such collision for **every** **`n` from 46 to 50**. Combined with **101** (**no** collision **`n=11..45`** for the same three), there is **no** collision in **`[11,50]`** for these schedules under this **`K`**.

**Implications:**

- Strengthens **negative** evidence that **structured** slow-/moderate-growth schedules can **delay** or **avoid** (in scanned range) the **`K`** cross-shell failure seen for **linear** (**097**), **square** (**099**), and **triangular** (**101**) encodings.
- Next optional band **`n>50`** or pivot to **verifier-oracle** line per **session-state**.

**Analogy pass summary:** Continuation probe — same combinatorial collision machinery as **098**/**101**; **triangular** omitted as already separated at **`n=36`**.

**Space-definition:** none
