# Results

| Field | Value |
|-------|--------|
| **Outcome** | **PASS** (flawed relation is malleable across **`m`**) |
| **Scope** | Toy hashing only; isolates **message domain** in the final verification equation. |

## Construction

- **Sound:** `σ = H(SIG|m|K)`; accept iff same recomputation with verifier’s **`m`**.
- **Flawed:** accept iff `σ = H(BAD|K)` — **no **`m`**.

## Observed behavior

- Fixed **`(K, σ_bad)`** with `σ_bad = H(BAD|K)` passes **flawed** verification for **`m₁ = finalize-epoch-9`** and **`m₂ = rollback-epoch-9`** simultaneously.
- **`σ_good = H(SIG|m₁|K)`** passes **sound** check only for **`m₁`**; **`m₂`** **fails**.

## Interpretation

Threshold / Merkle / **`Link`** hygiene does not replace **binding the signed message** into the verified signature predicate — an independent **interface** requirement (real schemes use **domain separation**, **message hashes**, transcript hashes, etc.).
