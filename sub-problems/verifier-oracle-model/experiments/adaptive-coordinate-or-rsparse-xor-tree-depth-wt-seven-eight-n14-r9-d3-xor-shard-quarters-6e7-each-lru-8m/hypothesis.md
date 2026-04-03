# Hypothesis: quarter-shard `r=9` XOR menu, `d=3`

## Analogy pass

1. **Abstract structure:** Same DP envelope as the completed `r=5` quarter-shard run: four contiguous XOR index blocks over `C(14,9)=2002` splits, **6×10⁷** `exists_tree` and **8M** LRU per quarter (**2.4×10⁸** aggregate). The `r=5` quarters all completed with **`d=3 feasible=False`** where half-shards at **12e7** were **PARTIAL**; `r=9` shares the same split count and half-shard pathology.

2. **Analogous domains:** (a) Symmetry / complement pairs in combinatorial search (`r` vs `n−r` menus differ in DP geometry despite equal menu size). (b) A/B replication in empirical science — mirror a decisive sub-menu experiment on the dual arity. (c) Load balancing — same shard geometry, different partition maps.

3. **Machinery:** Contiguous blocking + fixed memo cap; compare completion vs **PARTIAL** across arities.

4. **Transfer candidate:** Run the **identical** quarter partition **`[0:501), [501:1002), [1002:1503), [1503:2002)`** with **`--r-single 9`** to see whether `r=9` quarter menus also **finish** with definite **`d=3`** negatives (like `r=5`) or show asymmetric **PARTIAL** / witness behavior.

## Falsifiable claim

If `r=9` behaves like `r=5`, all four quarters finish without exit **2** and report **`d=3 feasible=False`**. If any quarter hits **PARTIAL** while `r=5` quarters did not (at the same per-quarter budget), the claim that the **2002-band** completion geometry is arity-symmetric at quarter scale is falsified.
