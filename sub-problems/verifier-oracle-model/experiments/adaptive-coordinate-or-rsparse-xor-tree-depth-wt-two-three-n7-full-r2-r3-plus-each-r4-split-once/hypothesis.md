# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-r3-plus-each-r4-split-once`

## Analogy pass

1. **Abstract structure:** We search a **finite menu** of binary partitions (coordinate + XOR shards) for the **minimal decision-tree depth** that separates pure subsets of a fixed mask shell. Adding one new partition is a **single degree of freedom** in a **35-dimensional** family (`C(7,4)` quartic XOR splits). The question is whether **one** extra direction can collapse depth the way **35** new directions (full `r=4` menu) collectively do in the known `min_d=2` union.

2. **Where else:** (i) **Basis pursuit / sparse recovery** — does one extra measurement vector resolve ambiguity when a full measurement bank would? (ii) **Matroid / rank** — one extra independent constraint can change flat dimension, or change nothing if redundant. (iii) **Coding** — one extra parity check may or may not lower covering radius of a syndrome partition.

3. **Machinery in those domains:** LP relaxation gaps; matroid rank tests; minimum distance vs. parity-check rank.

4. **Transfer candidate:** Treat each `r=4` XOR split as an **independent constraint direction** relative to the `r=2`+`r=3` span of partitions. **Falsifiable claim:** if **no** single direction lowers `min_d`, then **`min_d=2`** at this slice **requires** **overlap** among **multiple** `r=4` parities (consistent with prior `union {2,3}` vs `{2,4}`-only results).

## Falsifiable claim (pre-registered; **falsified** by run)

For `n=7`, shell `{2,3}`, language **coord + full `r=2` XOR (21) + full `r=3` XOR (35) + exactly one `r=4` XOR split** (each of the 35 choices):

- **Primary (expected, WRONG):** **`min_d = 3`** for **all 35** choices (`witness_min_d2_count = 0`).
- **Falsification:** **Any** choice yields **`min_d = 2`**.

**Result:** **All 35** choices yield **`min_d = 2`** (`witness_min_d2_count=35`, `min_d_ge3_count=0`). The “needs many overlapping `r=4` parities” story is **not** supported here: **one** quartic split suffices **after** the **full** triple-XOR menu is included.

Parent driver: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py`.
