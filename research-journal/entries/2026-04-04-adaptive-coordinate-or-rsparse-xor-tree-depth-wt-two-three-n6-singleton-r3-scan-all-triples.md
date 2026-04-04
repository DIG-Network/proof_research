# Experiment entry — 2026-04-04 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-singleton-r3-scan-all-triples

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-singleton-r3-scan-all-triples/`

**Context:** verifier-oracle-model (adaptive coordinate + XOR split-menu depth)

**Hypothesis:** At `n=6`, shell `{2,3}`, **every** singleton triple index `i ∈ {0..19}` with **full** `r=2` fixed still yields **`min_d=2`** (universal singleton sufficiency, paralleling `n=5`).

**Outcome:** **FAIL** (hypothesis falsified)

**Key finding:** **All** **20** singleton scans give **`min_d=3`** (`36` splits each: 15 pair + 1 triple). Full union `r=2,3` still gives **`min_d=2`** with **35** splits; pair-only stays at **`min_d=3`**. So **one** triple XOR is **not** enough at `n=6` to collapse depth from 3 to 2, unlike `n=5` where **any** single triple sufficed.

**Implications:**

- The “single critical triple generator” picture is **size-dependent**; `n=5` was **not** a universal template for `n=6`.
- Natural follow-up: minimal **`k`** triples + full `r=2` to reach `min_d=2`, or compare to **full** `r=3` menu size.

**Analogy pass summary:** Finite sensitivity of `min_d` over `C(n,3)`; threshold of generator count shifts with `n`.

**Space definition:** none
