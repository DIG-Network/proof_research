# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds678`

**Outcome:** PASS (engineering + completed three-seed random submenu scan; **no** `d=3` positive witness)

**Design:** Extend `…-r9-d3-random-xor-400x3-seeds012`: for each seed in `{6,7,8}`, `random.Random(seed).sample(range(2002), 400)` → sorted indices → `--skip-baseline --r-single 9 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 55000000`. Canonical list is `C(14,9)=2002` XOR bipartitions.

| Seed | XOR splits | `build_sec` | `dp_sec` | `d=3 feasible` | LRU misses after `d=3` |
|------|------------|-------------|----------|----------------|------------------------|
| 6 | 400 | ~4.08 | ~152.71 | False | 8_000_000 |
| 7 | 400 | ~4.06 | ~146.02 | False | 8_000_000 |
| 8 | 400 | ~4.08 | ~148.36 | False | 8_000_000 |

**Total wall time:** ~8.7 min (~521 s) for all three seeds on this host.

**Interpretation**

- All three non-contiguous 400-split `r=9` menus finished within budget with **`feasible=False` at `d=3`** and **LRU saturated** — consistent with seeds `{0,1,2}`, contiguous shard scan, and the symmetric `r=5` random probes.
- **H2** confirmed for seeds `{6,7,8}`; **H1** not found. Does **not** decide full-menu `r=9` `d=3` (still PARTIAL at 5e7/8M for the full 2002 menu).

**Repro:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds678/script.py`
