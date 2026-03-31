# Notes — star-independent-minmax-eigenvalue-quorum-collision

- **Full** multiset of eigenvalues **would** distinguish `5` zeros from `6` zeros — the failure mode is **deliberately lossy** `(λ_max, λ_min)`, matching the “constant-size verifier digest” metaphor in **023** / **024**.
- **Expander** hopes (second eigenvalue certifying large cuts) do not apply when the induced graph is **empty** — **no internal edges** ⇒ flat spectrum at `0`.
- **Generalization:** Any `G` with an **independent set** of size `≥ t` lets an adversary realize **both** sub-threshold and **≥ t** active sets inside that independent set, all inducing **edgeless** subgraphs, hence identical **min/max** adjacency spectrum `(0,0)` if all eigenvalues are `0`.
- **Next (if continuing spectral):** Laplacian of `G[S]` on **isolated** vertices — all eigenvalues `0` as well for standard Laplacian `D-A` with `D=0`. Same collision. Richer toys would need **forced** internal edges (every quorum set hits edges) — then spectrum may carry **some** scale, but **constant** openings still risk collisions (separate experiment).
