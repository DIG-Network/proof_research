# Notes — polynomial-three-eval-binary-collision

- **Scaling:** For fixed **p**, **k** evaluations admit at most **pᵏ** distinct summaries; binary patterns require **2ⁿ** injectivity ⇒ need **n ≤ k log₂ p** (information-theoretic) or extra structure. Here **k = 3**, **p = 97** ⇒ **p³** barrier explicit.
- **Not a cryptographic attack:** Toy model — shows **limits of polynomial-evaluation-only** binding for **full** **0/1** vectors, not a break of any deployed PCS.
- **Next threads:** (a) **k** growing with **n** (e.g. **Θ(log n)** points → **|π|** not **O(1)**); (b) bind **low-degree** statistics of **v** rather than **v** itself; (c) **nonlinear** mix (hash leaves then polynomial, Merkle on evaluations, etc.).
- **Verifier-oracle sibling:** Same pigeonhole logic as digest cross-link to **024**; strengthens the “constant **k** openings” obstruction ladder.
