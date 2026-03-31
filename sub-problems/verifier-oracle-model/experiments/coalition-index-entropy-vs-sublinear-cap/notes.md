# Notes

- Pairs **012** (Merkle *path* bits vs \(B(n)\)) with a **pure counting** view: \(\log_2 \binom{n}{t} \sim n - O(\log n)\) for central coefficients.
- **65536** row is numerically tight vs \(B(n) = 256 \cdot 16^2\): explains why “almost sublinear” polylog caps are **not** threatened by coalition-count alone until \(n\) is large — the threat to **naive indexing** is asymptotic.
- **Deliverable alignment** (`verifier-oracle-model`): documents a **definitional** barrier for *witness models* that smuggle in full coalition identity; sound **anonymous** realizations must avoid that witness model (aggregates, ZK-style hiding, or novel **R7** structure).
