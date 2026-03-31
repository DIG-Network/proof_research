# Sub-problem: anonymous quorum binding to a static commitment

## Question

Does there exist a cryptographic object that simultaneously:

1. Binds a signature-like attestation on message `m` to **membership in** a large committed set `V` of public keys (without the verifier holding each `pk_i` at verification), and
2. Hides **which** members signed, while still convincing the verifier that **at least** `t` members participated,

using only **standard** assumptions (discrete log / pairings / RSA / random oracle), **no** general-purpose ZK-SNARK/STARK verifier, and **sublinear** communication in `n`?

## Threat model hook

- Declare whether `pk_i` are **honest keygen** (random / standard distribution) or **adversarially registered** into `C`. Malicious registration can force **aggregate collisions** between distinct quorums in toy additive models (journal **008**); honest IID proxies often show **injective** majority aggregates (**007**).
- Any candidate **`Link(C, K)`** must be evaluated under the same registration assumption as the main soundness game.

## Why this blocks the main problem

This is the apparent “missing primitive”: threshold signatures usually expose an aggregate key **for a known cosigner set** or require per-signer verification material.

## Deliverable

- A candidate primitive with explicit algorithms **or**
- A documented failure of natural candidates (BLS aggregation with hidden partition, accumulators + OR-proofs, Merkle + signature aggregation, etc.) with precise attack or unsoundness pattern.
