# Results

**Outcome:** PASS

## Measured

- **`coord_only min_d=6`** (`d_max=6`).
- **`coord_plus_full_6xor min_d=1`**.
- **`coord_plus_union_rs=[2, 3, 4] total_splits=50 min_d=2`**, `dp_sec≈0.000` (sub-millisecond on this host).
- Wrapper command: `python3 .../adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6/script.py --union-rs 2,3,4 --lru-maxsize 4000000`.

## Verdict

Hypothesis confirmed: full multi-arity XOR union through **`r=n-2=4`** yields **`min_d=2`** on the **`35`**-mask **`{2,3}`** slice, matching the **`n≥7`** ladder pattern.
