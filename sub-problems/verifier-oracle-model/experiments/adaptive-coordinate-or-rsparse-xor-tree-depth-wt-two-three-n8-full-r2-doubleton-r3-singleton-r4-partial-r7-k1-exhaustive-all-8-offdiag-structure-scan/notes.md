# Notes

- **observation:** Wall time per menu decreases monotonically with index **1→8** in this run (~39s → ~13s); likely cache warmth from shared LRU across the sequential loop, not a semantic difference between splits.
- **insight:** Together with **`K∈{2,3,4}`** exhaustive scans, this closes the **entire partial `r=7` submenu lattice** at **`n=8`** for **`0 < stratum_min_d2 < 107800`**: **no** nonempty proper subset of the **8** full-**`r=7`** splits escapes the **`107800`** universal **`min_d=2`** plateau on this off-diagonal stratum.
- **dead_end:** Searching for a **middle** **`d2`** mass by varying **only** how many **`r=7`** XOR splits are included (holding base **`{2,3,4}`** fixed) — **fully exhausted** at **`n=8`** for **`s∈{0,1,2}`**.
- **question:** Does a **partial** menu inside **`r=5`** or **`r=6`** (not the full **`C(8,r)`** list) allow **`0 < stratum_min_d2 < 107800`**, or is the cliff equally sharp below full arity?
