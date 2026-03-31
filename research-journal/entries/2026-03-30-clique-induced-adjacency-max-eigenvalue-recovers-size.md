# 2026-03-30 — clique-induced-adjacency-max-eigenvalue-recovers-size

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/clique-induced-adjacency-max-eigenvalue-recovers-size/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** For host **G = K_n**, **G[S] ≅ K_{|S|}**, hence **λ_max(A(G[S])) = |S| − 1**; for **n = 10**, **t = 6**, **|S| = 5** vs **6** give **distinct** **λ_max**.

**Outcome:** **PASS**

**Key finding:** **Positive control** to **025**: **dense** **clique** host removes **independent-set** **spectral** **degeneracy**; **one** extremal eigenvalue **tracks** **|S|** in this **straw** model. Shows **spectral** **obstructions** are **geometry-dependent**, not absolute.

**Implications:**

- Narratives that use **induced-subgraph** spectra must fix **what** **G** is **committed** in **C** and **why** **quorums** cannot **hide** in **large** **α(G)** regions.
- **Expander** / **intermediate** **density** regimes remain **unmapped** in-repo.

**Analogy pass summary:** **Dense interaction** / **mean-field** vs **sparse** **modes**; **K_k** **closed-form** spectrum — seed: **λ_max** **sufficient** for **|S|** **iff** **G[S]** is **full** **clique**.
