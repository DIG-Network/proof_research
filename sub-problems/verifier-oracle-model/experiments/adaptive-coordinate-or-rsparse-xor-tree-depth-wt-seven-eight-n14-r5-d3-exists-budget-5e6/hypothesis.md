# Hypothesis

## Analogy pass

1. **Abstract structure:** The `n=14`, `{7,8}` adaptive tree search is a depth-first / memoized feasibility DP over subsets of a 6435-mask domain. Wall-clock timeouts only tell us the run did not finish; they do not quantify how much of the state space was explored.
2. **Analogous domains:** (a) Branch-and-bound for combinatorial optimization — record node counts, not only time limits. (b) Theoretical CS lower bounds via query complexity — count oracle calls. (c) Numerical PDE solvers — track residual iterations vs CPU time.
3. **Machinery in those domains:** Node budgets, call counters, and iteration counts give comparable progress metrics across machines.
4. **Transfer candidate:** Instrument `exists_tree` with a **hard cap on total invocations** (via `lru_cache` call counting) so short runs report **partial progress** in a machine-independent unit.

## Falsifiable claim

**Claim:** For `coord + r=5` XOR, `d=3`-only, unbounded LRU (`--lru-maxsize 0`), a budget of **5×10⁶** `exists_tree` invocations finishes within **≤120 s** on this automation host **and** either returns **`feasible=True`** or **`feasible=False`** for `d=3`.

**Outcome driver:** If the budget is exhausted first (exit **2**, `PARTIAL`), the claim is **falsified** for that budget/time pair; we still gain a **calibrated scale** for comparing to multi-hour unbounded runs.
