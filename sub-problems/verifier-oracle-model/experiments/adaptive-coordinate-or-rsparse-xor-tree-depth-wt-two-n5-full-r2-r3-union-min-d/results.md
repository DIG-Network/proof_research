# Results

**Outcome:** FAIL (hypothesis falsified; script exit **0** per repo convention)

## Measured

- **`coord_only min_d=1`** (`d_max=5`).
- **`coord_plus_full_5xor min_d=1`**.
- **`coord_plus_union_rs=[2, 3] total_splits=20 min_d=1`**, `dp_sec≈0.000`.
- Wrapper command: `python3 .../adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py --union-rs 2,3 --lru-maxsize 4000000`.

## Verdict

Hypothesis **rejected**: on the **`10`**-mask weight-**`2`** slice at **`n=5`**, the full **`r=2..3`** XOR union already has **`min_d=1`**, so the **`min_d=2`** certificate **does not** extend to **`n=5`**.
