# Notes

- **observation:** **~27.4 min** total wall for **18e7** cap — longest successful **full-menu** **`r=9`** **`d=3`** shard completed on this path without OOM (**10M** LRU safe).
- **observation:** Marginal **~679 s** over **12e7** baseline implies **~1.13×10⁻⁵ s** per extra `exists_tree` invocation once LRU is full (order-of-magnitude sanity check for planning **24e7** / **30e7** attempts).
- **dead_end:** Treating **`d=3 feasible=False`** in a **PARTIAL** run as evidence of **`min_d>3`** would be **unsound** — need completion or independent **lower-depth** certificates (already have **`d=2`** out for **`r=5`** family).
- **question:** Does **interleaving** XOR split order (non-canonical **2002** order) change **cache** locality enough to finish under **10M** LRU without raising cap? (Not tested here.)
