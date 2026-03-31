# Journal entry: 2026-03-31 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12-rerun-r5-r7

**Date:** 2026-03-31  
**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12`  
**Context:** verifier-oracle-model (follow-up to `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12`)

**Hypothesis tested:** Standalone `python3 script.py --skip-baseline --r-single 5` and `--r-single 7` may complete on a fresh automation host and yield `min_d(5)`, `min_d(7)` for the `n=12`, `wt∈{6,7}` coord + r-sparse XOR language.

**Outcome:** INCONCLUSIVE (process killed; no `min_d` values recovered)

**Finding:** Both invocations exited **137** (SIGKILL / OOM) after on the order of **3 minutes** of wall time, matching the prior host behavior documented in the parent experiment’s `results.md`. The **792**-split XOR menus at **r=5** and **r=7** still appear to exceed practical memoized-DP RSS for this cgroup.

**Implications:**

- Standalone certificates for **`min_d(5)`** / **`min_d(7)`** on this domain remain **open** until a higher-memory run or a memory-bounded DP implementation.
- **Union** languages including all **r** except **5** and **7** already gave **`min_d=2`** in the parent experiment; this rerun does not change that conclusion.

**Analogy pass summary:** N/A (operational rerun, not a new construction hypothesis).

**Pointer:** Parent results in `.../adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12/results.md`.
