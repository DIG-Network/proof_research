# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** **`r=5`** **`d=3`** at **10⁸** **`exists_tree`** with **8M** LRU remained **PARTIAL** (~917 s DP). Digest records **12M** LRU + **7.5e7** **OOM** on this host — we test **10M** LRU (**+25%** over **8M**) at the **same** **10⁸** budget to see if a modest cache enlargement changes termination vs thrashing without crossing prior OOM envelope.

2. **Analogous domains:** (a) Working-set expansion under fixed step budget. (b) Cache associativity vs miss rate plateaus. (c) Continuation parameter between stable (8M) and known-failed (12M) regimes.

3. **Machinery:** Same parent DP, **`--r-single 5`**, **`--d-min 3 --d-max 3`**, **`100000000`** max exists calls, **`10000000`** LRU.

4. **Transfer seed:** If **10M** still **PARTIAL** with similar DP time to **8M**, LRU is not the dominant lever at **10e7**; if **OOM**/SIGKILL, **10M** is near host limit; if **exit 0** with definite **`d=3`**, larger working set unlocked completion.

## Falsifiable claim

**H0:** Under **`--max-exists-calls 100000000`**, **`--lru-maxsize 10000000`**, **`r=5`**, **`d=3`-only**, the parent exits **2** (PARTIAL) or dies by **OOM** (non-2/0).

**H1:** Exit **0** with definite **`d=3 feasible=`** without budget exhaustion mid-probe.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-10e7-lru-8m` (INCONCLUSIVE PARTIAL ~917 s), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-75e6-lru-12m` (OOM class at 12M).
