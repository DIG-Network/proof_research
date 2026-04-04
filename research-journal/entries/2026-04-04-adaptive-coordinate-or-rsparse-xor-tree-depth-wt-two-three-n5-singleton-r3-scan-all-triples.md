# Experiment entry — 2026-04-04 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-singleton-r3-scan-all-triples

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-singleton-r3-scan-all-triples/`

**Context:** verifier-oracle-model (adaptive coordinate + XOR split-menu depth)

**Hypothesis:** With `n=5`, shell `{2,3}`, and **full** `r=2` fixed, **only** triple-XOR index **`0`** (`(0,1,2)`) yields **`min_d=2`** among **singleton** `r=3` augments (witness set **`{0}`**).

**Outcome:** **FAIL** (hypothesis falsified)

**Key finding:** **All** **`10`** singleton triple indices give **`min_d=2`** (**`11`** splits each). The prior experiment’s first `k=1` witness (`index 0`) was a **lexicographic search artifact**, not combinatorial uniqueness. **Any** triple parity + full pair menu suffices at `n=5` for this certificate.

**Implications:**

- Strengthens the “one triple generator is enough **vs** pair-only” picture: the phenomenon is **highly redundant** across triples here.
- Suggests follow-up at **`n≥6`**: singleton universality may fail once triple structure interacts differently with the mask shell.

**Analogy pass summary:** Critical-generator enumeration; witness from greedy/lex search need not be unique.

**Space definition:** none
