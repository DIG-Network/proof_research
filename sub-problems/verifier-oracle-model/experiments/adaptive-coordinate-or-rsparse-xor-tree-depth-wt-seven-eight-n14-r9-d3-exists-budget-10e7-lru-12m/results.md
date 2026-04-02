# Results: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-10e7-lru-12m

**Outcome:** INCONCLUSIVE

**Configuration:** `n=14`, shells `{7,8}`, coord + full **r=9** XOR menu (2002 partitions), **d=3** only, `--max-exists-calls 100000000`, `--lru-maxsize 12000000`, `--skip-baseline`.

**Run:** Process exit **247** after **~472.6 s** wall (~7.88 min). No `feasible=` line and no `PARTIAL:` line printed.

**Interpretation:** **12M** LRU **OOM** class is **not** **r-specific** at this scale — **r=9** mirrors **r=5** kill pattern (cf. **r=5** **10e7/12M** sibling run same session).

**Comparison:** **10e7/10M** **r=9** reached **PARTIAL** ~957 s; **10e7/12M** **r=9** dies earlier on this host.
