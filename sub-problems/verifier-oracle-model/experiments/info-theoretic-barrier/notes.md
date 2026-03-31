# Notes

- The counting argument distinguishes **injective encoding of which quorum** signed from **sound threshold attestation**. A scheme might avoid encoding a unique `S` while still being sound — but then the verification predicate must not be equivalent to “check signature under `PK_agg(S)` for a hidden `S`” without extra binding.
- Merkle commitment to keys is **binding** on keys but does not, by itself, give a sublinear witness that a **signature** was produced by ≥t of those keys without revealing which.
- Next experiments could formalize a **game** (Ideal functionality + UC) rather than counting alone.
