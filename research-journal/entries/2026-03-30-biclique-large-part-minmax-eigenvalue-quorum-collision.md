# 2026-03-30 — biclique-large-part-minmax-eigenvalue-quorum-collision

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/biclique-large-part-minmax-eigenvalue-quorum-collision/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** On **G = K_{3,7}** (**n=10**, **t=6**), **S_a ⊆ R**, **|S_a|=5**, **S_b ⊆ R**, **|S_b|=6** induce **edgeless** **subgraphs**, so **(λ_max,λ_min)=(0,0)** for **both** — **quorum** **collision** on **extremal** **adjacency** **spectrum**.

**Outcome:** **PASS**

**Key finding:** **21** **cross** **edges** (**dense** **bipartite**) still allows **same** **two-float** **spectral** **summary** **across** **t** if **signers** **stay** **inside** **the** **7**-**vertex** **independent** **part** — **intermediate** **host** **between** **025** **(sparse** **star)** and **026** **(clique)**.

**Implications:**

- **Spectral** **certificate** **narratives** need **α(G) < t** (or **equivalent**) so **every** **quorum** **hits** **an** **internal** **edge**, **not** **merely** **high** **|E|**.
- Digest **open** **line** **shrinks** to **small-α** / **forced-edge** **quorum** **regimes**.

**Analogy pass summary:** **Turán** **/** **block** **models** **/** **LDPC** **bipartite** **structure** — seed: **large** **color** **class** **hides** **pairwise** **interaction** **in** **G[S]**.
