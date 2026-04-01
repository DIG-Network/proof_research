# Results

**Outcome:** INCONCLUSIVE

**Environment:** Cursor automation host, **`timeout 7200`** wrapper, parent **`--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 0`**.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-two-hour/script.py
```

**Observed:** Subprocess **exit 124** after **~7200 s**. Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
INCONCLUSIVE: timeout 7200s (exit 124) — no d=3 feasibility line in budget.
```

No **`d=3 feasible=`** line from the parent.

**Conclusion:** **4×** the **30 min** budget (**1800 → 7200 s**) did **not** decide **`r=5` `d=3`**. The shard stays in the **multi-hour / overnight** class alongside **`r=9` `d=3`**; next brackets are **much longer wall-clock** on a **large-RAM** host or **process-level sharding** / algorithmic change—not another **small** timeout multiplier on the same machine.
