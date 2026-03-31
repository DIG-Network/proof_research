# Results — adaptive-coordinate-or-total-parity-xor-tree-depth-wt-five-vs-six

**Outcome:** **PASS**

**Gate set:** Coordinate **x_i** **or** **one** **total** **XOR** **⊕_{r=0}^{9} x_r** **(** **global** **Hamming** **parity** **).**

**Partition sizes on the 462-set:** **even** **popcount** **=** **210** **(** **all** **wt=6** **),** **odd** **=** **252** **(** **all** **wt=5** **).** **Each** **side** **is** **`pure_bits`** **—** **single** **split** **suffices.**

**Run:** `python script.py` **(** **default** **budget** **).**

| d | feasible | elapsed_sec |
|---|----------|-------------|
| 1 | **True** | ~0         |

**Conclusion:** **`min_d = 1`.**

**Context vs 091:** **091** **allowed** **only** **parity** **on** **≤4** **coordinates** **per** **node** **(** **plus** **coords** **).** **Full** **10-bit** **XOR** **is** **not** **among** **those** **210** **quad** **gates** **—** **it** **is** **weight-10** **on** **the** **dual** **vector.** **So** **depth** **drops** **3 → 1** **when** **the** **verifier** **may** **ask** **global** **parity** **once.**
