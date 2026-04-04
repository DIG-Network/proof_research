# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-scan-all-quintuples`

**Outcome:** **FAIL** (hypothesis: some unordered quintuple of triple indices achieves `min_d=2`)

**Measured:**

- `quints_checked=324632` (full `C(35,5)` enumeration)
- `witness_min_d2_count=0` (every quintuple: `min_d=3`)
- `lru_cap=4000000`
- `wall_sec≈765.946` (~12.8 min)

**Interpretation:** At **n=7**, shell **`{2,3}`**, **no** depth-**2** certificate exists in this DP model for **coord + full `r=2` XOR menu + any five `r=3` XOR splits** (unordered). Together with prior exhaustive **pair / triple / quadruple** scans, **every** choice of **at most five** triple-parities still leaves **`min_d=3`**.

**Next structural step (outside this experiment):** arity **six** would be **`C(35,6)=1_623_160`** sextuples — larger combinatorial envelope; or change the split family (e.g. add **`r=4`** sparse XORs, unions, or a different shell).
