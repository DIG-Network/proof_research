# Notes

- **observation:** Definite **`d=3 feasible=False`** for **`coord+3xor`** with **364** splits — first **`n=14`** **`r=3`** data point at **5e7/8M**; contrasts **`r=5`/`r=9`** **PARTIAL** (no feasibility bit).
- **observation:** LRU **saturated** (**8M** **`exists_tree`** misses) yet probe **finished** — bounded memo is **tight** but **not** truncating the **`d=3`** conclusion here (unlike **PARTIAL** runs that stop mid-search).
- **insight:** **Cardinality** **`C(14,r)`** is a poor **solo** predictor: **364** certifies **`d=3` out** **fast** (~82 s); **1001** (**`r=4`**) **PARTIAL** at same envelope; **2002** **PARTIAL**; **3432** (**`r=7`**) **trivial** PASS — **hardness** is **regime**-dependent, not monotone in **`|menu|`**.
- **question:** What is **`min_d`** for **`r=3`** exactly (**≥4**)? A **`d=4`-only** shard would certify without the full **`min_d`** scan.
- **next:** **`r=3`** **`d=4`** probe or extend **`min_d(r)`** row in digest; avoid parallel **10M×2** XOR workers on this host.
