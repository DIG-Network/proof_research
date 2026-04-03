# Results

**Outcome:** PASS

## Measured

- **Baselines:** `coord_only min_d=12` (d=1..11 infeasible, d=12 feasible); `coord_plus_full_12xor min_d=1` (d=1 feasible).
- **Full multi-arity XOR union:** `coord_plus_union_rs=[2,3,4,5,6,7,8,9,10,11]` with **`total_splits=4082`**, **`min_d=2`**, **`dp_sec≈0.024`** (4M LRU memo cap).
- **Command:** parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12/script.py --union-rs 2,3,4,5,6,7,8,9,10,11 --lru-maxsize 4000000`.

## Conclusion

The full `r=2..n-1` XOR union on the `n=12`, `{6,7}` majority slice has **`min_d=2`**, matching the pattern already recorded for **`n=13`** and **`n=14`**.
