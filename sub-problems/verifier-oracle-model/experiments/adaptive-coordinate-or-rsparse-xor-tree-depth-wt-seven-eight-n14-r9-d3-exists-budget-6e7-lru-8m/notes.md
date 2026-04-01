# Notes

- **observation:** At **6×10⁷** `exists_tree` cap, **`r=9` `d=3`** still **PARTIAL**; LRU **saturated** at **8M** — same structural pattern as **`r=5`** at **6e7/8M** and **`r=9`** at **5e7/8M**.
- **insight:** **`r=9`** wall **~562.3 s** vs **`r=5`** **~568.8 s** at **6e7** — similar order; **`r=9`** slightly faster here (unlike needing to infer much from **~7 s** delta on one host).
- **dead_end (local):** **+20%** budget does **not** close **`r=9` `d=3`** at **8M** LRU either — **2002** band remains **open** for **both** dual **`r`** values at this envelope.
