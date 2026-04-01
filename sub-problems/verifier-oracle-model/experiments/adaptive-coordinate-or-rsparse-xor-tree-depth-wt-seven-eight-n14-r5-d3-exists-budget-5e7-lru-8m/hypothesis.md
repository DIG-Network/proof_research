# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, `coord + r=5` XOR, `d=3`-only probe: raising the `exists_tree` budget to **5×10⁷** with a **larger LRU cap (8×10⁶)** either (a) completes with a definite `d=3` feasibility bit, or (b) at least clears the **5×10⁶** scale where the probe previously saturated in ~38 s.

**Context:** Prior shards: **5×10⁶** PARTIAL ~38.6 s (unbounded LRU); **2 h** wall-clock unbounded memo still no line; **r=6** behaves like **r=5** at 5e6; **r=7** is easy.

## Analogy pass (abbrev.)

1. **Abstract structure:** Decision problem over a huge AND–OR game tree; memoization turns it into “how many distinct subgames must we touch before the root value is known?”
2. **Analogous domains:** (i) endgame tables in chess with LRU cache; (ii) SAT/CDCL with clause deletion — completeness only if enough space-time; (iii) PDE time-stepping with adaptive mesh refinement budgets.
3. **Machinery:** Cache hit rate vs working-set size; scaling laws for partial computation.
4. **Transfer seed:** Treat **invocation count × LRU size** as a **two-axis** resource probe separate from wall-clock alone.
