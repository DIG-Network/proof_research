# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-pair-r3-complementary-iff-min-d2`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-pair-r3-complementary-iff-min-d2`

**Context:** verifier-oracle-model (`n=6`, shell `{2,3}`, coord + full `r=2` + two `r=3` splits)

**Hypothesis tested:** `min_d=2` holds **if and only if** the two chosen triples are **disjoint** (complementary 3+3 partition of `[6]`).

**Outcome:** PASS

**Key finding:** Exhaustive check over all `190` unordered pairs reports **`violations=0`**. The witness set from experiment 140 is **exactly** the disjoint-pair predicate — no non-complementary pair achieves depth 2, and every complementary pair does.

**Implications:**

- Treat “complementary triple cut” as a **proven** (within this DP model) **characterization**, not only an observed subset of witnesses.
- Any future `n>6` analog should distinguish “empirical witness listing” from “predicate equivalence” and test the latter when feasible.

**Analogy pass summary:** Matroid / coding-style upgrade from “witnesses ⊆ X” to “witnesses = X”; verified by finite exhaustive consistency check.
