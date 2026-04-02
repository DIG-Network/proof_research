# Journal entry

**Date:** 2026-04-02  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-r9-d3-xor-step2-start1-1001-each-12e7-lru-8m`  
**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `r∈{5,9}`, `d=3` band)

## Hypothesis tested

The **complementary** 1001-wide XOR submenu (indices `1,3,…,2001` in canonical `C(14,r)` XOR order) might behave differently from the even-interleaved half (`0,2,…,2000`) under the same `12e7` / `8M` LRU envelope — possibly yielding a `d=3` witness or materially different PARTIAL dynamics.

## Outcome

**INCONCLUSIVE** — both `r=5` and `r=9` hit `max_exists_calls` PARTIAL (~976 s and ~860 s DP respectively); LRU saturated; no `d=3` witness. Slightly faster total wall time than the even-interleave sibling (~30.6 min vs ~31.4 min) but **same** completion status.

## Key finding

Coset choice between the two natural 1001-index parity halves does **not** unlock `d=3` at this budget; any speed difference is second-order vs the fundamental PARTIAL barrier.

## Implications

- Further progress on `r=5`/`r=9` `d=3` likely requires **more budget**, **larger LRU** (if memory allows), or a **different** structural change than XOR index coset.
- Parallel dual-10M LRU runs remain **discouraged** on memory-bounded agents (prior OOM).

## Analogy pass summary

Complementary survey strata / coset symmetry was the seed; empirically the DP’s PARTIAL behavior is **stable** across the two halves at `12e7/8M`.
