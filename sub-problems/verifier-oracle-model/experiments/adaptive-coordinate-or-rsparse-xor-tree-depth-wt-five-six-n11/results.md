# Results: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n11

**Outcome:** PASS

**Setup:** `n=11`, domain = masks with Hamming weight in `{5,6}` (`C(11,5)+C(11,6)=924`). Majority `t=6`: wt 5 = one below quorum, wt 6 = quorum (same shell *labels* as **098–099**, larger ambient `n`).

**Coord-only:** `min_d = 11`.

**Coord + full 11-bit XOR:** `min_d = 1`.

**Single-arity r-sparse XOR** (`coord + all `C(11,r)` splits):

| r | partition count | min_d |
|---|-----------------|-------|
| 2 | 55 | 6 |
| 3 | 165 | 5 |
| 4 | 330 | 4 |
| 5 | 462 | 3 |
| 6 | 462 | 3 |
| 7 | 330 | 3 |
| 8 | 165 | **4** |
| 9 | 55 | 3 |
| 10 | 11 | 2 |

**`min_d(r)`** is **not monotone** (`r=8` worse than `r∈{5,6,7,9}`), but **unlike `n=10` (099)** there is **no** **`min_d(6),min_d(7) > min_d(5)`** **regression** — **`r=5,6,7`** **all** **plateau** **at** **3** **.**

**Unions:**

- `r ∈ {2,3,4}`: `min_d = 3`
- `r ∈ {2,3,4,5}`: `min_d = 3` (**contrast 099:** `n=10` gave **`2`** here)
- `r ∈ {2,…,10}`: `min_d = 2`

**Script:** `script.py` (exit 0, `PASS`). Wall time ~144 s (dominated by `r=3` then `r=2` DP).
