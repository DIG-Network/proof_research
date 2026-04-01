# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** The `coord + r=5` XOR DP at `n=14`, `{7,8}`, `d=3` hit **PARTIAL** at **5e7/8M** (~421 s) and again at **6e7/8M** (~569 s). The marginal cost of +10M calls was ~148 s; we test whether another +10M (**7e7**) crosses a completion threshold or remains structurally truncated.

2. **Analogous domains:** (a) Iterative refinement with fixed cache — more iterations may or may not reach fixed point. (b) Numerical continuation — step further along the same path. (c) Resource-bounded theorem proving — more search steps.

3. **Machinery:** Increase `--max-exists-calls` to **7×10⁷** with same **8M** LRU; compare exit code and wall time to **6e7**.

4. **Transfer seed:** If still **PARTIAL** at **7e7**, the **2002** `r=5` `d=3` probe is not a **near-threshold** artifact at +40% over **5e7**; larger budgets or different algorithms are required.

## Falsifiable claim

**H0:** Under `--max-exists-calls 70000000`, `--lru-maxsize 8000000`, `r=5`, `d=3`-only, the parent exits **2** (PARTIAL).

**H1:** The run completes with exit **0** and a definite **`d=3 feasible=`** line (no budget exhaustion mid-probe).

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-6e7-lru-8m` (INCONCLUSIVE PARTIAL ~569 s), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-lru-8m` (PARTIAL ~421 s).
