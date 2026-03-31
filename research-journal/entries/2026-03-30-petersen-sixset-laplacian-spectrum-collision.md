# 2026-03-30 — petersen-sixset-laplacian-spectrum-collision

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/petersen-sixset-laplacian-spectrum-collision/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** On the **Petersen** graph (**n = 10**, **3-regular**), two **distinct** **6**-vertex subsets exist whose **induced** subgraphs have **identical** **sorted** **Laplacian** eigenvalue multisets.

**Outcome:** **PASS**

**Key finding:** **S₁ = {0,1,2,3,4,5}** and **S₂ = {0,1,2,3,4,6}** share the same **full** **6**-tuple Laplacian spectrum (golden-ratio–related values **≈ 0.697, 1.382, 2, 3.618, 4.303** plus **0**). Shows **richer-than-(λ_max,λ_min)** summaries still **alias** on an **expander** toy when **symmetry** relates witnesses.

**Implications:**

- **π** = “sorted Laplacian eigenvalues of **G[S]**” does **not** uniquely identify **S** among **quorum**-sized sets on **highly symmetric** hosts.
- Digest **open** thread: **partially** addressed for **Petersen**; **asymmetric** **labeled** graphs / **break** **automorphisms** remain a follow-up.

**Analogy pass summary:** **Cospectral** **graphs**, **isospectral** **drums**, **non-injective** **spectral** **fingerprints** — seed: **Laplacian** **spectrum** **collision** **on** **induced** **subgraphs**.
