# Notes — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-septuple-r3-random-sample-400`

- **observation:** Wall time **~1.1 s** for **400** septuple DP calls — each call is cheap vs **1.62M** sextuple exhaustive scan (**~61 min**).
- **dead_end (sample-level):** This **400-draw** sample contains **no** **`min_d=2`** witness; consistent with exhaustive **six**-tuple closure (**all** **`min_d=3`**) but **not** a proof for **seven**.
- **question:** Does **any** septuple achieve **`min_d=2`**, or is the sparse triple ladder still **`min_d=3`** through full **`C(35,7)`**? Only exhaustive scan (or a smarter witness search) can close this.
- **next step:** Full **`C(35,7)`** scan (**~6.7M** combinations, extrapolated **multi-hour** wall) **or** structured / hitting-set search smaller than the full cross-product.
