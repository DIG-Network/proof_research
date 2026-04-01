# Experiment entry — 2026-04-01 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds012`

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds012/`

**Context:** verifier-oracle-model (`n=14`, Hamming shells `{7,8}`, `r=9` XOR menu, depth-3 feasibility probe)

**Hypothesis tested:** Same random-submenu design as `r=5`: three fixed seeds sampling 400 XOR indices from `C(14,9)=2002` might hit a submenu with `d=3` feasibility.

**Outcome:** PASS (all subprocesses completed; **no** `feasible=True` at `d=3`)

**Key finding:** Seeds 0–2 each gave `d=3 feasible=False` with LRU at 8M and `5.5×10⁷` budget — aligned with **`r=5`** random 400×3 and with **`r=9`** contiguous shard scan (all negative small-menu evidence; not a full-menu impossibility proof).

**Implications**

- Non-contiguous random 400-menus do not appear to rescue `r=9` `d=3` witness search versus contiguous shards for these seeds.
- Full-menu `r=9` `d=3` remains **open**.

**Analogy pass summary:** Stratified / spread indices vs contiguous blocks — mirrored from `r=5` probe.

**Parent tooling:** `--xor-index-indices` on `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`.
