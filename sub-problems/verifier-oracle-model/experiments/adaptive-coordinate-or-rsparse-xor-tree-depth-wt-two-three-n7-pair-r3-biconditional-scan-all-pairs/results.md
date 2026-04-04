# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-pair-r3-biconditional-scan-all-pairs`

**Outcome:** FAIL

**Setup:** **n=7**, shell **`{2,3}`**, language **coord + full `r=2` XOR menu + exactly two `r=3` XOR splits** (unordered pair of triple indices). **LRU** cap **`4_000_000`**. Exhaustive **`C(35,2)=595`** pairs.

**Baselines:** `coord_only` **`min_d=7`**; **`coord + full n-XOR`** **`min_d=1`** (sanity).

**Measured:**

| Quantity | Value |
|----------|-------|
| `pairs_checked` | 595 |
| `wall_sec` | ~1.74 |
| `witness_min_d2_count` | **0** |
| `violations` (biconditional `min_d=2` ⟺ disjoint) | **70** |

**Interpretation:**

- **Every** unordered pair has **`min_d=3`** for this fixed sparse menu at **n=7** (no depth-2 certificate from **two** triple-XOR splits **+** full **`r=2`**).
- The **70** “violations” are exactly the **70** **disjoint** triple pairs (**7** choices of **6** vertices × **10** complementary **3+3** splits on those **6** points). For those pairs the **n=6-style** predicate predicts **`min_d=2`**, but the DP returns **`min_d=3`**.
- The prior random sample (**200** pairs) saw only **23** disjoint pairs in the draw; the exhaustive scan confirms **all** disjoint pairs share the same failure mode, and **no** pair achieves **`min_d=2`**.

**Conclusion:** The **n=6** “two triples ⟺ depth **2**” phenomenon **does not** persist to **n=7** for this language; the correct coarse statement at **n=7** is **`min_d=3`** throughout (**595/595**).
