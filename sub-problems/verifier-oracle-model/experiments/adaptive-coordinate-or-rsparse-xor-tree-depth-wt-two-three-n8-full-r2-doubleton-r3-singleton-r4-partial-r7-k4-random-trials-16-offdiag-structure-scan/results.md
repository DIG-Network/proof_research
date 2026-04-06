# Results

**Outcome:** FAIL (hypothesis falsified for this bounded random probe)

**Pre-registered success criterion (script exit 0):** Among **`NUM_TRIALS=16`** independent draws with **`SEED=0`**, each sampling **`K_P7=4`** distinct splits from the full **`r=7`** XOR menu (**`C(8,7)=8`**), at least one draw yields **`0 < stratum_min_d2 < 107800`** on the off-diagonal **`s∈{0,1,2}`** stratum (**`107800`** cells).

**Observed:** **Every** trial returned **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`viol_d2_not_pred=107800`**, **`viol_pred_not_d2=0`**.

**Wall clock:** **`total_wall_sec≈274.4`** for all 16 passes (**`LRU_CAP=4_000_000`**).

**Interpretation:** On this fixed **`{2,3,4}`** shell grid, **half** of the **`r=7`** splits (**4 of 8**) is already enough—at least for these 16 random 4-subsets—to force **`min_d=2`** on **all** stratum cells, matching the **full** **`r=7`** saturation. There is **no** random-sample evidence of a **partial** `r=7` submenu sitting in a **proper intermediate** `stratum_min_d2` window; the “cliff” seen for **full** high-arity menus appears **robust** to **sparse** `r=7` sampling at **`K=4`**.

**Caveat:** Only **16** trials at one **`(SEED, K)`**; exhaustive **`C(8,4)=70`** submenu enumeration or other **`K`** values remain open.
