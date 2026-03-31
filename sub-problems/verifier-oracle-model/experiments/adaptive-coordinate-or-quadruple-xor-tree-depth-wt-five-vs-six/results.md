# Results — adaptive-coordinate-or-quadruple-xor-tree-depth-wt-five-vs-six

**Outcome:** **PASS**

**Domain:** `n=10`, Hamming weight in `{5,6}`, **462** masks.

**Gate set:** Coordinate **x_i** or **quadruple XOR** **x_i⊕x_j⊕x_k⊕x_l** for all **C(10,4)=210** lexicographic four-tuples.

**Run:** `python script.py --budget-seconds 3600 --d-min 1` (completed under budget).

| d | feasible | elapsed_sec |
|---|----------|-------------|
| 1 | False    | 0.000       |
| 2 | False    | 0.036       |
| 3 | **True** | 0.388       |

**Conclusion:** **`min_d = 3`**.

**Comparison (same 462-set toy):**

| Gate library | min_d |
|--------------|-------|
| 066 coord + pair-XOR | 5 |
| 090 coord + triple-XOR | 4 |
| **091 coord + quad-XOR** | **3** |

**Monotonicity:** **090 ⊂ 091** (omit quad nodes) ⇒ **min_d(091) ≤ min_d(090)**; observed **strict** **4 → 3**.
