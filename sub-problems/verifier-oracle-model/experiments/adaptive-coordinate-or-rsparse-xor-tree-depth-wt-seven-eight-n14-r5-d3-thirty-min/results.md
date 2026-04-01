# Results

**Outcome:** INCONCLUSIVE

**Environment:** Cursor automation host, **15 GiB** RAM, **4** cores, **`timeout 1800`** wrapper, parent **`--lru-maxsize 0`**.

**Command (repo root):**

```bash
timeout 1800 python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py \
  --skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 0
```

**Observed:** Subprocess **exit 124** after **~1800 s**. Stdout ended at:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
```

No **`d=3 feasible=`** line.

**Conclusion:** **Hypothesis falsified** in the sense of the stated claim: **30 minutes** did **not** suffice to decide **`d=3`** for **`r=5`**. The shard remains in the same **open** class as **`r=9` `d=3`** (**multi-hour** / large-RAM host still required for a decision).
