# Journal entry

**Date:** 2026-04-02  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-12e7-each-lru-10m-parallel`  
**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `coord + r=9` XOR, `d=3`)

## Hypothesis tested

Running the two **1.2×10⁸** / **10M** LRU XOR half-shards **in parallel** would cut wall-clock roughly in half vs the sequential wrapper while preserving verdict class (expected both PARTIAL).

## Outcome

**INCONCLUSIVE** (resource / scheduling). Shard **0** subprocess **SIGKILL** (**-9**) ~**4849 s**; shard **1** **PARTIAL** at cap after **~5838 s** DP (**~5.9×** sequential half time). Total wall **~5890 s** — worse than sequential **~2121 s**. Wrapper initially exited **1**; post-hoc **script.py** maps **-9** → exit **2** (INCONCLUSIVE).

## Key finding

Two concurrent **10M** LRU DP workers on this host are **unsafe**: OOM-style kill on one branch and **heavy contention** on the other. Parallelism **does not** substitute for sequential half-shards here.

## Implications

- Do **not** rely on in-process parallel **10M×2** for this probe on memory-bounded agents.
- Prefer **sequential** halves, **single** larger budget, or **separate** machines with isolated memory.

## Analogy pass summary

Embarrassingly parallel partition — **failed** once shared RAM / CPU becomes the bottleneck (Amdahl + memory bandwidth).

## Space definition

N/A
