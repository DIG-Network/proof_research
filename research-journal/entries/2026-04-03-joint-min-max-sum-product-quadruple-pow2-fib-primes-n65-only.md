# Journal entry — 2026-04-03 — joint-min-max-sum-product-quadruple-pow2-fib-primes-n65-only

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-pow2-fib-primes-n65-only`

**Context:** anonymous-quorum-binding (shell toy: exact **`K=(min,max,Σ,Π)`**, shells 5 vs 6)

**Hypothesis tested:** At least one of **`pow2_2^i`**, **Fibonacci prefix**, **first `n` primes** has a 5-vs-6 cross-shell collision at **`n=65`**.

**Outcome:** **FAIL**

**Key finding:** **None** of the three schedules collides at **`n=65`** (exhaustive per schedule, ~238 s wall). Together with **101–108**, there is **no** such collision for **any** **`n ∈ [11,65]`** on these three schedules under exact **`K`**.

**Implications:**

- One-step extension past **108** still leaves **pow2** / **fib** / **primes** clean on this **`K`**.
- **`n=66`** is the next single-`n` probe with another large combinatorial step.

**Analogy pass summary:** Minimal **`n`** frontier extension of **108** — same **`K`**, same three schedules, single **`n=65`**.

**Space-definition:** none
