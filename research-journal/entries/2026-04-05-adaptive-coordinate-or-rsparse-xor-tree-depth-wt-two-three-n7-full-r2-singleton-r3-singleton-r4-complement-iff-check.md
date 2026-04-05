# Experiment entry — 2026-04-05

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-singleton-r3-singleton-r4-complement-iff-check`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`, adaptive coordinate + XOR-tree DP)

**Hypothesis tested:** On the full `35×35` grid (coord + full `r=2` + one `r=3` + one `r=4`), `min_d = 2` if and only if the chosen quadruple is the set complement of the chosen triple in `[7]`.

**Outcome:** PASS

**Key finding:** All 1225 cells checked; zero violations of the iff; exactly 35 complementary pairs and 35 depth-2 cells. Wall time ~1.65 s with `4M` LRU. This machine-checks the structural claim recorded narratively after `…-n7-full-r2-singleton-r3-singleton-r4-grid-scan`.

**Implications:**

- The sparse `single triple + single quad` certificate for depth 2 is **exactly** the global `3+4` partition — not merely typical or dominant.
- Further work on “minimal menus” at `n=7` can treat complementarity as the **complete** classification for this language shape.

**Analogy pass summary:** Formal verification / finite combinatorics — replay and independently certify an invariant on a product enumeration.

**Space-definition:** none
