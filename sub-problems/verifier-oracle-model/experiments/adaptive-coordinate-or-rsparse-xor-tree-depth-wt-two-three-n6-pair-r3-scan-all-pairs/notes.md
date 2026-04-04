# Notes

- The **10** witnesses match **`C(6,3)/2 = 10`** partitions of six labeled vertices into two disjoint triples (each partition counted once as an unordered pair of triples).
- Complementarity is the natural interpretation: two **disjoint** triple XORs act like a **3-vs-3** split of the coordinate set `{0,…,5}`, analogous to a single coordinate split at `n=5` but requiring **two** parity bits to separate the two halves at `n=6`.
- Next structural step (if needed): triples that **overlap** on 1 or 2 vertices — the remaining `190 - 10 = 180` pairs — apparently never reach `min_d=2` with only full `r=2` + those two triples (empirically from this scan).
