# 2026-04-02 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-memo-dict-microbench-8e7

**Context:** `verifier-oracle-model` — `n=14`, `{7,8}`, `r=5`, `d=3`-only DP on the full 2002-split XOR menu; prior **30e7/10M LRU** run hit **PARTIAL** ~2616 s with steep marginal cost vs **24e7**.

**Hypothesis tested:** Replacing **`functools.lru_cache`** with a **plain `dict`** memo (**`--memo-dict`** on the parent driver), keeping the same **`--max-exists-calls`** semantics (count every invocation), materially reduces wall time at a fixed invocation budget when the LRU cap causes eviction thrashing.

**Outcome:** PASS

**Key finding:** At **8×10⁷** invocations and **10M** LRU cap, paired runs in one process: **LRU ~65.5 s** vs **memo-dict ~26.1 s** (**~2.5×**). **`memo_dict_size`** **3214257** at cutoff vs LRU essentially saturated — dict path does more useful work per invocation under the same budget counter.

**Implications:**

- Next full-menu **`r=5`/`r=9`**, **`d=3`** probes should default to **`--memo-dict`** where RAM allows, before pushing **30e7+** budgets on capped LRU.
- Parent script updated: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`.

**Analogy pass:** See experiment `hypothesis.md`.

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-memo-dict-microbench-8e7/`
