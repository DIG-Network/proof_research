# Hypothesis

**H1 (rubric exists):** A finite checklist of **verifier-side** properties can classify candidate proof systems into at least three buckets consistent with the main problem’s exclusions:

| Bucket | Intent |
|--------|--------|
| **EXCLUDED_SNARK** | Matches “Groth16 / PLONK / FRI toolchain” style: proof-agnostic verifier for **NP statements** given as **circuits** / AIR / R1CS with **poly(statement size)** work hidden inside a **fixed-interface** verify routine. |
| **GREY_TRANSPARENT** | Transparent-setup **compressed** proofs (IPA / Bulletproofs-style): verifier work often **Θ(log n)** in *folding dimension* but statement is still encoded as **constraints on n secrets** (e.g. `w ∈ {0,1}^n`, `∑ w_i ≥ t`). **Practical** verifier may still be **Ω(n)** in **field/group ops** unless the *statement* is compressed — policy choice whether this violates “no SNARKs / no circuit verifier.” |
| **ALLOWED_ATOMIC** | Fixed, **parameterized-family** checks: constant pairing count, `O(log n)` Merkle hashes, one Schnorr equation, **no** arbitrary circuit evaluator as input to `Verify`. |

**H2 (stress case):** For the concrete threshold-link predicate behind `F_Link` with hidden `w ∈ {0,1}^n`, **every** natural transparent compressed proof **inherits** `GREY_TRANSPARENT` because the **arithmetization size** scales **Ω(n)**.

**Falsification of H1:** Produce an internally inconsistent classification (e.g. Groth16 lands in ALLOWED_ATOMIC).

**Scope:** **Engineering/policy** rubric for this repo, not a legal definition of “SNARK.”
