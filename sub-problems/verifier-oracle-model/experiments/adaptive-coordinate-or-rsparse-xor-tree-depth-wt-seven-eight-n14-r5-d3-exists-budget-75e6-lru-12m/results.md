# Results

**Outcome:** INCONCLUSIVE (process killed — likely OOM; no DP completion line)

**Environment:** Cursor automation host. Wrapper invokes parent  
`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 12000000 --max-exists-calls 75000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-75e6-lru-12m/script.py
```

**Observed:** Two runs on this host both terminated with **wrapper exit code 247** (child exit **-9** ⇒ **SIGKILL**), consistent with **OOM** or host cgroup limit rather than parent’s normal **0/1/2** codes. Stdout never progressed beyond:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
```

**Wall time:** ~**470–490 s** (~7.8–8.2 min) to kill — **much sooner** than the **~5717 s** **1e8/16M** run, suggesting this **(7.5e7, 12M)** configuration **exceeds** this machine’s **effective RAM** budget **before** exhausting **`max_exists_calls`**.

**Metrics (partial)**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` (target) | 75,000,000 |
| `lru-maxsize` | 12,000,000 |
| Wall time to SIGKILL | ~470–490 s |
| `d=3 feasible=` line | **not observed** |
| `PARTIAL: exceeded max_exists_calls` | **not observed** |

**Conclusion:** The **intermediate** **(7.5×10⁷, 12×10⁶)** bracket **does not** yield a **clean PARTIAL** on this host — the process is **killed** early. **5e7/8M** remains the **only** **completed** **capped** data point for **`r=5` `d=3`** here (**PARTIAL** at **50M** invocations). **Next:** **`--lru-maxsize 0`** on a **large-RAM** machine with explicit **`timeout`**, or **smaller** **LRU** **with** **same** **7.5e7** **budget** **(** **e.g.** **9M** **)** **only** **if** **RAM** **allows** **;** **otherwise** **avoid** **12M+** **LRU** **on** **this** **class** **of** **host**.
