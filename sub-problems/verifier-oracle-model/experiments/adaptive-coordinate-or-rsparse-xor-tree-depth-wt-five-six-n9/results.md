# Results: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n9

**Outcome:** PASS

**Setup:** `n=9`, domain = masks with Hamming weight in `{5,6}` (`C(9,5)+C(9,6)=210`). Same weight shells as `(10,{5,6})` experiments; for `n=9` majority `t=5`, both shells are quorum-sized — this run is the **shell-separation** toy only.

**Coord-only:** `min_d = 9` (needs full adaptive coordinate depth).

**Coord + full 9-bit XOR:** `min_d = 1` (odd wt 5 vs even wt 6).

**Single-arity r-sparse XOR library** (`r=2..8`, excluding full `n` in the sweep label):

| r | partition count | min_d |
|---|-----------------|-------|
| 2 | 36 | 5 |
| 3 | 84 | 3 |
| 4 | 126 | 3 |
| 5 | 126 | 3 |
| 6 | 84 | 4 |
| 7 | 36 | 3 |
| 8 | 9 | 2 |

**Unions (coord + listed r-libraries):**

- `r ∈ {2,3,4}`: `min_d = 3`
- `r ∈ {2,3,4,5}`: `min_d = 2`
- `r ∈ {2..8}`: `min_d = 2`

**Script:** `script.py` (exit 0, prints `PASS`).
