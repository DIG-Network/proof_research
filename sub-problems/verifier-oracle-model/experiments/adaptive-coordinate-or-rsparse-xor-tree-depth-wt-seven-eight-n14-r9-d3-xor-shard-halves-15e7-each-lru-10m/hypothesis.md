# Hypothesis

## Analogy pass

1. **Abstract structure:** The DP explores a huge memoized search tree; `PARTIAL` means the frontier outgrows a fixed LRU before the `d=3` feasibility question is decided. This resembles **numerical PDEs** where mesh refinement converges only if both resolution (budget) and cache (working set) scale together.

2. **Analogous domains:** (a) **Branch-and-bound** — cutting planes without enough node budget leaves “unknown” regions. (b) **SAT/CDCL** — clause learning capacity vs search depth. (c) **Numerical continuation** — path-following fails if step size (budget per segment) is too small for the fixed history window.

3. **Machinery in those domains:** raise resolution; widen the working-memory window; or change the formulation. Here the formulation is fixed (XOR shard halves); we test **joint** budget + LRU uplift.

4. **Transfer candidate:** Prior `r=9` half-shard runs at `12e7`/`8M` were **PARTIAL** on at least one half. Increasing **both** `--max-exists-calls` to `15e7` and `--lru-maxsize` to `10M` (sequential halves, single process at a time) may allow the second half to finish and either witness `d=3` or return a definite infeasible — without repeating the exhausted 1001-index coset scans.

## Falsifiable claim

For `n=14`, weight band `{7,8}`, `r=9`, `d=3`-only probe, XOR menu as two contiguous index ranges `[0:1001)` and `[1001:2002)`, with **`15_000_000`** `exists_tree` budget per half and **`10_000_000`** LRU each (sequential), at least one run completes **without** `PARTIAL` and we learn whether `d=3` is feasible on that completion path (PASS if `feasible=True`, FAIL if both complete and `feasible=False`, INCONCLUSIVE if still PARTIAL with no witness).
