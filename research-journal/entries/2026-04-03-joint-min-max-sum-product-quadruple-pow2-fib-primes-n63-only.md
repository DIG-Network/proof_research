# Journal entry — 2026-04-03 — joint-min-max-sum-product-quadruple-pow2-fib-primes-n63-only

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-pow2-fib-primes-n63-only`

**Context:** anonymous-quorum-binding (shell toy: exact **`K=(min,max,Σ,Π)`**, shells 5 vs 6)

**Hypothesis tested:** At least one of **`pow2_2^i`**, **Fibonacci prefix**, **first `n` primes** has a 5-vs-6 cross-shell collision at **`n=63`**.

**Outcome:** **FAIL**

**Key finding:** **None** of the three schedules collides at **`n=63`** (exhaustive per schedule, ~188 s wall). Together with **101–106**, there is **no** such collision for **any** **`n ∈ [11,63]`** on these three schedules under exact **`K`**.

**Implications:**

- One-step extension past **106** still leaves **pow2** / **fib** / **primes** clean on this **`K`**.
- **`n≥64`** merits explicit compute budgeting before wider band scans.

**Analogy pass summary:** Minimal **`n`** frontier extension of **106** — same **`K`**, same three schedules, single **`n=63`**.

**Space-definition:** none
