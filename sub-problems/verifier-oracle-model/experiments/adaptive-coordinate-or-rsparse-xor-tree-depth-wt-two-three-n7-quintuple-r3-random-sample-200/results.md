# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-random-sample-200`

**Outcome:** **FAIL** (hypothesis: at least one random quintuple achieves `min_d=2`)

**Measured:**

- `sample_quints=200` (universe `C(35,5)=324632`, `seed=0`)
- `witness_min_d2_count=0`
- `lru_cap=4000000`
- `wall_sec≈0.486`

**Interpretation:** In this **random** probe, **no** depth-**2** certificate appeared for **coord + full `r=2` + five `r=3`** XOR splits at **n=7**, **`{2,3}`**. This is **not** an exhaustive **`C(35,5)`** proof (unlike the quadruple scan); it supports scheduling a **full** quintuple enumeration or a larger sample if we need a definitive finite statement at arity **5**.
