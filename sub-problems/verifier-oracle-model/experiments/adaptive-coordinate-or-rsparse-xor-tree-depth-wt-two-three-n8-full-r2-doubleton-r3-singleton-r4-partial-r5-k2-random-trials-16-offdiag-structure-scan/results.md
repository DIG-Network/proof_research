# Results

**Outcome:** PASS

**Setup:** `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}`, base language `coord + full r=2 + doubleton r=3 + singleton r=4`, append **two** distinct splits from full `r=5` XOR menu (`len=56`). **`NUM_TRIALS=16`**, **`SEED=0`**, **`K_P5=2`**, **`LRU_CAP=4_000_000`**.

**Finding:** Every trial yields **`stratum_min_d2=7630`** (strictly between **`0`** and **`107800`**). **`stratum_pred=0`** on all trials; **`7630`** cells with **`d2∧¬pred`**; **`0`** false positives.

**Aggregate:** `proper_nonempty_proper=True`, `min_stratum_d2_across_trials=7630`, `max_stratum_d2_across_trials=7630`, `total_wall_sec≈3867.907` (~**`64.5`** min sequential).

**Contrast:** Partial **`r=5`** **`K=1`** exhaustive (**`56`** menus) gave uniform **`3850`**. Partial **`r=6`** **`K=2`** exhaustive (**`378`** menus) gave uniform **`107800`**. This random **`K=2`** **`r=5`** sample shows a **new intermediate plateau** (**`7630`**) — not **`3850`**, not saturated **`107800`**.

**Interpretation:** The hypothesis “some draw yields `0 < stratum_min_d2 < 107800`” is confirmed; in this sample the statistic is **constant** across draws at **`7630`**. Exhaustive **`C(56,2)=1540`** remains open to test universality.
