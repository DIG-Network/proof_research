# Hypothesis

**H1 (spec coherence):** One can define an **ideal functionality** `F_Link` (parameterized by `n`, threshold `t`, and a binding commitment `C` to ordered public keys `(pk_0,…,pk_{n−1})`) such that:

- `F_Link.Verify(C, t, K, w)` returns **accept** iff witness `w` exposes a set `S ⊆ {0,…,n−1}` with `|S| ≥ t` and `Agg(S) = K`, where `Agg` is the same aggregation law as in the real protocol (abstracted as sum in the experiment), **and** the keys `{pk_i}_{i∈S}` are exactly those committed in `C` (ideal holds the hidden table).

**H2 (separation):** A **naive real-world** checker that only tests `SigVerify(K, m, σ)` does **not** query `F_Link` and accepts transcripts that `F_Link` would **reject** for the same `(C, t, K)` when the signing coalition is under-quorum — reproducing the Entry **002** interface gap in the same codebase.

**Falsification of H1:** Internal contradiction in the scripted state machine or failed assertions on honest transcripts.

**Falsification of H2:** If naive checker is wired to reject whenever `F_Link` rejects (trivial), the experiment’s “naive” definition must be the **deliberately incomplete** one from `aggregated-key-link-game`.
