# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-random-xor-400x3-seeds345`

**Outcome:** PASS (engineering + completed three-seed random submenu scan; **no** `d=3` positive witness)

**Design:** Same as `…-seeds012`: for each seed in `{3,4,5}`, `random.Random(seed).sample(range(2002), 400)` → sorted indices → `--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 55000000`.

| Seed | XOR splits | `build_sec` | `dp_sec` | `d=3 feasible` | LRU misses at end |
|------|------------|-------------|----------|----------------|-------------------|
| 3 | 400 | ~2.75 | ~176.99 | False | 8_000_000 |
| 4 | 400 | ~2.64 | ~157.61 | False | 8_000_000 |
| 5 | 400 | ~2.69 | ~149.17 | False | 8_000_000 |

**Interpretation**

- All three menus finished within budget with **`feasible=False` at `d=3`** and **LRU saturated** — extends seeds **0–2** with **independent** random 400-menus; still **negative evidence** for a small-menu depth-3 witness, **not** a full 2002-split impossibility proof.

**Repro:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-random-xor-400x3-seeds345/script.py` (~8–9 min total on automation host).
