# Notes — implications

1. **Where natural stacks break:** The conflict is not “Merkle is bad” per se — it is **binding each of Θ(n) contributions to C** while keeping the verifier’s input **compact** and the proof **sublinear**. Per-signer Merkle paths are the textbook way to get **set soundness** without listing all keys to the verifier, but they **inherit linearity in the number of authenticated keys** you must exhibit inside the proof.

2. **BLS (or any linear key aggregation):** Hiding the signer set hides **which** linear combination defines the aggregate verification key. Without SNARKs, compressing **“there exists S, |S| ≥ t, such that σ is valid under PK_S and each pk_i ∈ V”** into **o(n)** bits appears to require a **new** algebraic object, not just “BLS + Merkle + folklore.”

3. **Relaxations that salvage known tools (outside strict target):**
   - **Reveal** the aggregate key for the signing committee (loses strong anonymity of the subset; may be acceptable if only unlinkability across messages matters).
   - **Small t** or **small n** in practice so linear proofs are “acceptable” — contradicts asymptotic **o(n)** goal but may be a product decision.
   - **Allow Θ(n)** proof size — solves binding trivially (list proofs) but violates the main problem’s communication target.
   - **SNARKs / STARKs** — excluded by problem statement; they would reintroduce the forbidden verifier.

4. **Research direction:** A positive result likely needs either (a) a **special-purpose** proof system tightly tied to the signature algebra with **proof size independent of t** in a way current OR-proofs are not, or (b) a **weaker** anonymity notion, or (c) **additional** public structure in `C` (beyond plain Merkle root of keys) that makes threshold checks aggregatable — without sneaking in a SNARK verifier.

5. **Sub-problem status:** This experiment **does not close** the sub-problem formally (no theorem in a full AGM/ROM model); it **documents** why **first-choice** combinations fail the **joint** constraints and what must give if one insists on standard verifier assumptions.
