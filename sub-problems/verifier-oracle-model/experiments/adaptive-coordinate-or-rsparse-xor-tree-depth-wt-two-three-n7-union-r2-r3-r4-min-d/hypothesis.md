# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-union-r2-r3-r4-min-d`

## Analogy pass

1. **Abstract structure:** At **n=7**, shell **`{2,3}`**, we already know **coord + union `r∈{2,3,4,5}`** achieves **`min_d=2`**. After exhaustive **quintuple `r=3`** scans showed **no** depth-2 witness with **only** coord + full **`r=2`** + up to **five** triple-parities, the next structural question is **which arities are essential** in the full union certificate — in particular whether **`r=5`** (21 five-point parities) is necessary or **`r=4`** (35 four-point parities) already suffices together with **`r=2`** and **`r=3`**.

2. **Where else this structure appears:**
   - **Minimal sufficient statistic / feature selection:** drop coordinates from a rich model until prediction degrades.
   - **Circuit complexity / gate basis:** which parity gates are redundant given others.
   - **Matroid / span in GF(2):** which parity families generate the same separations on a fixed finite mask set.

3. **Machinery:** same DP **`min_depth_for_language`** as the parent **`n=7`** driver; one mixed language **`union-rs=2,3,4`**.

4. **Transfer seed:** If **`min_d=2`** still holds without **`r=5`**, the **`n=7`** depth-2 barrier for “few triples” coexists with a **compact** (fixed **91** split) multi-arity menu; if **`min_d=3`**, then **`r=5`** parities are **necessary** for depth-2 in this union family at this slice.

## Falsifiable claim

**`min_d=2`** for **coord + full `r=2` XOR menu + full `r=3` + full `r=4`** (no **`r=5`**).

**Opposite:** **`min_d=3`** (or higher) with **`union-rs=2,3,4`**.
