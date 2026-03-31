# Results: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n10

**Outcome:** PASS

**Setup:** `n=10`, domain = masks with Hamming weight in `{5,6}` (`C(10,5)+C(10,6)=462`). Majority threshold slice: wt 5 = one below quorum (`t=6`), wt 6 = quorum.

**Coord-only:** `min_d = 10`.

**Coord + full 10-bit XOR:** `min_d = 1`.

**Single-arity r-sparse XOR** (`coord + all `C(10,r)` XOR splits only):

| r | partition count | min_d |
|---|-----------------|-------|
| 2 | 45 | 5 |
| 3 | 120 | 4 |
| 4 | 210 | 3 |
| 5 | 252 | 2 |
| 6 | 210 | **3** |
| 7 | 120 | **4** |
| 8 | 45 | 3 |
| 9 | 10 | 2 |

**`min_d(r)` is not monotone in `r`:** `r=5` achieves depth **2**, but **`r=6` needs 3** and **`r=7` needs 4** (strict regression vs `r=5`-only), then `r=8→3`, `r=9→2`.

**Unions (coord + listed libraries):**

- `r ∈ {2,3,4}`: `min_d = 3` (matches **091**-era quad ceiling before pentuple).
- `r ∈ {2,3,4,5}`: `min_d = 2` (**093**).
- `r ∈ {2,…,9}`: `min_d = 2` (lower arities in the union mask the `r=6,7` regression).

**Cross-check:** Spot depths **066 / 090 / 091 / 093** for `r∈{2,3,4,5}` agree with this table.

**Script:** `script.py` (exit 0, prints `PASS`).
