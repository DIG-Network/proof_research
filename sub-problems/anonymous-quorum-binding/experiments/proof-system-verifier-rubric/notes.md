# Notes

- On-chain **auditing** cost often tracks **constraint count**, not proof length — a log-sized Bulletproof may still be unacceptable under “resource-constrained verifier” if implementation expands to **Ω(n)** field ops via precomputed bases or witness-dependent loops in naïve ports.
- **Recursive proof composition** (proof-of-proof) stays **EXCLUDED_SNARK**-adjacent unless the inner statement is **tiny** and fixed — separate experiment if a candidate uses recursion.
- If the project **ABANDONs** anonymous sublinear `Link`, a deliberate **relaxation** could move to **ALLOWED_ATOMIC** + linear `π` (out of scope for the original main success criterion).
