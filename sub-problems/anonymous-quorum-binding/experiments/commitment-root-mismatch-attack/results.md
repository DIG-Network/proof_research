# Results

| Field | Value |
|-------|--------|
| **Outcome** | **PASS** (attack succeeds on flawed verifier) |
| **Interpretation** | Negative evidence: any Merkle-style witness must pin opened paths to the **verifier’s** commitment `C`, not an adversary-supplied root in `π`. |

## What was tested

- Two disjoint 8-leaf Merkle trees (`C_honest` vs `C_attack`), toy signature `σ = H(SIG|m|K)` under majority aggregate on the **attack** key list.
- **Sound** `Verify`: Merkle checks use **`C_onchain`** → rejects when `π` is built for the other tree.
- **Flawed** `Verify`: each path checked only against **`π.declared_root`** (ignores `C_onchain`) → **accepts** for unrelated on-chain `C`.

## Conclusion

Confirms an **implementation-level** failure mode adjacent to **002/004**: `Link(C,·)` is not only about `K`; for tree commitments, **root equality with `C`** is part of the binding story.
