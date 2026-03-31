# 2026-03-30 — star-independent-minmax-eigenvalue-quorum-collision

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/star-independent-minmax-eigenvalue-quorum-collision/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** On a fixed **star** `K_{1,m}`, **leaf-only** subsets induce **edgeless** graphs, so **adjacency** **λ_max = λ_min = 0**; choose `|S_a| < t ≤ |S_b|` with both **leaf-only** → identical **two-float** summary **across** quorum.

**Outcome:** **PASS**

**Key finding:** `n = 10`, `t = 6`, `S_a` five leaves, `S_b` six leaves; both **zero** adjacency blocks; `(0,0)` vs `(0,0)`. Shows **spectral compression** to **extremal** adjacency eigenvalues does **not** encode quorum in this straw model — closes the digest’s “spectral not yet tested” gap at a **baseline** negative.

**Implications:**

- Any “**induced subgraph spectrum** (few numbers) as quorum certificate” story must specify **which** matrix, **which** statistics, and **why** active sets cannot live in a **large independent** set with **empty** induced subgraph.
- Pair with **023** (parity of count) and **024** (few polynomial evals) as **lossy summary** obstructions.

**Analogy pass summary:** **Spectral graph theory**, **spin / flat phases**, **PCA extremes on zero matrix** — seed: **edgeless** induced subgraph ⇒ **degenerate** spectrum.
