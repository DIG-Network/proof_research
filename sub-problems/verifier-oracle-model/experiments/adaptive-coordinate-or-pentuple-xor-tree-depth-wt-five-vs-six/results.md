# Results — adaptive-coordinate-or-pentuple-xor-tree-depth-wt-five-vs-six

**Outcome:** **PASS**

**Gate set:** **Coordinate** **x_i** **or** **5-sparse** **XOR** **⊕** **over** **each** **lexicographic** **5-tuple** **(** **C(10,5)=252** **)** **.** **No** **3/4-XOR** **primitives,** **no** **total** **10-bit** **parity** **(** **092** **).**

**Run:** `python script.py --budget-seconds 7200 --d-min 1`

| d | feasible | elapsed_sec |
|---|----------|-------------|
| 1 | False    | ~0          |
| 2 | **True** | ~0.005      |

**Conclusion:** **`min_d = 2`.**

**Comparison (same 462-set, adaptive `pure_bits` trees):**

| Primitives (per node, + coords) | min_d |
|---------------------------------|-------|
| 091 quad-XOR only | 3 |
| **093 pentuple-XOR only** | **2** |
| 092 total XOR | 1 |

**Note:** **091** **and** **093** **gate** **sets** **are** **incomparable** **(** **each** **omits** **splits** **the** **other** **has** **),** **yet** **5-sparse-only** **achieves** **strictly** **lower** **depth** **than** **4-sparse-only** **here.**
