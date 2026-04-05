# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-septuple-r3-scan-all-septuples`

## Analogy pass

1. **Abstract structure:** At **`n=7`**, **`{2,3}`**, the ladder **coord + full `r=2` + k sparse `r=3` XOR splits** was closed through **`k=6`** by exhaustive **`C(35,6)`** with **every** sextuple giving **`min_d=3`**. The next finite combinatorial rung is **`k=7`**: unordered septuples of triple indices, universe **`C(35,7)=6724520`**. Exhaustive enumeration is the proof obligation (random **`400`** sample had **`witness_min_d2_count=0`** but is not a closure).

2. **Where else this structure appears:**
   - **Finite combinatorial closure** after nested negative envelopes (quintuple → sextuple → septuple).
   - **Coding / parity menus:** each `r=3` split is a parity test; depth-2 feasibility is a structured search over **7** chosen parities plus the full **`r=2`** menu.
   - **Rare-witness search:** if a witness exists, exhaustive scan finds it; if not, we obtain a **uniform** negative over the full **`C(35,7)`** family.

3. **Machinery in those domains:** Complete enumeration; early exit on first **`min_d=2`** witness (PASS); otherwise FAIL with **`witness_min_d2_count=0`**.

4. **Transfer seed:** Close **`C(35,7)`** exactly as **`C(35,5)`** and **`C(35,6)`** were closed—no sampling gap.

## Falsifiable claim

**There exists** an unordered **7-tuple** of indices **`0..34`** such that **coord + full `r=2` + those seven `r=3` XOR splits** yields **`min_d=2`** in this DP model.

**Opposite outcome:** **every** one of the **`6724520`** septuples has **`min_d=3`** (**`witness_min_d2_count=0`**).
