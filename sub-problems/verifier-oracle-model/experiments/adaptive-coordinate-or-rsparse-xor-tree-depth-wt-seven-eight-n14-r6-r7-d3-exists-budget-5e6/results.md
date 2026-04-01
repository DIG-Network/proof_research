# Results

**Outcome:** PASS

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --d-min 3 --d-max 3 --lru-maxsize 0 --max-exists-calls 5000000`, legs `r=6` then `r=7`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-r7-d3-exists-budget-5e6/script.py
```

**Observed**

- **`r=6`:** exit **2** (PARTIAL). Same pattern as **`r=5`**: ~5×10⁶ `exists_tree` invocations in ~**35 s** (host variance **35–38 s**), `d=3 feasible=False` in the partial log, LRU ~5×10⁶ states.
- **`r=7`:** exit **0** (PASS). **`d=3 feasible=True`** in **~0.41 s** DP after **~5.9 s** split build (**3432** partitions). Completed **well inside** the 5×10⁶ budget.

**Conclusion:** Under identical bounded-memo conditions, **`d=3` decidability is not monotone in `r`**: **`r∈{5,6}`** stays in the **heavy partial** class while **`r=7`** certifies **`min_d≤3`** immediately. This sharpens the open **`r=5`/`r=6`** **`d=3`** region: hardness is **not** explained by “more XOR splits ⇒ always harder.”

**Metrics**

| Leg | XOR splits | build_sec (approx) | dp_sec (approx) | exit |
|-----|------------|--------------------|-----------------|------|
| r=6 | 3003       | ~4.6               | ~35.2 (partial) | 2    |
| r=7 | 3432       | ~5.9               | ~0.41           | 0    |
