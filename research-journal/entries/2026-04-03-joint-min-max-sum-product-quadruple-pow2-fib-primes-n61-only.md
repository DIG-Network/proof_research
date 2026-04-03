# Journal entry — 2026-04-03 — joint-min-max-sum-product-quadruple-pow2-fib-primes-n61-only

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-pow2-fib-primes-n61-only`

**Context:** anonymous-quorum-binding (shell toy: exact **`K=(min,max,Σ,Π)`**, shells 5 vs 6)

**Hypothesis tested:** At least one of **`pow2_2^i`**, **Fibonacci prefix**, **first `n` primes** has a 5-vs-6 cross-shell collision at **`n=61`**.

**Outcome:** **FAIL**

**Key finding:** **None** of the three schedules collides at **`n=61`** (exhaustive per schedule, ~179 s wall). Together with **101–104**, there is **no** such collision for **any** **`n ∈ [11,61]`** on these three schedules under exact **`K`**.

**Implications:**

- One-step extension past **104** does not break the clean regime for **pow2** / **fib** / **primes** on this **`K`**.
- **`n>61`** scans cost grows sharply; treat as explicit compute budget items.

**Analogy pass summary:** Minimal **`n`** frontier extension of **104** — same **`K`**, same three schedules, single **`n`**.

**Space-definition:** none
