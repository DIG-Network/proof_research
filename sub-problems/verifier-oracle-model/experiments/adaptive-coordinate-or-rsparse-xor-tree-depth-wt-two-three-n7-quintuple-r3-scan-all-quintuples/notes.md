# Notes — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-scan-all-quintuples`

- **observation:** Full **`C(35,5)=324632`** scan completed with **`witness_min_d2_count=0`**; wall **~766 s** at **`4M`** LRU — consistent with extrapolation from the random **`200`**-quint sample (**`…-random-sample-200`**).
- **insight:** The **`n=6`** phenomenon (**`min_d=2` iff two disjoint triples**) does **not** extend to **`n=7`** when allowing **up to five** triple-parities alongside **full `r=2`**: **no** **`min_d=2`** witness found in the **entire** arity-**5** finite family tested here.
- **dead_end (local):** For this **fixed language template** (**coord + all `r=2` + up to five chosen `r=3`**), **`n=7`** **`{2,3}`** **`min_d=2`** is **ruled out** for arity **≤5** triple-splits by exhaustive enumeration (**pairs → quintuples**).
- **question:** Does **six** triple-parities (**`C(35,6)`**) ever unlock **`min_d=2`**, or is the obstruction **infinite** within **triple-only** augmentation at **`n=7`**?
