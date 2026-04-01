# Results

**Outcome:** INCONCLUSIVE (process killed — likely OOM; no DP completion line)

**Environment:** Cursor automation host. Wrapper invokes parent  
`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 0 --max-exists-calls 75000000`.

**Command (repo root):**

```bash
timeout 14400 python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-75e6-lru-0/script.py
```

**Observed:** Wrapper **exit code 247** after **~5085 s** wall (**~84.8 min**). Stdout never progressed beyond:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
```

No **`d=3 feasible=`** line and no **`PARTIAL: exceeded max_exists_calls`**. Pattern matches **`…-75e6-lru-12m`** (**SIGKILL** / **OOM** class) and **`…-1e8-lru-16m`** (long run then kill), not **`timeout 124`**.

**Metrics (partial)**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` (target) | 75,000,000 |
| `lru-maxsize` | 0 (unbounded memo) |
| Wall time to termination | ~5085 s (~1.41 h) |
| Wrapper exit code | 247 |
| `d=3 feasible=` line | **not observed** |
| `PARTIAL: exceeded max_exists_calls` | **not observed** |

**Conclusion:** **Unbounded** memo with **7.5×10⁷** visit cap **does not** yield a **clean** **PARTIAL** or **feasibility** verdict on this host — the run is **killed** mid-**`d=3`** probe after **~85 min**, **longer** than **~8 min** for **12M LRU** but still **short** of **4 h** **timeout** and **short** of **~95 min** **1e8/16M** kill. **`r=5` `d=3`** **feasibility** remains **open** here; **5e7/8M** remains the only **completed** capped bracket (**PARTIAL**). **Next:** **larger** **RAM** **/** **different** **host**, **shard** **search**, **or** **lower** **budget** **unbounded** **trial** **only** **if** **memory** **profiling** **warrants** **it**.
