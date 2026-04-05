# Hypothesis — off-diagonal `|∩|=2`: wedge OR complement(symdiff) only (`n=7`)

## Abstract structure

Same **`22050`** grid as prior doubleton-`r=3` + singleton-`r=4` scans: **coord + full `r=2` + two triple-XOR splits `(i≤j)` + one quartic-XOR split `Q`**. Off-diagonal **`min_d=2`** witnesses (**`1190`** total) are not classified by the **patchwork** template (**`…-offdiag-patchwork-inter012-template`**, FAIL). Notes highlighted a competing **`|∩|=2`** pattern: **`Q = [7] \ (T_i △ T_j)`** (complement of symmetric difference) versus the **ordered wedge** **`W = (T_i \ T_j) ∪ ([7] \ (T_i ∪ T_j))`**.

**Claim under test (restricted):** Among off-diagonal cells with **`s = |T_i ∩ T_j| = 2`** and **`min_d = 2`**, every witness satisfies **`Q_mask ∈ {W, FULL_MASK ^ (T_i ⊕ T_j)}`** (both interpreted as 7-bit masks; **`Q`** is always a 4-set in this grid, so **`popc(Q_mask)=4`** is automatic).

**Converse (same stratum):** If **`i<j`**, **`s=2`**, and **`Q`** equals **`W`** or **`FULL_MASK ^ symdiff(T_i,T_j)`**, then **`min_d=2`** (biconditional within this stratum only).

## Analogy pass

1. **Abstract structure:** A **binary classification** problem on a finite fiber (**quartics over fixed triple pair**) where **two competing generative laws** (here: **two different 4-sets** built from **`T_i,T_j`**) may both appear in the **positive class**; the question is whether the positive class is **exactly their union** in a fixed **overlap stratum**.

2. **Where else:** (i) **Mixture models with two component supports** — the **support** of the observation law may be **union of two manifolds**. (ii) **Algebraic curves with multiple branches** — **one stratum**, **two charts** that **glue** on a **lower-dimensional overlap**. (iii) **Error syndromes in coding** — **two distinct error patterns** can yield the **same decoder depth** metric.

3. **Machinery:** **Union of charts** / **piecewise definitions**; **explicit enumeration** to test **set equality** of **finite fibers**.

4. **Transfer candidate:** Treat **`|∩|=2`** as isolating a **two-chart** geometry: **wedge** vs **complement(symdiff)** — the smallest **symmetric** enlargement of the failed **single-chart** patchwork.

## Memory / prior-art in-repo

- **FAIL:** `…-offdiag-patchwork-inter012-template` — **`s`-split patchwork** is not **`min_d=2`** biconditional; **`complement(symdiff)`** appears as **`min_d=2`** witness while patchwork expected wedge.
- **PASS:** `…-structure-scan` — **`1190`** off-diagonal **`min_d=2`** cells exist.

## Falsifiable statement

Exhaust the **`22050`** grid; restrict to **`i<j`** and **`popc(T_i & T_j)=2`**. Let **`W`** and **`C`** be the wedge and complement-symdiff masks. Report counts of violations:

- **`min_d=2`** but **`Q ∉ {W,C}`**
- **`Q ∈ {W,C}`** but **`min_d≠2`**

If either is nonempty, the **two-chart disjunction** is **false** on this stratum.
