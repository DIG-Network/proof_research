# Notes

- **observation:** Exhaustive singleton scan is cheap here (`10` DP runs × `11` splits each).
- **insight:** `min_d=2` with `full r=2 + one r=3` is **label-symmetric** over triples at `n=5` — no “special” triple from the menu’s combinatorial ordering.
- **dead_end:** Hypothesis “only index `0` works” was a **search-order artifact** from the prior experiment’s lexicographic `k=1` witness finder, not a parity-theoretic fact.
- **question:** For larger `n`, is “any one `r=3` split + full `r=2`” still always sufficient for the analogous `min_d` drop, or does `n=5` overstate symmetry?
