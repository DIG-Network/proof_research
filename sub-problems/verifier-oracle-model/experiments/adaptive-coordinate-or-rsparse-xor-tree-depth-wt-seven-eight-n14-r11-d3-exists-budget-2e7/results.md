# Results

**Outcome:** FAIL (hypothesis falsified — **`exit 1`** from this folder’s **`script.py`**)

**Hypothesis tested:** **4×** **`exists_tree`** budget (**2×10⁷**) would let **`r=11`**, **`d=3`-only** finish with **`feasible=True`** (like **`r=7`** / **`r=12`**), vs **PARTIAL** at **5×10⁶**.

**What happened:** The **`d=3`** probe **completed** without **`_BudgetExceeded`** (**no** **exit 2**). **`exists_tree`** **LRU** **`currsize`** after **`d=3`:** **8 290 234** (well under **2×10⁷**). Line: **`d=3 feasible=False`**. So **`min_d > 3`** for **coord + 11-sparse XOR** on **`n=14`**, **`{7,8}`** — the **5×10⁶** **PARTIAL** at **`r=11`** was **truncated search**, **not** “almost there” on a **feasible** **`d=3`** instance.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r11-d3-exists-budget-2e7/script.py
```

**Timings (representative run):** **`build_sec≈0.88`**, **`dp_sec≈72`** for **`d=3`-only**.

**Comparison:** **`r=12`** (**91** splits) **certifies** **`d=3`** in **~10⁻² s**; **`r=11`** (**364** splits) needs **depth ≥ 4** (at least **`d=4`** in **`[d_min,d_max]`** range) — different **hardness** **mechanism** than **`r∈{5,6,8,9,10}`** where **`d=3`** may still be feasible but **budget**-blocked.
