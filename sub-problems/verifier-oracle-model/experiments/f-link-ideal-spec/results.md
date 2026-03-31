# Results — f-link-ideal-spec

**Outcome:** **PASS** (for **H1** and **H2** as specification / regression checks)

## H1 — Ideal coherence

- `F_Link.Verify(C, t, K, S)` (as scripted) accepts iff `S` is a set of distinct indices in range, `|S| ≥ t`, and `Agg(S) = K`, with `C` matching the internally committed key vector.
- Honest majority witness **accepts**; strict under-quorum witness **rejects**.

## H2 — Separation from naive real interface

- `verify_naive_sig_only(K, σ, m)` **accepts** both honest and under-quorum `(K, σ)` pairs (toy signature).
- **Composed** verifier `F_Link` **then** signature check **rejects** under-quorum and **accepts** honest case.

## Interpretation

The experiment fixes a **reference ideal** for the predicate that Entry **002** argued is **missing** from constant-size `(K, σ)` verification. It does **not** realize `F_Link` efficiently or privately; it **locates** the interface point for any future construction.

## Script

`python script.py` — assertions + printed verdict; exit code 0.
