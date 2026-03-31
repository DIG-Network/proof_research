# 2026-03-31 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n13

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n13`  
**Context:** verifier-oracle-model  
**Outcome:** INCONCLUSIVE

## Hypothesis tested

Extend the `(12,{6,7})` adaptive coord + r-sparse XOR depth scan to `n=13`, same majority semantics (`t=7`, shells `|S|∈{6,7}`, `|domain|=3432`).

## Key finding

- **Baseline:** coord-only `min_d=13`, coord + full 13-XOR `min_d=1` (~27 s).
- **Single-arity:** `r=2` completes with `min_d=7`, `dp_sec≈1356` (vs `min_d(2)=6` on n=12).
- **Full row `r=2..12`:** not completed in session; `r=3` onward expected much heavier (`286` triple splits vs `78` pairs).

## Implications

- Same structural story as n=12: global parity still collapses adjacent shells in one split; cheap coord-only still needs depth `n`.
- Scaling the **full** `min_d(r)` table to n=13 requires long **per-r** shards; use `python -u` for live per-depth logs.

## Analogy pass summary

See `hypothesis.md` in the experiment folder.
