# Results

**Outcome:** **FAIL**

**Setup:** `n=8`, base language `coord + full r=2 + doubleton r=3 + singleton r=4`, then append **exactly four** distinct XOR splits from the full `r=7` menu (`len(p7)=8`). **Exhaustive** enumeration of all **`C(8,4)=70`** index quadruples (lex order via `itertools.combinations`). Off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}` (**107800** cells). **`LRU_CAP=4_000_000`**.

**Measured:**

- Every one of the **70** menus: **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** `d2∧¬pred`, **`0`** false positives on predicate-vs-depth mismatches beyond that pattern.
- **`total_wall_sec≈1233.1`** (~20.6 min) for all **70** menus sequential.
- **`min_stratum_d2_across_menus=max_stratum_d2_across_menus=107800`** — no menu achieves **`0`** or a proper intermediate count on this stratum.

**Conclusion:** The prior **16-trial random** `K=4` probe was **representative**: **every** `K=4` partial `r=7` submenu **saturates** the stratum to universal `min_d=2` in this DP model, same as **full** `r=7` (and the strict full `r∈{5,6,7}` scans).
