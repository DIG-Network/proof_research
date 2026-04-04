# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-pair-r3-complementary-iff-min-d2`

**Outcome:** PASS

**Setup:** `n=6`, masks with popcount in `{2,3}`. Language: **coord + full `r=2` XOR menu (15 splits) + exactly two `r=3` splits** `{i,j}`. LRU memo cap `4_000_000`. Same baselines as experiment 140.

**Claim tested:** For unordered pairs of triple indices `0 ≤ i < j < 20`, with triples in lex order on `C(6,3)`:

> `min_d = 2` **if and only if** the two triples are **disjoint** (hence complementary 3+3, since each has size 3).

**Scan:** All `C(20,2)=190` pairs. Wall time ~`0.12` s.

**Finding:** **`violations=0`**. The empirical classification from experiment 140 is **exact**: non-complementary pairs always give **`min_d=3`**; complementary pairs always give **`min_d=2`**.

**Implication:** The “10 witness pairs” phenomenon is not an incomplete description of a larger witness family — it is **equivalent** to the purely combinatorial **disjoint-triple** predicate under this fixed menu.
