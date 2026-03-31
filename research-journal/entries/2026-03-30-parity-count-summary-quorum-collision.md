# 2026-03-30 — parity-count-summary-quorum-collision

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/parity-count-summary-quorum-collision/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** For **n = 10**, **t = 6**, the summary **h(k) = k mod 2** agrees on **k = 4** (under-quorum) and **k = 6** (at threshold), so **no** decision rule on **h(k)** alone realizes **k ≥ t**.

**Outcome:** **PASS**

**Key finding:** **Coarse** scalar summaries of participation count can **straddle** the **majority** boundary — the same abstract failure mode as **lossy bins** in hypothesis testing, distinct from **021**’s **aligned** **F₂** mask family and **022**’s **single** **𝔽_p** evaluation ambiguity.

**Implications:**

- Any “**1-bit quorum hint**” derived only from **parity** of signer count is **interface-incomplete** for strict threshold soundness.
- Clarifies that **sublinear** **|π|** tension is not only about **Merkle** bits but about **injective** enough **statistics** of hidden participation.

**Analogy pass summary:** **Hypothesis testing / binning**, **quantization**, **database rollups**, **modular aliasing** — seed: **non-injective** **h(k)**.
