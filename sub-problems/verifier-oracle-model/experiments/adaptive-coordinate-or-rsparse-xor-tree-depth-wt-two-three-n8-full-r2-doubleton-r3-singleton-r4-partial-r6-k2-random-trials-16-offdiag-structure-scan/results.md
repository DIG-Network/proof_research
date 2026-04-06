# Results

**Outcome:** FAIL (pre-registered hypothesis falsified on this random sample)

**Setup:** `n=8`, base language `coord + full r=2 + doubleton r=3 + singleton r=4`, then append **two** distinct XOR splits sampled uniformly without replacement from the full **`r=6`** menu (`C(8,6)=28`). Off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}` (`107800` cells). **`NUM_TRIALS=16`**, **`SEED=0`**, **`K_P6=2`**, **`LRU_CAP=4_000_000`**.

**Finding:** Every trial had **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** cells with **`d2∧¬pred`**, **`0`** false positives. **`total_wall_sec≈986.6`**; per-trial walls **`40.9s`**–**`88.6s`**.

**Interpretation:** In this probe, **two** random **`r=6`** splits behave like **one** (**`K=1` exhaustive`**) and like full **`r=6`**: universal saturation of **`min_d=2`** witnesses on the stratum. This does **not** rule out an intermediate value for some **specific** pair in **`C(28,2)=378`**; exhaustive enumeration remains open (~**`11h`** sequential at observed per-menu cost).

**Command:**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r6-k2-random-trials-16-offdiag-structure-scan/script.py
```
