# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds91011`

**Outcome:** PASS (engineering + completed three-seed random submenu scan; **no** `d=3` positive witness)

**Design:** Same as `…-r9-d3-random-xor-400x3-seeds678`: for each seed in `{9,10,11}`, `random.Random(seed).sample(range(2002), 400)` → sorted indices → `--skip-baseline --r-single 9 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 55000000`. Canonical list is `C(14,9)=2002` XOR bipartitions.

| Seed | XOR splits | `build_sec` | `dp_sec` | `d=3 feasible` | LRU misses after `d=3` |
|------|------------|-------------|----------|----------------|------------------------|
| 9 | 400 | ~4.22 | ~174.37 | False | 8_000_000 |
| 10 | 400 | ~4.17 | ~152.33 | False | 8_000_000 |
| 11 | 400 | ~4.10 | ~133.78 | False | 8_000_000 |

**Total wall time:** ~541 s (~9.0 min) for all three seeds on this host.

**Interpretation**

- All three non-contiguous 400-split `r=9` menus finished within budget with **`feasible=False` at `d=3`** and **LRU saturated** — consistent with seeds `{0..8}`, contiguous shard scan, and symmetric `r=5` random probes.
- **H2** confirmed for seeds `{9,10,11}`; **H1** not found. Does **not** decide full-menu `r=9` `d=3` (still PARTIAL at 5e7/8M for the full 2002 menu).

**Repro:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds91011/script.py`
