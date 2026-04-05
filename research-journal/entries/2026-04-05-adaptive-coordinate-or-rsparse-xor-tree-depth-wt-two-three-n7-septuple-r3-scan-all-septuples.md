# Journal entry — 2026-04-05 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-septuple-r3-scan-all-septuples`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-septuple-r3-scan-all-septuples`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`), exhaustive closure after `C(35,6)` sextuples (all `min_d=3`) and a non-proof random `400/6724520` septuple sample (`witness_min_d2_count=0`).

**Hypothesis tested:** **Some** unordered septuple of `r=3` XOR indices yields `min_d=2` with **coord + full `r=2`**.

**Outcome:** **FAIL** — `septs_checked=6724520`, `witness_min_d2_count=0`, `wall_sec≈14123` (~3.92 h), `lru_cap=4_000_000`.

**Key finding:** **Every** septuple in the `C(35,7)` universe keeps `min_d=3`; there is **no** depth-2 certificate from **seven** sparse triple parities plus the full pair-XOR menu in this DP model.

**Implications:**

- The **`r=3`-only ladder** is **combinatorially closed** through **k=7** at this slice; further progress on `min_d=2` requires **non-ladder** augmentations (e.g. **`r=4`** / full union menus already known to suffice elsewhere in the digest).
- Random **`400`**-draw **FAIL** is **consistent** with the exhaustive negative.

**Analogy pass summary:** See `hypothesis.md` — finite combinatorial closure after nested `C(35,k)` envelopes.
