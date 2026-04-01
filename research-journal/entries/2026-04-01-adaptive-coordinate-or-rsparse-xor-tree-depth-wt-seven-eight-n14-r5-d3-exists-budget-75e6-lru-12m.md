# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-75e6-lru-12m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-75e6-lru-12m/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `coord + r=5`, `d=3`-only with **7.5×10⁷** `exists_tree` budget and **12×10⁶** LRU (intermediate bracket between 5e7/8M PARTIAL and 1e8/16M long run).

## Hypothesis tested

See `hypothesis.md`: intermediate (budget, LRU) should yield a clean PARTIAL or feasibility line within ~1 h on this host class.

## Outcome

**INCONCLUSIVE** — process **SIGKILL** (**exit 247** / child **-9**) after **~470–490 s**; no `feasible=` or `PARTIAL:` line.

## Key finding

**12M LRU** with **7.5e7** budget **OOM-kills** this worker **early**; the **(7.5e7, 12M)** bracket **does not** produce a **PARTIAL** transcript here. **5e7/8M** remains the only **completed** capped **`r=5` `d=3`** datapoint on constrained RAM.

## Implications

- Do **not** assume **12M** LRU is safe on **~15 GiB** class hosts for this shard.
- Next honest steps: **`lru-maxsize 0`** + large RAM + explicit timeout, or **smaller** LRU if testing **7.5e7** budget in isolation.

## Analogy pass summary

Interpolation between two resource caps in transposition-table search; host killed before table could fill.

## Space-definition

None.
