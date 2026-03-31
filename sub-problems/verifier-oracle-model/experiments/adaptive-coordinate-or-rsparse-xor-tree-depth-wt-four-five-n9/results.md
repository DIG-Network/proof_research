# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-four-five-n9`

**Outcome:** PASS

**Domain:** `n=9`, `popcount(x) ∈ {4,5}` (**252** masks). Majority **`t=5`**, **`n = 2t − 1`** (complement swaps the two shells).

## `min_d` by language

| Language | `#` XOR primitives (if applicable) | `min_d` |
|----------|-------------------------------------|--------|
| Coordinate only | 0 | **9** |
| Coord + full **9**-bit XOR | 1 | **1** |
| Coord + pair (`r=2`) | 36 | **5** |
| Coord + triple | 84 | **3** |
| Coord + quad | 126 | **3** |
| Coord + 5-tuple | 126 | **3** |
| Coord + 6-tuple | 84 | **4** |
| Coord + 7-tuple | 36 | **3** |
| Coord + 8-tuple | 9 | **2** |
| Coord + **∪ r∈{2,3,4}** | — | **3** |
| Coord + **∪ r∈{2,…,5}** | — | **2** |
| Coord + **∪ r∈{2,…,8}** | — | **2** |

## Reasoning

- **H1:** Even **wt=4** vs odd **wt=5** → full **n**-bit parity splits in **one** node. **Confirmed.**
- **H2:** **`min_d(r)`** is **not** monotone: **local** **plateau** **`r∈{3,4,5}`** **and** **`r=7`** **at** **`3`**, **interior** **peak** **`r=6`** **at** **`4`**, **`r=8`** **at** **`2`**. **Contrasts** **`(8,{4,5})`** **where** **`r=4`** **was** **global** **minimum** **among** **`r≤5`** **.**
- **H3:** **Union** **`r≤5`** **already** **`min_d=2`** **;** **adding** **`r=6..8`** **does** **not** **improve** **below** **2** **here** **.**

**Cross-row snapshot (same adjacent shells **4** vs **5**):**

| `n` | `n=2t−1?` | pair | `r=3..5` | `r=6` | `r=7` | `r=8` | union 2–5 |
|-----|-----------|------|----------|-------|-------|-------|-----------|
| 8 | no | 4 | all **4** for r=2,3,5; **2** for r=4 | — | — | — | **2** |
| 9 | yes | 5 | **3** for r=3,4,5 | **4** | **3** | **2** | **2** |
