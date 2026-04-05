# Results — off-diagonal `|∩|∈{0,1}` symdiff biconditional (`n=7`)

**Outcome:** **FAIL**

**Setup:** Same **`22050`** grid as structure scan: **coord + full `r=2` + doubleton `r=3` (`i<j`) + singleton `r=4`**, **`LRU_CAP=4_000_000`**.

**Hypothesis (stratum):** For **`i<j`** with **`s = |T_i∩T_j| ∈ {0,1}`**, **`min_d = 2` ⇔ `Q = T_i ⊕ T_j`**.

**Measured (exhaustive):**

- **`wall_sec ≈ 31.8`** (representative run)
- **Stratum size:** **`13475`** cells (**`s=0`:** **`2450`**, **`s=1`:** **`11025`**)
- **Within stratum:** **`min_d=2`:** **`770`**; predicate hits **`Q=symdiff`:** **`315`**
- **Violations (disjoint types):**
  - **`d2_s0=140`:** **`min_d=2`** with **`s=0`** ( **`symdiff`** is a **6-set**, so equality to **`Q`** is impossible — biconditional fails immediately)
  - **`d2_not_symdiff=630`:** **`s=1`**, **`min_d=2`**, but **`Q ≠ symdiff`**
  - **`symdiff_not_d2=315`:** **`s=1`**, **`Q=symdiff`**, but **`min_d=3`** (matches the **false-positive** pattern from **`…-offdiag-symmetric-diff-predicate`** on the **`s=1`** slice)

**Conclusion:** The **patchwork** suggestion “**`Q = T_i△T_j`** on **`s∈{0,1}`**” is **not** a **`min_d=2`** **biconditional** even **after** dropping the **`s=2`** branch. **`|∩|=0`** **disjoint** triples still admit **many** **`min_d=2`** **certificates** with **`Q`** **not** equal to **6-bit** **symdiff**, and **`|∩|=1`** **shows** **both** **direction** **failures**.
