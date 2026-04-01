# Journal entry — 2026-04-01 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds678`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds678/`

**Context:** verifier-oracle-model (`n=14`, Hamming shells `{7,8}`, majority `t=8`)

**Hypothesis tested:** Independent random 400-split `r=9` XOR submenus (seeds 6, 7, 8) might hit a `d=3` feasible menu missed by seeds 0–2 and by contiguous shards.

**Outcome:** PASS (all subprocesses exit 0; **no** `d=3` witness — all three menus `feasible=False` with LRU saturated at 8M)

**Key finding:** Seeds `{6,7,8}` mirror the qualitative outcome of `{0,1,2}`: ~146–153 s DP each, **8,000,000** `exists_tree` cache misses after `d=3`, no positive. Together with shard scans, this reinforces that **small** random/coherent slices of the **2002**-split `r=9` menu are consistently negative at this budget — full-menu `r=9` `d=3` remains undecided.

**Implications**

- Optional further work: more seeds, different `k`, or return to **full-menu** `r=5`/`r=9` with larger envelopes if resources allow.
- Narrative: the **2002** band (`r∈{5,9}`) remains the hard pocket vs **3003** (`r∈{6,8}`) at `5e7`/8M, and random-submenu evidence now spans **six** seeds for `r=9`.

**Analogy pass summary:** Same as sibling `…-seeds012` — Monte Carlo coverage over index space for rare witnesses.

**Space-definition:** none
