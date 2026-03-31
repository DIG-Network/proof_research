# Hypothesis

**H0 (testable claim):** For a static Merkle commitment `C` to an ordered list of `n` independent public keys `{pk_i}`, and a proof string `π` with length `|π| = o(n)` (in group elements / hashes, counting each as `Θ(λ)` bits), **no** verifier algorithm that is a fixed composition of:

- hash / Merkle opening checks,
- a constant number of pairing or elliptic-curve equation checks per validator index **not** present in `π`,

can implement sound verification of the statement “signatures from some undisclosed strict-majority subset of the committed keys attest to `m`” **using only standard BLS-style linear multisignature aggregation** as the attestation object, **without** either:

1. embedding `Ω(n)` bits of subset-identifying information in `π` or implicit verifier state, or
2. replacing linear aggregation with a different proof/accumulator mechanism excluded only if it smuggles SNARK-like power.

**Falsification:** Provide an explicit `(Commit, Prove, Verify)` triple meeting the main problem constraints where `Verify` uses ≤ `poly(λ, log n)` work and `|π| = o(n)`, and pass the scripted sanity checks in `script.py`.

**Note:** This hypothesis is about **structural alignment** between Merkle-commitment + sublinear `π` + classical aggregation APIs, not a formal cryptographic theorem.
