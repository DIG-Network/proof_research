# Results

**Outcome:** **INCONCLUSIVE** (resource / parallelism artifact; wrapper initially exited **1** before a post-run fix maps **SIGKILL** to exit **2**).

**Configuration:** Same as sequential **12e7×2** half-shards: `n=14`, shells `{7,8}`, `coord + r=9` XOR, `d=3`-only, ranges `[0:1001)` and `[1001:2002)`, **`--max-exists-calls 120000000`**, **`--lru-maxsize 10000000`**, `--skip-baseline`, **two subprocesses in parallel** (`ThreadPoolExecutor(max_workers=2)`).

**Observed run (first execution):**

- **Shard 0 (`0:1001`):** subprocess **returncode -9** (**SIGKILL**) after **~4849 s** wall for that worker — no `PARTIAL:` / completion line (**consistent with OOM killer** under **two** concurrent **10M** LRU resident sets).
- **Shard 1 (`1001:2002`):** completed with **exit 2** (PARTIAL): **~5838.35 s** DP (**~97.3 min**), LRU at cap **10M**; `d=3 feasible=False` at budget exhaustion. This is **~5.9×** the sequential half’s **~992 s** — **severe CPU/memory contention** from colocating two heavy processes.
- **Total wall-clock:** **~5890.5 s** (**~98 min**) — **not** ~half of sequential **~2121 s**; dominated by the slower shard under contention plus failed shard 0.

**Interpretation:** On this host, **parallel** dual **10M** LRU half-shards is **not** a safe substitute for sequential halves: one worker can be **SIGKILL**’d and the survivor’s DP time **balloons**. This **does not** resolve `r=9` `d=3` on the **2002** menu; it is an **infrastructure / scheduling** negative for this workload pattern.

**Script note:** After this run, `script.py` was updated so **returncode -9** is classified as **INCONCLUSIVE** (exit **2**) rather than **FAIL** (exit **1**), since SIGKILL is not a cryptographic verdict.
