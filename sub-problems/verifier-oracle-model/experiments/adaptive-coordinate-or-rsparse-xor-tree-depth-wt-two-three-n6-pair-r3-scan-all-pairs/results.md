# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-pair-r3-scan-all-pairs`

**Outcome:** PASS

**Setup:** `n=6`, masks with popcount in `{2,3}` (35 masks). Language: **coord splits + full `r=2` XOR menu (15 splits) + exactly two `r=3` splits** indexed by an unordered pair `{i,j}` from `C(6,3)` in lex order (20 triples). LRU memo cap `4_000_000`.

**Baselines:** `coord_only` → `min_d=6`; `coord + full 6-XOR` → `min_d=1`.

**Scan:** All `C(20,2)=190` pairs. Wall time ~`0.12` s.

**Finding:** **10** pairs achieve **`min_d=2`**. They are exactly the **10 complementary pairs** of disjoint triples that partition `[6]`:

- Indices `(0,19)`, `(1,18)`, …, `(9,10)` in lex order on `combinations(range(6),3)`.
- Example: triple `0` = `{0,1,2}`, triple `19` = `{3,4,5}`; triple `9` = `{0,4,5}`, triple `10` = `{1,2,3}`.

**Contrast:** Singleton `r=3` + full `r=2` always gave `min_d=3` (parent experiment 139). **Two** triple splits suffice for `min_d=2` iff the two triples are **complementary** (a 3+3 vertex cut); arbitrary pairs of triples still need depth 3.

**Implication:** Minimal `k` for `r=3` slices in this shell is **2** (not 20), but only for this structured family of pairs — not for all pairs.
