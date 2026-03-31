# 2026-03-30 — mod-m-threshold-alias-gap-set-scan

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/mod-m-threshold-alias-gap-set-scan/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** Generalize **081:** for **t = ⌊n/2⌋ + 1** and **n** through **30,** crossing gaps **D(n,t)** equal **{1,…,n},** hence **k mod m** aliases across the threshold cut iff **2 ≤ m ≤ n,** first clean **m = n+1.**

**Outcome:** **PASS** (plus **all** **t ∈ [1,n]** **checked** **for** **n ≤ 20**).

**Key finding:** **Constructive** **proof** **D = {1,…,n}** **for** **every** **valid** **t** **(** **cases** **d < t** **and** **d ≥ t** **)** **—** **not** **special** **to** **majority** **or** **n=10.** **Single-modulus** **count** **compression** **with** **m ≤ n** **always** **collapses** **some** **under-threshold** **and** **over-threshold** **counts** **in** **the** **full-range** **model.**

**Implications:**

- **081** **is** **one** **point** **in** **a** **general** **“** **mod** **m** **≤** **n** **⇒** **not** **a** **threshold** **certificate** **alone** **”** **law.**
- **Constant-size** **modular** **count** **hints** **need** **m > n** **(** **Θ(log n)** **bits** **)** **or** **extra** **structure.**

**Analogy pass summary:** **Frobenius** **/** **divisibility,** **Nyquist** **aliasing,** **CRT** **—** **seed:** **enumerate** **D** **as** **interval** **difference** **set.**
