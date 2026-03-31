# Results — aggregated-key-link-game

**Outcome:** **PASS** (for the hypothesis about the verifier **interface**)

## What was tested

A verifier that accepts `π = (K, σ)` and only checks `σ` authenticates `m` under `K` (toy: `σ = H(m‖K)`), with `C` a Merkle-style commitment to the multiset of validator public keys. The verifier **never** uses individual `pk_i`.

## Finding

- With **only** the signature check against the provided `K`, an adversary who knows all secret keys used to define the `pk_i` can choose `S` with `|S| = t − 1`, set `K ← \mathrm{Agg}(\{pk_i : i ∈ S\})`, and produce a consistent `σ`. **Accept** — **strict under-quorum**.
- A **reference** predicate `Link(C, K)` implemented by brute force (“exists `S ⊆ [n]`, `|S| ≥ t`, with `\sum_{i∈S} pk_i = K`”) **rejects** the same `π` when given the full key list (this brute-force link is **not** allowed in the target model; it only characterizes the missing condition).

## Interpretation

Sound threshold verification relative to `Commit(V)` necessarily includes **some** efficient surrogate for `Link(C, K)` (or an entirely different `π` shape). Constant-size `(K, σ)` alone does not encode “≥ `t` keys from `C`” against a full-key adversary.

## Script

`python script.py` — asserts under-quorum naive accept and link reject; exit code 0.
