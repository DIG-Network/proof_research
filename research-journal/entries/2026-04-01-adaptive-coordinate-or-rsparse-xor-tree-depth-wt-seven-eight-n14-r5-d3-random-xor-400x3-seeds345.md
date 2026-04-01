# Experiment entry — 2026-04-01 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-random-xor-400x3-seeds345`

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-random-xor-400x3-seeds345/`

**Context:** verifier-oracle-model (`n=14`, Hamming shells `{7,8}`, `r=5` XOR menu, depth-3 feasibility probe)

**Hypothesis tested:** Independent PRNG seeds **3,4,5** sampling 400 XOR indices from `C(14,5)=2002` might hit a submenu with `d=3` feasibility (extends `…-seeds012`).

**Outcome:** PASS (all subprocesses completed; **no** `feasible=True` at `d=3`)

**Key finding:** Each seed gave `d=3 feasible=False` with LRU **8M** full and **`5.5×10⁷`** budget — **six** random 400-menus (seeds 0–5) now uniformly negative; aligns with contiguous shard scans; **full** 2002-split `min_d` still not certified.

**Implications**

- Strengthens empirical case that **small** random `r=5` XOR submenus are unlikely to reveal a depth-3 certificate without searching the full menu or changing budgets / structure.
- Does not resolve full-menu `r=5` / `r=9` `d=3` open threads.

**Analogy pass summary:** Same stratified-menu / spread-sampling framing as `…-seeds012`.

**Parent / sibling:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`; extends `…-r5-d3-random-xor-400x3-seeds012`.
