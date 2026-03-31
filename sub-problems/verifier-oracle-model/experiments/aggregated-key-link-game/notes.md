# Notes

- The toy `H(m||K)` “signature” is **not** cryptographically sound EUF-CMA; it only isolates the **interface** dependency: any verifier that checks a predicate of the form `SigVerify(K, m, σ)` without `Link(C, K)` invites **pick your own K** from an undersized coalition.
- Real Schnorr/BLS multisignatures still fix a verification key `K`; the under-quorum attack is **structural** — it does not break discrete log, it shows **which statement** the proof must establish.
- `verify_with_link` as written is **exponential** in `n` and uses full `pks` — it is a **specification oracle** for “what soundness wants,” not a candidate scheme. Sublinear `Link` is the open bottleneck aligned with `anonymous-quorum-binding`.
- Next: formalize `Link` as an ideal functionality `F_link` and measure simulator failure when `π` is `o(n)`.
