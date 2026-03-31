# Notes

- Complements **013** (unauthenticated quorum field): here the bug is **wrong commitment anchor** (trust `declared_root` in `π`) rather than a fake `k̂`.
- Distinct from **002**’s “no `Link(K)`” toy: this one assumes **Merkle paths are present** but still separates worlds if the **on-chain** `C` is not the root used in verification.
- For real systems: “verify Merkle proof” APIs must take **`expected_root = C`** from chain state, never from untrusted `π` alone.
