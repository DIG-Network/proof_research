# Notes

- **observation:** Build time for **`r=5`** XOR list ~**2.7 s** per subprocess (full **2002** built then sliced — acceptable overhead).
- **insight:** **LRU 8M** saturated on **every** quarter at **`d=3`**; completion is **not** from staying under cache cap — the search tree **finishes** (reports **`min_d=None`**, **`feasible=False`**) despite saturation, unlike **1001-split** halves at **12e7**.
- **dead_end:** **Contiguous quarter** of **`r=5`** XOR splits is **not** a **`d=3`** witness menu for **`n=14`**, **`{7,8}`** (all four quarters negative).
- **question:** Does **any** **~500-split** **non-contiguous** sample complete with **`feasible=True`**, or is **witness** inherently tied to **larger** XOR fraction (still open for full **2002**)?
