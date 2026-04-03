# Experiment entry

**Date:** 2026-04-03  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-3e7-memo-dict`

**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `r=5`, full **2002** XOR menu, `d=3`-only)

**Hypothesis tested:** With **`--memo-dict`**, a **3×10⁷** **`exists_tree`** budget gives a fast wall-clock datapoint comparable in spirit to the prior **300M/10M LRU** **PARTIAL** (session next action: thirty million, not Python **`30e7`**).

**Outcome:** INCONCLUSIVE (exit **2**, **PARTIAL** after **30M** calls, **~112.5 s** DP).

**Key finding:** **`memo_dict_size` 12_256_532** at cutoff — dict memo avoids LRU thrashing; **~120 s** end-to-end vs **~2600 s** class for **300M** LRU at **10M** cap. Still **no** complete **`d=3`** verdict at this budget.

**Implications:**

- Scale **`--max-exists-calls`** under **`--memo-dict`** when RAM allows; expect much lower wall per invocation than capped LRU at the same budget tier.
- **`memo_dict_size` < `max_exists_calls`** is normal (budget counts every call, including hits).

**Analogy pass summary:** Same as sibling microbench / **30e7 LRU** line — memo policy dominates wall time; search depth still budget-limited.
