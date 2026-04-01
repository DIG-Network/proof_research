# Journal entry — 2026-04-01 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds91011`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds91011/`

**Context:** verifier-oracle-model (`n=14`, Hamming shells `{7,8}`)

**Hypothesis tested:** Independent RNG seeds `{9,10,11}` might hit a 400-split `r=9` XOR submenu with `d=3 feasible=True` (H1); null H2 all `feasible=False`.

**Outcome:** PASS (H2 — all three seeds completed; no `d=3` witness)

**Key finding:** Same pattern as seeds `{0..8}`: each run `feasible=False`, LRU 8M saturated, `5.5×10⁷` budget sufficient. Total wall ~9 min.

**Implications:**

- Extends empirical negative evidence for small random `r=9` menus; still not a full-menu proof for 2002 splits.
- Full-menu PARTIAL at 5e7/8M for `r=5`/`r=9` remains the structural open item.

**Analogy pass summary:** Monte Carlo replication over index space — see `hypothesis.md`.

**Space definition:** none
