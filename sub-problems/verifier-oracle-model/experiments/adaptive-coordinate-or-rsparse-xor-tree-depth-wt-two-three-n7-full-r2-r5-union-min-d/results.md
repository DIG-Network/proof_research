# Results

**Outcome:** PASS

## Measured

- **`coord_only min_d=7`** (trivial on 56 masks, `d_max=7`).
- **`coord_plus_full_7xor min_d=1`**.
- **`coord_plus_union_rs=[2,3,4,5] total_splits=112 min_d=2`**, **`dp_sec≈0.001`** (4M LRU).

## Reasoning

Hypothesis confirmed: full multi-arity XOR union through **`r=n-1=5`** on **`n=7`**, **`{2,3}`** shells matches the **`min_d=2`** certificate already observed for **`n∈{8,…,14}`**.
