# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-r3-plus-each-r4-split-once`

**Outcome:** **FAIL** (the **stated primary hypothesis** in `hypothesis.md` is **falsified**).

**What was tested:** `n=7`, shell `{2,3}`, language **coord + full `r=2` XOR (21 splits) + full `r=3` XOR (35 splits) + exactly one `r=4` XOR split**, scanning all `C(7,4)=35` choices of that quartic split.

**Measured:**

- `r4_checked=35`, `witness_min_d2_count=35`, `min_d_ge3_count=0`
- `total_splits=57` for each run (21+35+1)
- `wall_sec≈0.053` (full scan), `lru_cap=4_000_000`
- Baseline: `coord_only min_d=7`, `coord_plus_full_xor min_d=1` (sanity)

**Interpretation:**

- **Every** choice of a **single** `r=4` XOR parity, together with the **full** `r=2` and `r=3` menus, achieves **`min_d=2`** in this DP model.
- This is **much stronger** than needing the full **`r=4`** menu (35 splits) from the `union r∈{2,3,4}` construction: **one** quartic split is **already** sufficient **once** the full triple menu is present.
- Contrasts with the closed **`r=3`-only ladder** on top of full `r=2`: exhaustive **`C(35,7)`** septuples of **extra** `r=3` splits still gave **`min_d=3`** everywhere (`…-n7-septuple-r3-scan-all-septuples`).

**Script exit code:** `1` (**hypothesis falsified** per repo convention).
