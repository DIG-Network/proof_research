# Notes

- **observation:** Both halves saturated **10M** LRU at **`max_exists_calls=150000000`**; second half slightly faster DP (**~1118** s vs **~1167** s) mirroring prior **12e7** asymmetry between shards.
- **dead_end (local):** For this host envelope, **+25%** `exists_tree` budget over **12e7/10M** half-shards is **insufficient** to escape PARTIAL on **`r=9`** `d=3` probes—do not expect a small incremental bump alone to finish.
- **insight:** Wall time scaled **roughly** with the higher cap (**~38** min vs **~35** min for **12e7/10M**), consistent with LRU-miss-dominated work near the cap rather than an early witness.
- **question:** Does **18e7–20e7** at **10M** (or **15e7** at **11M** if memory allows) ever complete on either half, or does the frontier grow faster than **O(budget)** in this band?
