# Hypothesis: n=14 r=5 d=3 — 10e7 budget, 12M LRU

## Analogy pass (mandatory)

1. **Abstract structure:** Decision-tree DP over 6435 masks with memoized `exists_tree`; LRU caps resident states; budget counts total `exists_tree` invocations before a verdict on `d=3` feasibility for coord + all 2002 five-sparse XOR splits.

2. **Analogous domains:** (a) PSPACE-style game search with transposition table vs full TT; (b) numerical PDEs — finer mesh (more cache) vs timestep limit; (c) branch-and-bound — larger frontier store may finish earlier or still hit node cap.

3. **Machinery there:** TT size trades memory for time; mesh refinement affects stability; branch-and-bound node limits yield PARTIAL certificates.

4. **Transfer seed:** Prior **10M** LRU at **10e7** was PARTIAL ~838 s for **r=5**; **12M** LRU previously OOM’d with **7.5e7** budget — **10e7** + **12M** tests whether the OOM was budget-linked or intrinsic to 12M on this host.

## Falsifiable claim

Either **d=3** is certified **feasible** or **infeasible** within **10⁸** `exists_tree` calls with **12×10⁶** LRU, or we record **PARTIAL** / host **OOM** class.

## Parent

`../adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`
