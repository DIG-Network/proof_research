# Results: n=7 full r=2 + singleton r=3 + singleton r=4 — full grid

**Outcome:** PASS (primary hypothesis confirmed)

**Setup:** `n=7`, shell `{2,3}` (56 masks), coordinate splits + **full** `r=2` XOR menu (21 splits) + **one** `r=3` XOR split + **one** `r=4` XOR split. Exhaustive grid `35×35 = 1225` pairs of split indices. LRU memo cap `4_000_000`, `d_max=n`.

**Counts:**

| Metric | Value |
|--------|-------|
| `min_d == 2` | **35** |
| `min_d >= 3` | **1190** |
| Wall time (full grid) | ~**1.69** s |

**Sharp structure (verified combinatorially on the grid output):** `min_d == 2` **iff** the chosen 4-subset for `r=4` is the **set complement** in `[7]` of the chosen 3-subset for `r=3`. There are exactly **35** such complementary pairs (bijection between triples and their 4-complements). No other `(r3, r4)` pair achieves depth 2.

**Interpretation:** With only **one** triple parity and **one** quartic parity on top of the full pair-XOR menu, a depth-2 certificate is **exceedingly rare** — it requires the quartic XOR to be the complementary partition to the triple (equivalently, the triple and quad define a **3+4 split of all 7 indices**). This refines the prior “full `r=3` + any `r=4` → uniform `min_d=2`” result: **richness of the triple menu** was doing the work; a single triple almost always leaves `min_d=3` unless the quartic is locked to its complement.

**Command:**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-singleton-r3-singleton-r4-grid-scan/script.py
```
