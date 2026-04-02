# Results

**Outcome:** INCONCLUSIVE (exit 2 from wrapper: both subprocesses returned exit 2 PARTIAL; no `d=3 feasible=True` witness).

## Configuration

- `n=14`, masks with popcount in `{7,8}` (6435 masks).
- `d=3` only (`--d-min 3 --d-max 3`), `--skip-baseline`.
- XOR submenu: **1001** partitions selected by **even indices** `0,2,4,…,2000` in the canonical `itertools.combinations` order for `r-sparse` XOR (total list length 2002 for both `r=5` and `r=9`). Same cardinality as contiguous half `[0:1001)` but **interleaved** across the full menu.
- Per run: `--max-exists-calls 120000000`, `--lru-maxsize 8000000` (matches `*-xor-shard-halves-12e7-each-lru-8m` envelope).
- Sequential: `r=5` then `r=9` (single process).

## Measured output

| Phase | `exists_tree` cap hit | LRU | `d=3 feasible` line | DP wall (parent stderr/stdout) |
|-------|----------------------|-----|----------------------|--------------------------------|
| r=5 | yes (PARTIAL) | 8M full | False (incomplete probe) | ~940.82 s |
| r=9 | yes (PARTIAL) | 8M full | False (incomplete probe) | ~940.97 s |

**Total sequential wall:** ~1882 s (~31.4 min), comparable to paired contiguous half-shards (~1853 s aggregate for r=5 halves in prior entry).

## Interpretation

Non-contiguous **1001-wide** parity-interleaved submenu does **not** improve over contiguous half-shards at this budget: both runs exhaust `12e7` `exists_tree` with LRU saturated, still no completion verdict for `d=3`. Does **not** refute the hypothesis that geometry differs from contiguous halves (timings are similar, not faster), but provides another **INCONCLUSIVE** data point for the `{7,8}` / `r∈{5,9}` / `d=3` band.
