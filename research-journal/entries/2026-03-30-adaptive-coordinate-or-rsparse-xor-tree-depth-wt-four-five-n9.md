# Entry — 2026-03-30 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-four-five-n9`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-four-five-n9/`

**Context:** `verifier-oracle-model` — extend **`min_d(r)`** sweep after **096** **`(8,{4,5})`**.

**Hypothesis tested:** On **`n=9`**, **`|x|∈{4,5}`** (**252** masks), **`n=2t−1`** for **`t=5`**, compute **`min_d`** for **coord + `r`-sparse XOR** only for **`r=2..8`**, full parity, and unions.

**Outcome:** PASS

**Key finding:** **`min_d(r)`** **:** **`r=2→5`**, **`3,4,5,7→3`**, **`6→4`** **(interior peak)**, **`8→2`**. **Union** **`r∈{2,3,4,5}`** **`min_d=2`**. Same **shell** **pair** **as** **096** **but** **`n=9`** **:** **pair** **gate** **worse** **than** **`n=8`** **(** **5** **vs** **4** **)** **;** **6**-**sparse** **is** **strictly** **worse** **than** **5**- **and** **7**-**sparse** **(** **4** **vs** **3** **)** **.**

**Implications:**

- **096** **non-monotonicity** **is** **not** **an** **`n=8`** **artifact** **;** **interior** **maxima** **in** **`r`** **appear** **on** **larger** **`n`** **too** **.
- **Complement** **symmetry** **class** **`n=2t−1`** **does** **not** **restore** **a** **simple** **monotone** **`r`** **ladder** **for** **this** **shell** **pair** **.

**Analogy pass summary:** **096**/**095**/**093** **rows** **;** **same** **`{4,5}`** **shells** **,** **vary** **`n∈{8,9}`** **.**

**Invented space:** none.

---

**Update (2026-04-03):** The experiment folder’s **`script.py`** was rebased to the **`n=10`**-style CLI (**`--union-rs`**, **`--lru-maxsize`**, etc.). Journal certification of the **full** multi-arity union **`coord + ⋃_{r=2}^{8} XOR_r`** (**501** splits, **`min_d=2`**) is in **`2026-04-03-adaptive-coordinate-or-rsparse-xor-tree-depth-wt-four-five-n9-full-r2-r8-union-min-d.md`** (index row dated 2026-04-03).
