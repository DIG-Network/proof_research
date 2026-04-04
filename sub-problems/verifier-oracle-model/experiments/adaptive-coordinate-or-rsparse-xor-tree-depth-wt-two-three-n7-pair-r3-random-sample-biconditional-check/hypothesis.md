# Hypothesis — n=7 pair of `r=3` splits: `min_d=2` iff disjoint triples? (random sample)

**Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py`  
**Prior:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-pair-r3-complementary-iff-min-d2` proved at **n=6** that **`min_d=2`** **iff** the two triples are **disjoint** (equivalently complementary **3+3** on **[6]**).

**Context:** At **n=7**, **C(7,3)=35** triples; **C(35,2)=595** unordered pairs. Two triples cannot partition **[7]** (no complementary **3+3**), but **disjoint** pairs still exist (**6** vertices covered, **one** left out). Exhaustive **595** DP runs may be heavy in cron time; this experiment uses a **fixed-seed random sample** of pairs to probe whether the **same biconditional** (replacing “complementary” by **disjoint**) still holds.

**Falsifiable claim:** For every sampled unordered pair `{i,j}` of triple indices,

> `min_d(coord + full r=2 + {i,j} r=3 splits) = 2` **if and only if** `|T_i ∩ T_j| = 0`.

- Any violation → **FAIL** (structure changes at **n=7**).
- No violations in sample → **PASS** (evidence only; not an exhaustive **595** proof).

## Analogy pass (mandatory)

1. **Abstract structure:** Same DP language as **n=6**, but the ambient set has **one** extra coordinate; **disjoint** triples are no longer a perfect matching of the ground set — the “partition certificate” story from **n=6** may or may not survive.

2. **Analogous domains:** (i) **Hypergraphs** — **2** edges of size **3** in **K₇**; (ii) **Matroid** **union** — dependence when edges overlap; (iii) **Coding** — supports of weight-**3** codewords and intersection patterns.

3. **Machinery:** Same **min_depth** DP; statistical sampling over the pair space when exhaustive cost is high.

4. **Transfer seed:** Reuse the **n=6** predicate (**disjoint** ⟺ **`min_d=2`**) as a literal guess at **n=7** and let data falsify or support.
