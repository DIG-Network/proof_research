# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** The verifier-oracle DP on `coord + r-sparse XOR` splits is a bounded-work search for a depth-`d` decision tree. At `n=14`, `{7,8}`, `r=5`, `d=3`, prior runs hit a **50M exists_tree / 8M LRU** cap before deciding feasibility — same split menu size as `r=9` (2002), but empirically similar hardness to `r=9` at that envelope.

2. **Analogous domains:** (a) Branch-and-bound with memoization — cache fills and search truncates before optimality proof. (b) PDE/time-stepping — doubling step budget to see if boundary is numerical vs structural. (c) SAT solver clause learning — more conflicts allowed may finish or still timeout.

3. **Machinery in those domains:** Increase compute envelope slightly; compare wall time and termination (PASS vs PARTIAL).

4. **Transfer seed:** If **+20%** invocation budget (`6×10⁷`) over the **5×10⁷** `r=5` run yields **`feasible=True/False`** instead of PARTIAL, we learn whether the 50M cutoff was **near** a decision boundary or still **far** (still PARTIAL ⇒ need much larger budget or different algorithm).

## Falsifiable claim

**H0:** Under `--max-exists-calls 60000000`, `--lru-maxsize 8000000`, `r=5`, `d=3`-only, the parent script still exits **2** (PARTIAL).

**H1:** The same run completes with a definite **`d=3 feasible=`** line (PASS or explicit infeasibility), i.e. not PARTIAL.

## Memory / lineage

- **Parent experiments:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-lru-8m` (PARTIAL ~421s), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-d3-exists-budget-5e7-lru-8m` (PASS — contrast).
