# 2026-03-30 — tropical-min-pool-summary-quorum-collision

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/tropical-min-pool-summary-quorum-collision/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** **h(S) = min_{i∈S} c_i** **with** **strictly** **increasing** **public** **c_i**; **two** **sets** **straddling** **t** **that** **both** **contain** **argmin** **share** **h**.

**Outcome:** **PASS**

**Key finding:** **c_i = i**, **S_a** **size** **5**, **S_b** **size** **6**, **both** **contain** **0** **⇒** **h = 0** **each** **—** **min-plus** **style** **one-number** **summary** **is** **blind** **to** **quorum** **in** **this** **straw** **model**.

**Implications:**

- **Adds** **tropical** **/** **bottleneck** **analogy** **next** **to** **021** **(F₂)** **and** **023** **(parity** **of** **count)**.
- **Does** **not** **rule** **out** **richer** **tropical** **vectors** **—** **only** **this** **scalar** **min**.

**Analogy pass summary:** **Min-plus** **linear** **functionals,** **bottleneck** **LP,** **non-injective** **mins** **—** **seed:** **shared** **argmin** **hides** **|S|**.
