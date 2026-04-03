# Results

**Outcome:** PASS

## Measured

- **`coord_only min_d=9`** (`d_max=9` scan).
- **`coord_plus_full_9xor min_d=1`**.
- **`coord_plus_union_rs=[2,…,8] total_splits=501 min_d=2`** with **`dp_sec≈0.001`** (4M LRU memo).
- Wrapper echoed parent: **`--union-rs 2,3,4,5,6,7,8 --lru-maxsize 4000000`**.

## Conclusion

The full multi-arity XOR union at **`n=9`**, **`{4,5}`** has **`min_d=2`**, extending the certified ladder to **`n∈{9,10,11,12,13,14}`** for this shell geometry.
