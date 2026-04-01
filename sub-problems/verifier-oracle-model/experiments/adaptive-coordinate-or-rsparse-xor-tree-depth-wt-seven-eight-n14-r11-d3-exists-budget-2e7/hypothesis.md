# Hypothesis

**Claim (tested):** At **`n=14`**, **`{7,8}`**, **`d=3`-only**, **`r=11`**, raising **`--max-exists-calls`** to **2×10⁷** would yield **`d=3 feasible=True`** (either by finishing a previously truncated **feasible** search, or by escaping **PARTIAL**).

**Result:** **Falsified.** The **2×10⁷** run **completes** **`d=3`** with **`feasible=False`** (**~8.29×10⁶** memoized **`exists_tree`** states). So **`r=11`** is **not** a **“need more budget for** **`d=3`** **”** case — **`d=3`** is **infeasible** for **coord+11xor** here (**`min_d≥4`**).

## Analogy pass

1. **Abstract structure:** Resource-bounded search — scaling a **counter** on **miss** calls may cross a **barrier** where a fixed point (feasibility verdict) becomes reachable.

2. **Analogous domains:** **FPT** kernel size vs **parameter**; **SAT** solver **conflict limits**; **numerical** **continuation** past a **bottleneck**.

3. **Machinery:** Empirical **scaling** of **work** vs **budget**; **order-of-magnitude** **steps**.

4. **Transfer seed:** **4×** **`exists_tree`** budget on the **same** **`r=11`** leg that **exactly** hit **5e6** in the prior shard.

## Parents

- `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r11-r12-r13-d3-exists-budget-5e6` (**`r=11`** **PARTIAL** at **5e6**; **`r=12,13`** easy).
