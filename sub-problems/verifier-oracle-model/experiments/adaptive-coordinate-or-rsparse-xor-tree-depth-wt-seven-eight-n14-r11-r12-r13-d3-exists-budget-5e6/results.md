# Results

**Outcome:** PASS (on **revised** acceptance: **`r=11`** **PARTIAL**, **`r=12,r=13`** **quick** **`d=3`**)

**Original hypothesis** (all three **PARTIAL** like **`r=8..10`**) was **falsified** on first run; script and journal record the **observed** classification.

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --d-min 3 --d-max 3 --lru-maxsize 0 --max-exists-calls 5000000`, legs **`r=11`**, **`r=12`**, **`r=13`**.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r11-r12-r13-d3-exists-budget-5e6/script.py
```

**Observed (authoritative run)**

| Leg | XOR splits | build_sec | dp_sec   | Parent exit | Notes                                      |
|-----|------------|-----------|----------|-------------|--------------------------------------------|
| r=11| 364        | ~0.89     | ~35–44   | 2           | **PARTIAL** — LRU **≈5×10⁶**, budget hit   |
| r=12| 91         | ~0.24     | ~0.008   | 0           | **`d=3 feasible=True`**, **`min_d=3`**     |
| r=13| 14         | ~0.04     | ~0.003   | 0           | **`d=3 feasible=True`**, **`min_d=3`**      |

**Conclusion:** At **`n=14`**, **`{7,8}`**, **`5×10⁶`** **`exists_tree`** budget, **`d=3`-only**, there is a **second “easy” band** at **`r∈{12,13}`** (few XOR splits), while **`r=11`** stays in the **heavy PARTIAL** class with **`r∈{5,6,8,9,10}`**. **`r=7`** is **not** unique: **high** **`r`** can certify **`d=3`** in **milliseconds** once the split family is small enough, but **`r=11`** sits **between** the **`r=7`** window and that regime.

**Comparison (5×10⁶ budget, d=3-only, n=14 {7,8})**

| r   | Outcome class (this / prior shards)        |
|-----|----------------------------------------------|
| 5,6,8–11 | PARTIAL (exit 2) at **5e6**            |
| 7   | **PASS** — quick **`feasible=True`**         |
| 12,13 | **PASS** — quick **`feasible=True`** (**this** exp.) |
