# Hypothesis: eighth-shard `r=5` XOR menu, `d=3`

## Analogy pass

1. **Abstract structure:** Finer contiguous blocking of the same split menu under a fixed aggregate `exists_tree` budget may change whether LRU saturation yields PARTIAL vs a complete `feasible` bit at `d=3`.

2. **Analogous domains:** (a) Mesh refinement in numerical analysis — smaller elements, more boundary work. (b) Finer bucketization in external-memory algorithms — more passes, different IO profile. (c) Sub-block coding — shorter segments can change which errors are correctable first under a bit budget.

3. **Machinery:** Trade number of segments vs work per segment; locality vs capacity.

4. **Transfer candidate:** Partition **2002** XOR indices into **eight** contiguous blocks (~251 splits each, last **245**) with **3×10⁷** `exists_tree` and **8M** LRU **per** eighth — **8 × 3×10⁷ = 2.4×10⁸** total, **same** aggregate cap as **four** **6×10⁷** quarters — and compare completion / `d=3 feasible` to quarter geometry.

## Falsifiable claim

All eight eighths finish without exit **2** (no PARTIAL at this budget) **or** some eighth exhibits PARTIAL / a `feasible=True` witness. If outcomes match quarters (all complete, all `False`), eighthing does not change the `d=3` negative pattern for `r=5` at this envelope; if PARTIAL appears where quarters completed, finer blocking hurts completion at fixed per-shard budget.
