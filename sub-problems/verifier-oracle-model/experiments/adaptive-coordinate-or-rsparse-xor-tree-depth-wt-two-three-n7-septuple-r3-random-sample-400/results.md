# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-septuple-r3-random-sample-400`

**Outcome:** **FAIL**

**Setup:** `n=7`, mask shell `{2,3}`, language **coord + full `r=2` XOR menu + seven** chosen **`r=3`** XOR splits (unordered septuple of indices into the **35** triple masks). **`SAMPLE_SEPTS=400`**, **`SEED=0`**, **`LRU_CAP=4_000_000`**.

**Measured:**

- `baseline coord_only min_d=7`, `coord_plus_full_xor min_d=1` (sanity).
- `sample_septs=400`, `total_universe=6724520` (**`C(35,7)`**).
- `wall_sec≈1.086`.
- `witness_min_d2_count=0` — **no** septuple in this draw achieved **`min_d=2`**.

**Conclusion:** Random probe finds **no** depth-**2** certificate at **seven** triple-parities in this sample. This is **evidence only** — it does **not** replace exhaustive **`C(35,7)`** enumeration (cf. quintuple random sample superseded by full **`C(35,5)`**).
