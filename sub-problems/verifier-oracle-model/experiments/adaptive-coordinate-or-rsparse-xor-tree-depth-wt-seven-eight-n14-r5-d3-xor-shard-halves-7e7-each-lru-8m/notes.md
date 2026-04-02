# Notes

- **observation:** First contiguous half and second half took **similar** DP time (~540 s vs ~537 s); asymmetry seen in some `r=9` 6e7/10M runs was **not** reproduced here.
- **dead_end (local):** At **7e7/8M per half**, **contiguous 50% XOR shards** do **not** yield a **`d=3` witness** for **`r=5`**—same negative pattern as **`r=9`** half-shards at **6e7/10M** (different budget/LRU, same structural outcome).
- **insight:** Per-half runtime **>** half of full-menu **7e7** time (~644 s) implies **menu position** matters for where the DP spends its budget; contiguous blocking may not isolate an "easy" sub-language.
- **question:** Would **7e7/8M** on **quarter** shards (four sequential runs) ever complete `d=3` on a shard before budget—worth testing only if wall-clock budget allows ~4× ~?s.
