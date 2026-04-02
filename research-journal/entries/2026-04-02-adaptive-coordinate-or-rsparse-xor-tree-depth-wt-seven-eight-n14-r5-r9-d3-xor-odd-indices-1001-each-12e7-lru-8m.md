# Journal entry

**Date:** 2026-04-02  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-r9-d3-xor-odd-indices-1001-each-12e7-lru-8m`  
**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `r∈{5,9}`, `d=3` band)

## Hypothesis tested

A **non-contiguous** 1001-index XOR submenu (even indices `0,2,…,2000` in canonical order) might behave differently from contiguous half-shards under the same `12e7` / `8M` LRU envelope.

## Outcome

**INCONCLUSIVE** — both `r=5` and `r=9` hit `max_exists_calls` PARTIAL (~941 s DP each); LRU saturated; no `d=3` witness.

## Key finding

Interleaved 1001-cut does not beat contiguous halves on wall time at this budget; still PARTIAL for both parity-dual split counts (2002).

## Implications

- Structured non-contiguous sampling at **fixed** 1001 size is not a free lunch for closing `d=3` on this host.
- Complementary coset `1,3,…,2001` remains an obvious symmetric follow-up if more CPU time is available.

## Analogy pass summary

Stratified / interleaved indexing (statistics, QMC) was the seed; empirical result: no observed benefit vs contiguous half-shards at `12e7/8M`.
