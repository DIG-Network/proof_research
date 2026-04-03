# Results

**Outcome:** PASS

## Measured

- **`coord_only min_d=10`** (`d_max=10` scan).
- **`coord_plus_full_10xor min_d=1`**.
- **`coord_plus_union_rs=[2,…,9] total_splits=1012 min_d=2`** with **`dp_sec≈0.003`** (4M LRU memo).
- Wrapper echoed parent: **`--union-rs 2,3,4,5,6,7,8,9 --lru-maxsize 4000000`**.

## Conclusion

The full multi-arity XOR union at **`n=10`**, **`{5,6}`** has **`min_d=2`**, extending the certified ladder to **`n∈{10,11,12,13,14}`** for this shell geometry.
