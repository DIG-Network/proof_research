# Results

**Outcome:** PASS

## Command

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n13-full-r2-r12-union-min-d/script.py
```

(equivalent to parent with `--union-rs 2,3,4,5,6,7,8,9,10,11,12` and `--lru-maxsize 4000000`)

## Measured outputs

| Quantity | Value |
|----------|-------|
| Masks (`C(13,7)+C(13,8)`) | 3003 |
| Full union total XOR splits | 8177 |
| Baseline `coord_only` `min_d` | 13 |
| Baseline `coord_plus_full_13xor` `min_d` | 1 |
| Union language `min_d` | **2** |
| Union DP wall time | ~0.057 s (script-reported `dp_sec`) |
| End-to-end wall time (single run, cold) | ~39 s (includes full `d=1..13` baseline scan) |

## Reasoning

The parent driver scans **`d`** until the first feasible depth. For the combined **`coord + ⋃_{r=2}^{12} XOR_r`** language, the first feasible depth is **`d=2`**, so **`d=1`** is infeasible. This matches the **`n=14`** full **`r=2..13`** union outcome (**`min_d=2`**, **`16368`** splits), supporting that **`min_d=2`** is not special to **`n=14`** alone for this **`{7,8}`** majority slice.
