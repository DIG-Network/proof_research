# Results

**Outcome:** PASS

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --d-min 3 --d-max 3 --lru-maxsize 0 --max-exists-calls 5000000`, legs **`r=8`**, then **`r=9`**, then **`r=10`**.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r8-r9-r10-d3-exists-budget-5e6/script.py
```

**Observed**

All three legs returned exit **2** (**PARTIAL**): **`exists_tree`** budget **5×10⁶** exhausted, **`min_d=None`** in the summary line, LRU **≈5×10⁶** states.

| Leg | XOR splits | build_sec (approx) | dp_sec (approx) | exit |
|-----|------------|--------------------|-----------------|------|
| r=8 | 3003       | ~5.65              | ~34.45          | 2    |
| r=9 | 2002       | ~4.08              | ~31.32          | 2    |
| r=10| 1001       | ~2.21              | ~31.62          | 2    |

**Conclusion:** Under the **same** bounded-memo **`d=3`** probe as **`r=5,6`**, values **`r∈{8,9,10}`** sit in the **heavy partial** class. The **easy **`r=7`** window** does **not** extend to **`r=8`** at this budget; **`r=9,10`** behave consistently with **budget saturation** rather than quick certification.

**Comparison (5×10⁶ budget, d=3-only)**

| r   | Outcome class (this / prior shards)      |
|-----|------------------------------------------|
| 5,6 | PARTIAL (exit 2)                       |
| 7   | **PASS** — `d=3 feasible=True` ~0.4 s |
| 8–10| PARTIAL (exit 2) — this experiment     |
