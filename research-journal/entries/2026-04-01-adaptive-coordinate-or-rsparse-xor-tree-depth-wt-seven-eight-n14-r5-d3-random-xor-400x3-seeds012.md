# Experiment entry — 2026-04-01 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-random-xor-400x3-seeds012`

**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-random-xor-400x3-seeds012/`

**Context:** verifier-oracle-model (`n=14`, Hamming shells `{7,8}`, `r=5` XOR menu, depth-3 feasibility probe)

**Hypothesis tested:** Three fixed-seed uniform samples of **400** XOR split indices (non-contiguous in canonical order) might hit a submenu that already admits `d=3` feasibility, which would certify `min_d ≤ 3` for the full `r=5` language.

**Outcome:** PASS (all subprocesses completed; **no** `feasible=True` at `d=3`)

**Key finding:** Seeds 0, 1, and 2 each yielded `d=3 feasible=False` with LRU capped at 8M and `5.5×10⁷` `exists_tree` budget — same qualitative outcome as the contiguous 400-wide shard partition, suggesting **index contiguity was not** the reason the earlier scan missed a small-menu witness (for these random trials).

**Implications**

- Further **random** seeds or **larger** random submenus could be tried, but diminishing returns unless coupled with a new idea (e.g. targeted index families).
- Full-menu `r=5` `d=3` remains **open**; heaviest evidence remains partial runs on the full 2002 splits.

**Analogy pass summary:** Spread-spectrum / stratified sampling vs contiguous blocks — tested by random 400-submenus; no hit.

**Parent tooling:** `--xor-index-indices` on `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`.
