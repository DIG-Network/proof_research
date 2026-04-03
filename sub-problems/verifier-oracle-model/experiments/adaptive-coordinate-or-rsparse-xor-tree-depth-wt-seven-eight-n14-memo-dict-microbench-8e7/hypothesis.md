# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** `exists_tree` is a recursive decision procedure with a memo keyed by `(bitmask, depth)`. A fixed-size LRU evicts still-needed states under heavy fan-out, inflating work per invocation budget unit.

2. **Analogous domains:** (a) CPU cache thrashing vs fully associative backing store. (b) Graph search with duplicate detection via hash table vs bounded queue. (c) Dynamic programming where tabulation must not drop entries while subproblems remain active.

3. **Machinery:** Replace `functools.lru_cache` with an unbounded `dict` on the same key, preserving the same `--max-exists-calls` semantics (count every invocation, including memo hits).

4. **Transfer seed:** Expose `--memo-dict` on the parent `n=14` driver; microbench paired runs at **8×10⁷** invocations / **10M** LRU cap.

## Falsifiable claim

**H0:** Wall time for memo-dict is not substantially below capped LRU at the same invocation budget (speedup hypothesis false).

**H1:** Memo-dict completes the same budget in clearly less wall time (eviction was a dominant cost).

## Memory / lineage

- **Parent code:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`
- **Context:** Follow-up to **30e7/10M** **PARTIAL** on **`r=5`**, **`d=3`** (LRU saturation / marginal cost growth).
