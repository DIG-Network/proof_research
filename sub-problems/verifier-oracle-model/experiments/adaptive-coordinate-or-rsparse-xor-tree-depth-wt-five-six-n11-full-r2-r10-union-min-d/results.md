# Results

**Outcome:** PASS

## Measured

- **`coord_only min_d=11`** (`d_max=11` scan).
- **`coord_plus_full_11xor min_d=1`**.
- **`coord_plus_union_rs=[2,…,10] total_splits=2035 min_d=2`** with **`dp_sec≈0.008`** (4M LRU memo).
- Wrapper command echoed parent invocation with **`--union-rs 2,3,4,5,6,7,8,9,10 --lru-maxsize 4000000`**.

## Conclusion

The full multi-arity XOR union at **`n=11`**, **`{5,6}`** has **`min_d=2`**, extending the same **`min_d=2`** pattern already certified for **`n∈{12,13,14}`** on the analogous shells.
