# Results

**Outcome:** INCONCLUSIVE (external termination — no DP completion line)

**Environment:** Cursor automation host (~15 GiB RAM advertised). Wrapper invokes parent  
`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 16000000 --max-exists-calls 100000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-1e8-lru-16m/script.py
```

**Observed:** Process ran **~5717 s** (~95 min) wall time (terminal harness metadata). Stdout never progressed beyond:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
```

Wrapper **exit code 247** (child did not exit 0/1/2 from parent’s normal codes — consistent with host-level kill / automation cap rather than `PARTIAL` or `PASS`).

**Metrics (partial)**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` (target) | 100,000,000 |
| `lru-maxsize` | 16,000,000 |
| Wall time to termination | ~5717 s |
| `d=3 feasible=` line | **not observed** |
| `PARTIAL: exceeded max_exists_calls` | **not observed** |

**Conclusion:** **2×** scaling of **(budget, LRU)** over **(5×10⁷, 8×10⁶)** does **not** yield a verdict in this environment within the available wall clock: the run is **heavier** than the **~421 s** **5e7/8M** **PARTIAL** (likely **larger LRU working set** ⇒ **slower** **per** **invocation** **and** **longer** **path** **to** **budget** **exhaustion** **or** **finish**). **No** evidence **for** **or** **against** **`d=3`** **feasibility** **for** **`r=5`**. Next: **unbounded** **memo** **`--lru-maxsize 0`** on a **large-RAM** **machine** **with** **explicit** **`timeout`**, **or** **process** **sharding** **/** **smaller** **incremental** **(e.g.** **7.5e7** **/** **12M)** **bracket** **on** **this** **host**.
