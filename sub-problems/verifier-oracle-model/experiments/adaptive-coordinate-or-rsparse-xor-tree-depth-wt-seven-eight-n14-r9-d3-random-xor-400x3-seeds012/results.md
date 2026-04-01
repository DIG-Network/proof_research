# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds012`

**Outcome:** PASS (engineering + completed three-seed random submenu scan; **no** `d=3` positive witness)

**Design:** Mirror `…-r5-d3-random-xor-400x3-seeds012`: for each seed in `{0,1,2}`, `random.Random(seed).sample(range(2002), 400)` → sorted indices → `--skip-baseline --r-single 9 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 55000000`. Canonical list is `C(14,9)=2002` XOR bipartitions (same count as `r=5`).

| Seed | XOR splits | `build_sec` | `dp_sec` | `d=3 feasible` | LRU misses after `d=3` |
|------|------------|-------------|----------|----------------|------------------------|
| 0 | 400 | ~4.24 | ~169.65 | False | 8_000_000 |
| 1 | 400 | ~4.09 | ~152.90 | False | 8_000_000 |
| 2 | 400 | ~4.10 | ~149.29 | False | 8_000_000 |

**Total wall time:** ~9.2 min (~552 s) for all three seeds on this host.

**Interpretation**

- All three non-contiguous 400-split `r=9` menus finished within budget with **`feasible=False` at `d=3`** and **LRU saturated** — same qualitative pattern as **`r=5`** random 400×3 and as **`r=9`** contiguous shard scan.
- **H2** confirmed for these seeds; **H1** (random witness) not found. Does **not** decide full-menu `r=9` `d=3` (still open alongside partial full-menu run).

**Repro:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds012/script.py`
