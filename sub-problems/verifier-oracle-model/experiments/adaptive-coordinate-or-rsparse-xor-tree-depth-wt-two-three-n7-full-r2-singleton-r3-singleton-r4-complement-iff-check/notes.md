# Notes

- **Independence:** Re-runs the full DP grid; does not assume the prior experiment’s output — only the same parent driver and indexing order (`itertools.combinations` for triples/quads aligned with `build_r_xor_partition_masks`).
- **Why it matters:** Upgrades a human-read pattern from `…-grid-scan` to a falsifiable program: any future change to the DP or mask ordering that breaks the iff would fail this script immediately.
- **Next (optional):** Minimal `(r3 multiset, r4 multiset)` for `min_d=2` when allowing repeated triple/quad splits; or return to anonymous-quorum-binding per session alternation.
