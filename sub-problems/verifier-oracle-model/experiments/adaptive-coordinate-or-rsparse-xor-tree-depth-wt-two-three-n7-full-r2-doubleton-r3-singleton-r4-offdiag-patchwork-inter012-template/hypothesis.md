# Hypothesis — off-diagonal patchwork by triple intersection size (`n=7`, doubleton `r=3` + singleton `r=4`)

## Abstract structure

We have a fixed **coordinate** refinement of a **56-mask** universe (`wt ∈ {2,3}` on 7 bits), plus **one full `r=2` XOR menu**, **two `r=3` XOR splits** indexed by triples `T_i, T_j` (order matters only through which split masks are in the language), and **one `r=4` XOR split** indexed by quartic `Q`. The DP computes **`min_d`** for acceptance of this XOR-tree language. Empirically there are **`1225`** cells with **`min_d=2`**; **`35`** are diagonal (`i=j`) and **`1190`** are off-diagonal (`i<j`). The diagonal case is closed: **`Q = [7] \ T_i`**. The prior experiment falsified a single **unordered** law **`|T_i∩T_j|=1` ∧ `Q = T_i △ T_j`** for all off-diagonal witnesses.

**Claim under test:** Off-diagonal **`min_d=2`** might still admit a **short case split** by **`s = |T_i ∩ T_j| ∈ {0,1,2}`**, using **symmetric difference** when **`s∈{0,1}`** and an **ordered** “outer wedge” when **`s=2`**:

- **`s=0`:** `Q = T_i △ T_j` (equals **`T_i ∪ T_j`** when disjoint).
- **`s=1`:** `Q = T_i △ T_j`.
- **`s=2`:** `Q = (T_i \ T_j) ∪ ([7] \ (T_i ∪ T_j))` (vertices in **`T_i` only** or **outside both** triples).

Together with the diagonal complement law, this is a **patchwork template** suggested by **lexicographic asymmetry** in the doubleton-triple menu.

## Analogy pass

1. **Abstract structure:** A finite configuration space (**triples/quartics**) maps to a **hard predicate** (**`min_d=2`**) defined by a **global consistency** property (**DP feasibility**). Local **intersection pattern** of supports is a **natural stratification**; different strata may need **different sufficient statistics** (here: different set formulas for **`Q`**).

2. **Where else:** (i) **Piecewise regression / segmented models** — one global formula rarely fits; **change surfaces** in covariate space. (ii) **Stratified sufficient statistics** — the **minimal summary** of data depends on **overlap pattern** (e.g. **capture–recapture** with **0/1/2** shared tags). (iii) **Fault diagnosis with shared components** — **symptoms** depend on whether faults **disjointly**, **simply overlap**, or **share a module**; different **syndrome** encodings apply.

3. **Machinery in those domains:** **Likelihood ratios** / **different local charts**; **contingency tables** by overlap type; **directed** versus **undirected** interaction graphs when **overlap is asymmetric** in the generating process.

4. **Transfer candidate:** Treat **`s=|T_i∩T_j|`** as the **stratum variable**; keep **XOR/symdiff** where supports are **thinly overlapping**, but switch to an **ordered difference + exterior** template when two triples **share two vertices** (a **doubleton overlap**), matching the **session-state** suggestion **`(T_i\T_j)∪([7]\(T_i∪T_j))`**.

## Memory / prior-art in-repo

- **FAIL (2026-04-05):** `…-offdiag-symmetric-diff-predicate` — **`Q=T_i△T_j`** is **neither necessary nor sufficient** without **`s`** split; many **`min_d=2`** with **`|∩|=2`**, and **`315`** false positives with **`|∩|=1` ∧ `Q=T_i△T_j`** but **`min_d=3`**.
- **PASS (same day):** `…-structure-scan` — enumerates **`1225`** depth-2 cells; **`1190`** off-diagonal.

## Falsifiable statement

On the full **`22050`**-cell grid, for every **`i≤j, k`**:

- If **`min_d=2`** then the **patchwork predicate** above holds (**diagonal:** complement; **off-diagonal:** cases **`s∈{0,1,2}`**).
- Conversely, if the predicate holds then **`min_d=2`** (no **`min_d≥3`** cells satisfy the predicate).

If any violation occurs, the patchwork classifier is **false**.
