# Experiment entry

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-memo-dict-log-rss`  
**Context:** verifier-oracle-model  

## Hypothesis (short)

Intermediate **`5×10⁷`** **`exists_tree`** budget with **`--memo-dict`**, **`--log-rss`**, and **`--progress-every 2×10⁶`** to relate memo growth to resident RAM before retrying **10⁸** dict on large hosts.

## Outcome

**INCONCLUSIVE** — **exit 247** (**SIGKILL**/OOM) at **~3.8×10⁷** invocations (**~15 GB** **`VmRSS`**), before **`max_exists_calls`** or a **`PARTIAL:`** line.

## Key finding

**`memo_dict_size`** and **`VmRSS`** scale together (~**1 GB** per **~1M** new dict entries in this band). **5×10⁷** dict budget is **not** safe on **~15 GB** class runners.

## Implications

- Use **`--progress-every`** on long **`--memo-dict`** jobs to distinguish **stall** vs **OOM** vs **budget PARTIAL**.  
- Parent **`n=14`** script now supports **`--log-rss`** and **`--progress-every`**.  
- Next probes: **sharding**, **LRU-capped** lines, or **more RAM** — not raw **5×10⁷–10⁸** dict on this envelope.

## Analogy pass summary

See `hypothesis.md` in the experiment folder.
