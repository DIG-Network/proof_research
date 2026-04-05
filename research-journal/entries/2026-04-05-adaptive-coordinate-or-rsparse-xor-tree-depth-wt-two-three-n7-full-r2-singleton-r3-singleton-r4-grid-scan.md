# Experiment entry — 2026-04-05

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-singleton-r3-singleton-r4-grid-scan`

**Context:** verifier-oracle-model (`n=7`, `{2,3}` adaptive XOR-tree depth)

**Hypothesis tested:** With full `r=2` fixed, there exists some pair of **one** `r=3` and **one** `r=4` XOR split such that `min_d ≥ 3` (sparse triple+quartic menu does not universally collapse to depth 2).

**Outcome:** PASS

**Key finding:** Full `35×35` grid: **1190/1225** cells have `min_d=3`, **35/35** complementary exceptions have `min_d=2`. The depth-2 cases are **exactly** when the quartic subset is the set-theoretic complement of the triple (`|T|=3`, `|Q|=4`, `Q = [7]\setminus T`). Wall ~**1.7** s, LRU 4M.

**Implications:**

- The earlier “full `r=3` + any singleton `r=4` → `min_d=2`” phenomenon is **not** reproduced when the triple menu is collapsed to a **single** parity — complementarity between the chosen triple and quad is necessary for depth 2 in this slice.
- Suggests **redundancy among triple parities** was essential for the uniform `min_d=2` augmentation in the full-menu experiment.

**Analogy pass summary:** See `hypothesis.md` (learning / group testing / coding).

**Space definition:** none
