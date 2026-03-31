# Results — proof-system-verifier-rubric

**Outcome:** **PASS** (for **internal consistency** of the rubric and scripted assertions — **not** a mathematical characterization of “SNARK”)

## What was tested

- Scripted classification table for several proof **families** against flags: trusted setup, whether `Verify` takes an **arbitrary** circuit/AIR, asymptotic pairing/hash/ops vs statement size `n_stmt`.
- Assertions: Groth16 row is `EXCLUDED_SNARK`; BLS single-equation row is `ALLOWED_ATOMIC`; at least one `GREY_TRANSPARENT` row exists.

## Findings

1. **EXCLUDED_SNARK** aligns with the user’s explicit exclusions (Groth16, PLONK, FRI-style generic verifiers) when “generic” means **circuit-parameterized** `Verify`.
2. **GREY_TRANSPARENT** captures transparent compressed proofs whose **transcript** is short in `n` but whose **natural arithmetization** of `F_Link`-style predicates still scales **Ω(n)** — policy must decide if these violate “verifiable without a prover circuit” **in spirit**.
3. **ALLOWED_ATOMIC** is where fixed-family checks (one BLS equation, one Merkle path) live; they **do not** alone solve `Link` + anonymity (per prior experiments).

## Interpretation

This experiment **documents** a boundary for **this** research project; it does **not** forbid or allow a specific IPA deployment without a separate security + policy experiment.

## Script

`python script.py` — prints table; exit code 0.
