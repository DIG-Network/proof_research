# Journal entry — 2026-04-04 — joint-min-max-sum-product-quadruple-pow2-fib-primes-n87-only

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-pow2-fib-primes-n87-only`

**Context:** anonymous-quorum-binding (shell toy: exact **`K=(min,max,Σ,Π)`**, shells 5 vs 6)

**Hypothesis tested:** At least one of **`pow2_2^i`**, **Fibonacci prefix**, **first `n` primes** has a 5-vs-6 cross-shell collision at **`n=87`**.

**Outcome:** **FAIL**

**Key finding:** **None** of the three schedules collides at **`n=87`** (exhaustive per schedule, ~1636 s wall). Together with **101–130**, there is **no** such collision for **any** **`n ∈ [11,87]`** on these three schedules under exact **`K`**.

**Implications:**

- One-step extension past **130** still leaves **pow2** / **fib** / **primes** clean on this **`K`**.
- **`n=88`** is the next single-`n` probe with another combinatorial step in **`C(n,6)`**.

**Analogy pass summary:** Minimal **`n`** frontier extension of **130** — same **`K`**, same three schedules, single **`n=87`**.

**Space-definition:** none
