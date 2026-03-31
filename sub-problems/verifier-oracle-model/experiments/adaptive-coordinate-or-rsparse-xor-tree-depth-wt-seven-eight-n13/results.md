# Outcome: PASS

## Baseline (`--baseline-only`)

- **Domain:** `n=13`, `|S| ∈ {7,8}`, `|masks| = C(13,7)+C(13,8) = 3003`, majority `t=8`.
- **coord-only:** `min_d = 13`.
- **coord + full 13-XOR:** `min_d = 1`.
- **Earlier baseline wall time:** ~31 s (per prior run notes).

## Single-arity row (`--skip-baseline --r-single r`)

**Canonical `min_d(r)` for `r=2..12`:** `7,5,4,3,3,3,4,3,4,3,2`.

Timings below are **wall-clock DP** for the inner `exists_tree` scan (per shard); they depend strongly on **memo policy** and host.

### Timings (unbounded memo, original resolved run)

| r | XOR splits | min_d | dp_sec (approx) |
|---|------------|-------|-----------------|
| 2 | 78 | 7 | 1079 |
| 3 | 286 | 5 | 3527 |
| 4 | 715 | 4 | 460 |
| 5 | 1287 | 3 | 41 |
| 6 | 1716 | 3 | 11 |
| 7 | 1716 | 3 | 6 |
| 8 | 1287 | 4 | 1500 |
| 9 | 715 | 3 | 13 |
| 10 | 286 | 4 | 21 |
| 11 | 78 | 3 | 0.03 |
| 12 | 13 | 2 | 0.002 |

### Timings (default `--lru-maxsize 4000000`, automation host)

Same **feasibility** answers; **much** longer wall time on heavy **`r`** because of cache eviction / recomputation.

| r | XOR splits | min_d | dp_sec (approx) |
|---|------------|-------|-----------------|
| 2 | 78 | 7 | 4516 |
| 3 | 286 | 5 | 7689 |
| 4 | 715 | 4 | 880 |
| 5 | 1287 | 3 | 45 |
| 6 | 1716 | 3 | 10 |
| 7 | 1716 | 3 | 6 |
| 8 | 1287 | 4 | 3341 |
| 9 | 715 | 3 | 14 |
| 10 | 286 | 4 | 21 |
| 11 | 78 | 3 | 0.02 |
| 12 | 13 | 2 | 0.001 |

## Unions

| RS | total splits | min_d | dp_sec (approx) |
|----|--------------|-------|-----------------|
| 2,3,4 | 1079 | 4 | 1514 (unbounded) / 3380 (LRU 4M) |
| 2,3,4,5 | 2366 | 3 | 453 (unbounded) / 542 (LRU 4M) |
| 2,3,4,5,6 | 4082 | 3 | 61 (LRU 4M) |
| 2..12 | 8177 | 2 | 0.06 |

## Comparison: same `n=13`, different adjacent shells

| Experiment | `|domain|` | `min_d(2..12)` row | `{2,3,4}` | `{2..5}` | `{2..12}` |
|------------|------------|--------------------|-----------|----------|-----------|
| `{6,7}`, `t=7` | 3432 | `7,5,4,3,3,3,4,3,4,3,2` | 4 | 3 | 2 |
| `{7,8}`, `t=8` | 3003 | `7,5,4,3,3,3,4,3,4,3,2` | 4 | 3 | 2 |

The **full `min_d(r)` vector and the listed union depths match** despite different mask sets (3003 vs 3432). Suggests the DP optimum for this gate library on `n=13` is **insensitive** to which adjacent majority-shell pair is chosen, for these statistics.

## Hypotheses

- **H1:** PASS.
- **H2:** PASS (full row; non-monotone in `r` as expected).
- **H3:** PASS — `{2..5}→3`, `{2..12}→2`; triple union `{2,3,4}→4` (same as `{6,7}` slice on n=13).

## Implementation notes (`script.py`)

- **`--lru-maxsize N`:** default **4_000_000** caps `functools.lru_cache` on `exists_tree` to avoid **OOM** (observed **SIGKILL** on **`r=2`** with unbounded memo on a constrained host). Use **`--lru-maxsize 0`** for unbounded memo when RAM allows (faster on heavy shards).
- **Progress:** prints **`probing d=…`** before each depth trial and uses **`flush=True`** so long runs are visible under piped / captured logs.

## Repro

`python3 script.py --baseline-only`; then for each `r`: `python3 script.py --skip-baseline --r-single r`. Unions: `python3 script.py --skip-baseline --union-rs "2,3,4"` etc. Add `--lru-maxsize 0` only on hosts with enough memory.
