# Results

**Outcome:** PASS

**Run:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-three-four-n8-full-r2-r7-union-min-d/script.py`

**Observed:**

- `coord_only min_d=8` (d_max=8)
- `coord_plus_full_8xor min_d=1`
- `coord_plus_union_rs=[2, 3, 4, 5, 6, 7] total_splits=246 min_d=2` with `dp_sec≈0.001`

**Conclusion:** Full XOR union on **`n=8`**, **`{3,4}`** (**126** masks) has **`min_d=2`**, matching the ladder from **`n=9..14`**.
