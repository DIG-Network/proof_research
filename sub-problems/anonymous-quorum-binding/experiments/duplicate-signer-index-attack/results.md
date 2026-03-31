# Results

| Field | Value |
|-------|--------|
| **Outcome** | **PASS** (attack succeeds on flawed verifier) |
| **Model** | Merkle + toy `σ = H(SIG|m|K)`; aggregate **with multiplicity** `K = Σ_{i∈S} pk_i`. |

## Transcript

- `n = 8`, `t = 5`, `S = (0,0,0,0,0)`, five copies of the same Merkle path for leaf `0`.
- `K = 5 · pk_0`, `σ = H_sig(m, K)` — algebraically consistent with multiplicity sum.
- **Unique validators represented:** **1** `< t`.

## Verdicts

| Verifier | Requires distinct indices | Accepts duplicate-`S` |
|----------|---------------------------|------------------------|
| Sound | Yes (`|set(S)| = |S|`) | **No** |
| Flawed | **No** | **Yes** |

## Interpretation

“**`t` openings**” is **not** the same as “**`t` distinct** committed signers” unless the interface explicitly enforces **set** semantics on indices / cosigner IDs.
