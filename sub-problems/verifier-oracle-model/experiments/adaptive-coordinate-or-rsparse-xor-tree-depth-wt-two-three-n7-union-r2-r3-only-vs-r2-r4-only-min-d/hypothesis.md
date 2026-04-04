# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-union-r2-r3-only-vs-r2-r4-only-min-d`

## Analogy pass

1. **Abstract structure:** At **`n=7`**, shell **`{2,3}`**, **coord + full union `r∈{2,3,4}`** achieves **`min_d=2`** with **`91`** XOR splits, while **any** certificate using **only** coord + full **`r=2`** + **up to six** **sparse** **`r=3`** splits stays at **`min_d=3`** (exhaustive through **`C(35,6)`**). The remaining coarse question is **which full arity menus are individually sufficient** when **one** of **`{3,4}`** is dropped from the **`{2,3,4}`** union.

2. **Where else this structure appears:**
   - **Minimal feature sets / ablation:** remove one layer from a deep net and measure whether accuracy collapses.
   - **Generating sets in GF(2) linear algebra:** which parity families span the separating hyperplanes needed for a fixed finite classification task.
   - **Redundancy in basis expansions:** two different bases can both be sufficient; dropping one coordinate family may or may not preserve a short decision procedure.

3. **Machinery:** Same DP **`min_depth_for_language`** as the **`n=7`** driver; two mixed languages **`union-rs=2,3`** and **`union-rs=2,4`** ( **`56`** splits each **)** .

4. **Transfer seed:** If **`{2,3}`** alone still has **`min_d=2`**, then **full `r=4`** is **not necessary** for depth-**2** in this union-style family (**contrary** to the **sparse-triple-ladder** story, which concerns **partial** **`r=3`** menus). If **`{2,3}`** has **`min_d≥3`** but **`{2,4}`** has **`min_d=2`**, then **four-point parities** are **load-bearing** and **full triple parities** are **redundant** for this certificate **class**. If **both** are **`≥3`**, then **both** arities are **essential** in the **`{2,3,4}`** union.

## Falsifiable claims (primary / secondary)

- **Primary:** **`min_d ≥ 3`** for **coord + union `r∈{2,3}`** only (**`56`** splits **)** — i.e. **omitting full `r=4`** **precludes** depth-**2** on this **full-menu** slice **(** **matches** **the** **role** **of** **`r=4`** **in** **the** **`91`**-split **witness** **)** .

- **Secondary** **(** **measured** **,** **not** **gating** **exit** **)** **:** **`min_d`** for **coord + union `r∈{2,4}`** only.

**Opposite** **(** **primary** **)** **:** **`min_d = 2`** for **`{2,3}`** only.
