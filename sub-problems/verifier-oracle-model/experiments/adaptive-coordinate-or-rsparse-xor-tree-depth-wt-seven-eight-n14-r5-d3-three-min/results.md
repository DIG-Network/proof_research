# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-three-min

**Outcome:** INCONCLUSIVE (wall-clock budget; no feasibility bit)

## Command

```bash
timeout 180 python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py \
  --skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 0
```

## Observed

- **Exit code:** **124** (`timeout`)
- **Stdout (abridged):** `skip_baseline=1 …` then `probing d=3 …` with **no** trailing **`d=3 feasible=`** line within **180 s**.

## Conclusion

**Hypothesis falsified** in the sense that **3 minutes** is **not** sufficient to decide **`d=3`** here; **not** a proof that **`d=3`** is infeasible or feasible — **decidability at this shard remains open** pending **longer** wall-clock or **algorithmic / sharding** changes.
