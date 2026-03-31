# Notes

- Distinct from **002** (no paths at all): here the adversary has a **valid majority** of paths into `C` but decouples the **claimed** signing key `K` from the **algebraic** aggregate of those paths.
- Distinct from **013** (under-quorum + fake count): here `|S| ≥ t` is **honest**; the bug is purely **missing `K` vs opened-key aggregation** consistency.
- Real BLS / pairing verification would typically **relate** `σ` to a single `K`; this toy shows the **spec-level** requirement: whatever `K` means in `SigVerify` must be **tied** to the witness the verifier actually checked (opened keys), not an arbitrary concurrent field.
