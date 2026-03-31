# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-four-five-n8`

**Outcome:** PASS (DP complete; **H2** / **H3** refined — **H2** as stated is **false**)

**Domain:** `n=8`, `popcount(x) ∈ {4,5}` (**126** masks). Majority **`t=5`**; note **`n ≠ 2t−1`** (**`9`**).

## `min_d` by language

| Language | `#` XOR primitives (when applicable) | `min_d` |
|----------|--------------------------------------|--------|
| Coordinate only | 0 | **8** (= `n`) |
| Coord + full **8**-bit XOR | 1 | **1** |
| Coord + all **pair** XORs | 28 | **4** |
| Coord + all **triple** XORs | 56 | **4** |
| Coord + all **quad** XORs | 70 | **2** |
| Coord + all **5-tuple** XORs | 56 | **4** |
| Coord + **pair ∪ triple ∪ quad** | — | **2** |
| Coord + **∪_{r=2}^{5} r`-sparse`** | — | **2** |

## Reasoning

- **H1:** Full **n**-bit parity splits **even** weight **4** vs **odd** weight **5** in one node → **`min_d=1`**. **Confirmed.**
- **H2 (refuted):** **`min_d(r)`** is **not** monotone in **`r`**. Here **`min_d(4)=2 < min_d(3)=min_d(2)=min_d(5)=4`**. In particular **5-sparse-only** is **strictly worse** than **4-sparse-only** (**4 vs 2**), unlike **`(10,{5,6})`** where **pentuple** beat **quad**.
- **H3:** Union **`r∈{2,3,4,5}`** achieves **`min_d=2`** (**≤ 2**). **Confirmed**; adding **5-tuples** to **`{2,3,4}`** does **not** beat **`min_d=2`** here.

**Contrast:**

| Instance | `min_d` pair | triple | quad | 5-sparse |
|----------|--------------|--------|------|----------|
| `(10,{5,6})` | 5 | 4 | 3 | 2 |
| `(7,{3,4})` | 4 | 3 | **3** | — |
| `(8,{4,5})` | 4 | **4** | **2** | **4** |
