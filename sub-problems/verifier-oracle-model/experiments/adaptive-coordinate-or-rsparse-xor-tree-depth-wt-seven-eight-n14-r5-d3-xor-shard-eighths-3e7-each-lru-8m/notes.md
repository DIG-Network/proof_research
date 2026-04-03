# Notes — n14 r=5 d=3 XOR eighth-shards 3e7×8

- **observation:** Parent subprocesses print **`PASS`** when the **`d=3`** probe completes; the wrapper maps “no witness” to exit **1** (same as quarter / half wrappers).
- **insight:** **LRU** headroom at **~250**-split scale is large vs **~500**-split quarters at **2×** per-shard budget — **PARTIAL** at quarters was consistent with **working-set** size, not only global **`exists_tree`** totals.
- **question:** Would **6×10⁷** on **~250**-split eighths reproduce quarter-style **8M** saturation (stress test), or is **251** always “easy” for memo?
- **dead_end:** None opened — eighths **confirm** quarter **`d=3`** **`False`** pattern without new positive witness.
