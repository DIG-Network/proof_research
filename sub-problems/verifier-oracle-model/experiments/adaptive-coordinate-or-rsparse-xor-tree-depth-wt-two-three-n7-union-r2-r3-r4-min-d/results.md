# Results

**Outcome:** PASS

## Measured

- **`coord_only min_d=7`** (56 masks, `d_max=7`).
- **`coord_plus_full_7xor min_d=1`**.
- **`coord_plus_union_rs=[2,3,4] total_splits=91 min_d=2`**, **`dp_sec≈0.002`** (4M LRU).

## Reasoning

Hypothesis confirmed: at **`n=7`**, **`{2,3}`** shells, **coord + full `r=2` + full `r=3` + full `r=4`** already admits a **depth-2** decision tree — **`r=5`** parities are **not** required for the known union certificate (contrast **`n7-full-r2-r5-union-min-d`** which used **`r∈{2,3,4,5}`** and also reported **`min_d=2`**). Together with the exhaustive **quintuple `r=3`** failure, this locates the “missing strength” between **finite few-triple** languages and **full `r=4`** menu.
