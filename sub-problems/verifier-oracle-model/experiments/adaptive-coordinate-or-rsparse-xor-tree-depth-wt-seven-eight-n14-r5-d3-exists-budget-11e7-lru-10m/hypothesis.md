# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** **`r=5`** **`d=3`** at **10⁸** **`exists_tree`** with **10M** LRU ended **PARTIAL** (~838 s). **12M** LRU **OOM**s on this host. Test a **modest +10%** visit budget (**1.1×10⁸**) at **fixed 10M** LRU to see if the probe completes without raising LRU past the OOM cliff.

2. **Analogous domains:** (a) Fixed cache, extended time horizon in iterative search. (b) Continuation in homotopy / budgeted search: small step past a known plateau.

3. **Machinery:** Same parent DP, **`--r-single 5`**, **`--d-min 3 --d-max 3`**, **`110000000`** max exists calls, **`10000000`** LRU.

4. **Transfer seed:** If **exit 0** with definite **`d=3`**, the extra **10⁷** visits sufficed; if **exit 2** **PARTIAL**, compare wall time vs **10e7/10M** (~838 s) for marginal cost of +10% budget.

## Falsifiable claim

**H0:** Exit **2** (PARTIAL) or host kill (**OOM** / non-0/2).

**H1:** Exit **0** with definite **`d=3 feasible=`** without budget exhaustion.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-10e7-lru-10m` (INCONCLUSIVE PARTIAL ~838 s), `…-10e7-lru-12m` (OOM — do not increase LRU).
