# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** Same **`r=5`**, **`d=3`-only** full **2002** XOR menu probe as the **300M/10M LRU** run, but with **plain `dict` memo** (`--memo-dict`) and a **smaller** invocation budget (**3×10⁷**) to measure wall time and termination mode without LRU eviction thrashing.

2. **Analogous domains:** (a) Working-set vs fixed-capacity cache (microbench showed **~2.5×** speedup at **8×10⁷**). (b) Session-state next action: compare **30M** dict path to prior **300M** LRU **PARTIAL**. (c) Same parent DP geometry; only memo policy and budget differ.

3. **Machinery:** Parent **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`**: **`--skip-baseline`**, **`--r-single 5`**, **`--d-min 3 --d-max 3`**, **`--max-exists-calls 30000000`**, **`--memo-dict`**. LRU cap argument is ignored for the DP when **`--memo-dict`** is set.

4. **Transfer seed:** If eviction was dominant, **3×10⁷** dict should finish in wall time well below the **~2460 s** class extrapolated for **300M** LRU at similar µs/call; outcome may still be **PARTIAL** if the search needs more invocations.

## Falsifiable claim

**H0:** Wall time is not dramatically lower than naive linear scaling from LRU **PARTIAL** runs at comparable effective work (hypothesis: dict helps only under eviction pressure — at **3×10⁷** we mainly learn **PASS/PARTIAL** and **`memo_dict_size`**).

**H1:** Run completes quickly (orders of magnitude below **300M** LRU wall) while still reporting **`memo_dict_size`** and a clear **PARTIAL** or **PASS** for **`d=3`**.

## Memory / lineage

- **Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-30e7-lru-10m` (INCONCLUSIVE **PARTIAL** at **3×10⁸** invocations, **10M** LRU).
- **Related:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-memo-dict-microbench-8e7` (**PASS**, dict vs LRU at **8×10⁷**).
