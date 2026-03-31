# Main problem — formal statement

## Objects

- Integer `n ≥ 1` — validator count.
- Quorum threshold `t = ⌊n/2⌋ + 1` (strict majority).
- Validator set `V = { (id_i, pk_i) }_{i=1}^n` — identities (or indices) and public signing keys from a standard signature scheme (e.g. Schnorr / ECDSA / BLS).
- Message space `M` — arbitrary bitstrings.
- **Commitment** `C = Commit(V)` — compact: `|C| = O(λ)` bits, independent of `n` beyond `poly(λ, log n)` if needed for indexing semantics. The commitment is public and binding to `V`.

## Threat model (explicit)

- **Verifier input:** `Verify` receives **only** `(C, m, π)` — no per-validator `pk_i` list, no hidden oracle to the full key table (see sub-problem `verifier-oracle-model`).
- **Validator keys:** Unless otherwise stated, **soundness** games should declare whether public keys are **honest keygen** (e.g. IID random scalars / standard sampling) or **adversarially chosen** but still bound into `C` (malicious registration). Toy experiments show **aggregate ambiguity** can be **forced** under malicious choice (`rogue-key-aggregate-collision`); **IID** regimes often look injective in integer proxies (`random-aggregate-injectivity-mc`). Real groups may additionally assume **proof-of-possession** or delinearized aggregation — state any such assumption in a full construction.

## Algorithms (target)

- `Sign(sk_i, m) → σ_i` — standard per-validator signing.
- `Prove(V, S, {σ_i}_{i∈S}, m) → π` — prover (aggregator) produces proof. Requirement: `|π| = o(n) · λ` (sublinear in `n`) or a documented practical constant bound with clear justification.
- `Verify(C, m, π) → {accept, reject}` — verifier **does not** receive `pk_1..pk_n` individually; only `C`, `m`, `π`.

## Security goals

1. **Completeness:** If `S ⊆ {1..n}`, `|S| ≥ t`, and each `σ_i` is valid for `pk_i` and `m`, then honestly generated `π` verifies against `C = Commit(V)`.
2. **Soundness (threshold):** No PPT adversary given `C` for an honest `V` can produce `(m*, π*)` that `Verify` accepts unless at least `t` validators from `V` signed `m*` (under a precise game: static corruption, EUF-CMA-style unforgeability lifted to threshold).
3. **Set soundness:** Accepting proofs imply signers are subset of the committed validator keys (no “foreign” key contribution).
4. **Signer anonymity (optional but desired):** `π` need not reveal `S` uniquely; verifier only learns that *some* quorum attested.

## Hard exclusions

- No SNARKs/STARKs or general-purpose ZK proof systems requiring circuits for verification of the main statement.
- No trusted setup, TEE, or trusted third party.
- No proof `π` that is `Θ(n)` merely by listing all signatures / all keys / full Merkle proofs for each signer without asymptotic or practical sublinearity argument.

## Success criterion

Explicit algorithms + assumption statement + reference implementation where `Verify` meets resource constraints and experiments pass under stated assumptions.
