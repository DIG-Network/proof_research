# Hypothesis

**H:** Under **relaxation R1** from Entry **010** — allow **`|π| = Θ(t · log n)`** (one Merkle inclusion path per attested signer, plus `O(1)` signature material) — there exists a **toy** `Verify(C, m, π)` that:

1. Uses **only** `(C, m, π)` (no hidden key list),
2. **Accepts** when a strict majority subset **honestly** signed (completeness),
3. **Rejects** strict **under-quorum** attempts that reuse the same interface (soundness in this toy model).

**Falsification:** Scripted under-quorum transcript verifies, or honest transcript fails.

**Scope:** Demonstrates **R1 suffices** for a **linearity** regime; **does not** meet the main problem’s **sublinear** `π` requirement.
