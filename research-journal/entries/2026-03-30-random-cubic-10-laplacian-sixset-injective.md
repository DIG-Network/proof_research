# 2026-03-30 — random-cubic-10-laplacian-sixset-injective

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/random-cubic-10-laplacian-sixset-injective/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** Some **`networkx.random_regular_graph(3, 10, seed)`** sample yields **pairwise** **distinct** **sorted** **induced** **Laplacian** **spectra** **over** **all** **210** **6**-**subsets** **(same** **8**-**decimal** **rounding** **as** **032).**

**Outcome:** **FAIL** **(in** **search** **range)**

**Key finding:** **Seeds** **0..99 999** **—** **no** **injective** **instance.** **Collisions** **arrive** **almost** **immediately** **on** **typical** **samples** **(often** **single-vertex** **swaps** **between** **6**-**sets),** **so** **Laplacian** **spectrum** **of** **G[S]** **does** **not** **uniquely** **identify** **S** **even** **for** **generic** **labeled** **cubics** **—** **not** **only** **Petersen** **symmetry.**

**Implications:**

- **032** **open** **thread** **(asymmetric** **host):** **random** **cubic** **evidence** **points** **away** **from** **“pick** **a** **rigid** **expander** **and** **publish** **full** **L**-**spectrum** **of** **G[S]”** **as** **a** **coalition** **fingerprint.**
- **Scaling** **search** **or** **different** **degree** **/ ** **n** **could** **be** **future** **work;** **this** **run** **is** **a** **strong** **negative** **for** **the** **stated** **toy** **claim.**

**Analogy pass summary:** **Graph** **distinguishability,** **identifiability,** **syndrome** **injectivity** **—** **seed:** **exhaust** **random** **labeled** **hosts** **for** **injective** **spectrum** **map** **on** **k**-**subsets.**
