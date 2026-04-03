# 2026-04-03 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-eighths-3e7-each-lru-8m

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-eighths-3e7-each-lru-8m`

**Context:** verifier-oracle-model (`n=14`, shells `{7,8}`, **`r=5`**, **`d=3`**, **2002** XOR splits)

**Hypothesis tested:** Eight contiguous eighth-shards (**~251** splits each, last **245**) with **3×10⁷** `exists_tree` and **8M** LRU per eighth (**2.4×10⁸** total, matching four **6×10⁷** quarters) tests whether **finer** blocking at the **same aggregate budget** changes **PARTIAL** vs complete **`d=3`** outcomes relative to **quarters**.

**Outcome:** **PASS** (clean completion). **All eight** eighths finished **without** budget **PARTIAL**; **all** **`d=3 feasible=False`**. **~183 s** (~**3.05 min**) sequential. **LRU** **not** saturated (max **~2.84×10⁶** misses vs **8M** cap).

**Key finding:** **Eighth** geometry is **much cheaper** wall-clock than **quarters** at **matched** **2.4×10⁸** total cap because **~250-split** menus fit the **8M** memo footprint; **quarter** **PARTIAL** at **6e7** was tied to **~500-split** **working-set** pressure, not only global invocation totals. **Negatives** **align** with **quarters** (**no** **`d=3`** witness).

**Implications:**

- **Sharding resolution:** **Sub-500** split contiguous blocks are **decisive** at **3e7/8M** without **LRU** cap hits for **`r=5`** here.
- **Full-menu `d=3`** still **open**; optional follow-up: **6e7** on eighths to stress **LRU** like quarters.

**Analogy pass summary:** Finer segmentation trades **per-segment** work vs **global** budget; here it **reduces** memo pressure **enough** to **finish fast** while preserving **`d=3`** **`False`**.

**Space-definition:** none
