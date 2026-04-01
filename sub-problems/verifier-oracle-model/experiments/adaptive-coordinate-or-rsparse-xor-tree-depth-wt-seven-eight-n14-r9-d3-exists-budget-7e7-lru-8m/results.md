# Results

**Outcome:** INCONCLUSIVE (parent exit **2** — PARTIAL: budget exhausted during `d=3` probe).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `--d-min 3 --d-max 3`, `--max-exists-calls 70000000`, `--lru-maxsize 8000000`, `--skip-baseline`.

**Measured:**
- `exists_tree` budget hit at **7×10⁷** invocations; LRU saturated at **8×10⁶** entries.
- Wall time for `d=3` probe segment: **~595.27 s** (~9.92 min); build **~4.17 s**.
- Parent printed `d=3 feasible=False` after PARTIAL (wrapper semantics; not certified completion).

**Comparison (dual 2002 band at 7e7/8M):** **`r=9`** **~595 s** vs **`r=5`** **~644 s** — **`r=9`** **faster** at the same invocation cap (consistent with prior runs where **`r=9`** was slightly cheaper than **`r=5`** at comparable budgets).
