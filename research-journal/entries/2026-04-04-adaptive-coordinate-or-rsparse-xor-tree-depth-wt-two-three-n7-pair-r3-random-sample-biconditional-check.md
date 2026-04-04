# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-pair-r3-random-sample-biconditional-check`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-pair-r3-random-sample-biconditional-check`

**Context:** verifier-oracle-model (**n=7**, shell **`{2,3}`**, coord + full **`r=2`** + two **`r=3`** splits)

**Hypothesis tested:** Lift the **n=6** exact biconditional: **`min_d=2`** iff the two triples are **disjoint** (at **n=7**, disjoint no longer means a **3+3** partition of the ground set).

**Outcome:** FAIL

**Key finding:** Random sample (**200** / **595** pairs, seed **0**) found **23** violations: **disjoint** triples with **`min_d=3`**, not **2**. The **n=6** “disjoint ⟺ depth-2” structure is **not** dimension-free for this minimal two-triple language.

**Implications:**

- Any **n>6** story must separate **complementary** **3+3** (**n=6**) from **disjoint-but-uncovered** vertex (**n=7**).
- Characterizing **`min_d=2`** at **n=7** for sparse XOR menus likely needs **finer** predicates than **disjointness** alone (or **more** splits / larger unions).

**Analogy pass summary:** Hypergraph / matroid-union viewpoint: extra ground-set element changes which **certificates** exist at depth **2**.

**Scope:** Sampled check only; exhaustive **595** pairs not run here.
