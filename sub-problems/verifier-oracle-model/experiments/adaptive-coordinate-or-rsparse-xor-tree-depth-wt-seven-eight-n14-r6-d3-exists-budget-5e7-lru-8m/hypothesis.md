# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, `coord + r=6` XOR, `d=3`-only probe: the same **`5×10⁷`** `exists_tree` budget and **`8×10⁶`** LRU cap as the **`r=5`** shard either (a) completes with a definite `d=3` feasibility bit, or (b) exhibits comparable **PARTIAL** behavior (confirming **`r=6`** stays in the hard bracket at this scale).

**Context:** **`r=6`** matched **`r=5`** at **5×10⁶** (both PARTIAL ~31–35 s). **`r=5`** at **5×10⁷** + LRU **8M** still PARTIAL ~421 s. This run **mirrors** that configuration for **`r=6`**.

## Analogy pass (abbrev.)

1. **Abstract structure:** Same AND–OR game tree as the **`r=5`** probe; only the split library (5-sparse vs 6-sparse XOR gates) changes the state graph shape.
2. **Analogous domains:** (i) chess endgame tables with different move generators; (ii) SAT with different clause pools — same budget, different branching; (iii) adaptive mesh refinement with different refinement stencils.
3. **Machinery:** Working-set growth vs cache cap; whether **`r=6`** needs more or fewer distinct memo keys than **`r=5`** at fixed depth cap.
4. **Transfer seed:** **Controlled variable** — isolate **`r`** while holding **(budget, LRU, d-window)** fixed to compare **`r=5` vs `r=6`** scaling at **5e7**.
