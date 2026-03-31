# Results: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n13

**Outcome:** **PASS** (baseline phase) — **H1** **confirmed** **2026-03-31** **on** **this** **host** **(** **`--baseline-only`** **)** **.**

**Setup:** `n=13`, masks with **wt ∈ {7,8}** (**3003** **masks**). Majority **t=8**.

**Coord-only:** `min_d = 13` (`d_max=13` scan; **d=12** **infeasible** **~10** **s**, **d=13** **feasible** **~6.3** **s** **on** **this** **run** **).

**Coord + full 13-XOR:** `min_d = 1` (**~0.001** **s** **).

**Not** **run** **this** **session** **:** **full** **`r=2..12`** **`min_d(r)`** **table** **or** **unions** **—** **next** **:** **shard** **per** **`--r-single`** **r** **(** **expect** **heavy** **`r`** **near** **`C(13,r)`** **max** **,** **as** **on** **`n=12`** **)** **.**

**Repro:** `python3 script.py --baseline-only`
