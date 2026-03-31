# 2026-03-30 — mod-m-count-summary-threshold-aliasing-scan

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/mod-m-count-summary-threshold-aliasing-scan/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** For **n = 10**, **t = 6**, **h(k) = k mod m** admits a pair **k₁ < t ≤ k₂** with **k₁ ≡ k₂ (mod m)** iff **m ≤ n**; first **m** with no such pair is **n + 1 = 11**.

**Outcome:** **PASS**

**Key finding:** Crossing gaps **k₂ − k₁** cover **every** **d ∈ {1,…,10}**, so **m | d** for some crossing pair iff **m ≤ 10**. Extends **parity-count-summary** (**m = 2**) and **023** to a **full** modular family; **O(1)**-bit residue cannot separate threshold unless **m** is **Ω(n)** in this count-only model.

**Implications:**

- A **single** modular bucket of **total participation** (no other probes) needs modulus **> n** to avoid aliasing here — **Θ(log n)** bits, not **constant**.
- Pairs **(0, 6)**, **(0, m)** for **m ∈ {6,…,10}** are canonical witnesses; **(4, 6)** remains a valid **m = 2** example.

**Analogy pass summary:** **Nyquist / aliasing**, **modular hashing**, **CRT lift** — seed: **D = crossing gaps**, **m | d** **⇔** **alias**.
