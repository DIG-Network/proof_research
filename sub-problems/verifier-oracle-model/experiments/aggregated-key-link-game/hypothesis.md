# Hypothesis

**H (soundness interface):** Consider a class of verifiers `Verify(C, m, π)` that parse `π = (K, \sigma)` where `K` is a single compact “claimed aggregate public key” (one group element / `λ` bits) and `\sigma` is a standard multisignature on `m` under `K` (Schnorr/BLS-style: verification is a fixed equation in `(K, m, \sigma)` only).

**Claim:** If `Verify` **does not** additionally enforce a predicate `Link(C, K)` asserting that `K` equals (or is uniquely determined by) the aggregation of **at least** `t` distinct keys among those committed in `C`, then a **full-key knowledge** adversary can produce an accepting transcript with an **honest** `(C, m)` while only **t − 1** validators signed `m` (strict under-quorum).

**Falsification:** Exhibit a sound `Verify` in this message format where `Link` is not used (or is implied with `o(n)` work and no per-key material) and the scripted attack fails.

**Scope:** This is a **game-theoretic / API** statement about the **interface** between commitment, aggregate key, and signature check — not a reduction to a hard problem.
