# 2026-03-30 — f2-linear-measurements-threshold-ambiguity

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/f2-linear-measurements-threshold-ambiguity/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** For **n = 8**, **t = 5**, there exist majority / one-below-threshold bit patterns **x, y** and **n−1** **independent** **F₂** linear functionals **r_j** with **r_j·x = r_j·y** for all **j** (all parity pools agree).

**Outcome:** **PASS**

**Key finding:** A **fixed** family of **parity-only** linear measurements can be chosen (after fixing **d = x ⊕ y**) so that **seven** independent pools are **identical** on a **strict-majority** pattern and a **sub-threshold** pattern. Pure **linear pooling** is a straw model that does **not** carry threshold structure by itself; aligns with the need for **nonlinear** / **cryptographic** **`Link`**-style binding in earlier journal entries.

**Implications:**

- Treat “**compress-then-linear-probe**” sketches as **non-starters** unless nonlinearity or **injective** restriction on patterns is modeled.
- **Coding-theoretic** language (syndrome collision along **d**) is a useful **digest** thread for `verifier-oracle-model`.

**Analogy pass summary:** **Group testing**, **linear codes / syndromes**, **sketching identifiability**, **statistical summaries** — seed from **parity checks orthogonal to** **d**.
