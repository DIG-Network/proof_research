# Journal entry

**Date:** 2026-04-02  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-24e7-lru-10m`  
**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `r=5`, `d=3` band)

## Hypothesis tested

Mirror **`r=9` `24e7/10M`** for the complementary **`r=5`** shell (**`C(14,5)=C(14,9)`**) on the full **2002** XOR menu to see whether **`+6×10⁷`** **`exists_tree`** beyond **18e7** completes **`d=3`** or remains **PARTIAL**.

## Outcome

**INCONCLUSIVE** — **PARTIAL** at **240000000** **`exists_tree`** calls; **~1970.27 s** DP (**~32.8 min** wall **~2009 s** including startup); LRU **10M** saturated; **no** certified full-menu **`d=3`** verdict.

## Key finding

**Dual 2002** lanes both **unfinished** at **24e7/10M**. **`r=5`** **~148 s** (**~7%**) faster than **`r=9`** at this cap (**narrower** than **~9%** at **18e7**). Marginal **18e7→24e7** cost **~478 s** (**r=5**) vs **~474 s** (**r=9**) — **~8 µs**/extra call **both** at **LRU** cap.

## Implications

- **Budget ladder** alone has **not** closed **`d=3`** for **full** **2002** menu at **10M** LRU through **2.4×10⁸** for **either** shell.
- Next pressure points: **>24e7**, **>10M** LRU (**OOM** risk), or **DP/memo** / **structural** attack on the **`exists_tree`** frontier.

## Analogy pass summary

Paired **complement-shell** probe; same **bounded-work-unit** extension as **`r=9` 24e7**; confirms **near-identical** marginal **`exists_tree`** cost across **`r=5`/`r=9`** at **10M** LRU in the **18e7→24e7** step.
