# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-random-xor-400x3-seeds012`

**Outcome:** PASS (engineering + completed three-seed random submenu scan; **no** `d=3` positive witness)

**Parent change:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` gained `--xor-index-indices I,J,K,...` (mutually exclusive with `--xor-index-range`). Keeps only listed 0-based indices into the canonical `C(14,5)=2002` XOR partition list.

**Design:** For each seed in `{0,1,2}`, `random.Random(seed).sample(range(2002), 400)` → sorted unique indices → same DP flags as contiguous shard scan: `--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 55000000`.

| Seed | XOR splits | `build_sec` | `dp_sec` | `d=3 feasible` | LRU at end |
|------|------------|-------------|----------|------------------|------------|
| 0 | 400 | ~2.64 | ~167.67 | False | 8_000_000 |
| 1 | 400 | ~2.87 | ~163.36 | False | 8_000_000 |
| 2 | 400 | ~2.81 | ~198.59 | False | 8_000_000 |

**Interpretation**

- All three non-contiguous 400-split menus finished within budget with **`feasible=False` at `d=3`** — **H2** confirmed for these seeds; **H1** (random witness) not found.
- Does **not** contradict contiguous shard scan: both are **negative evidence** for finding a **small** submenu that already admits depth-3 feasibility; **full** 2002-split `min_d` remains **open** (prior partial `5e7`/8M run).

**Repro:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-random-xor-400x3-seeds012/script.py` (~8–10 min total on this host).
