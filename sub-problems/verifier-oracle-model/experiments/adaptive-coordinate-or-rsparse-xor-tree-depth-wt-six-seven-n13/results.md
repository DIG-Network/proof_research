# Outcome: PASS

## Baseline (`--baseline-only`)

- **Domain:** `n=13`, `|S| ∈ {6,7}`, `|masks| = 3432`, majority `t=7`.
- **coord-only:** `min_d = 13`.
- **coord + full 13-XOR:** `min_d = 1`.
- **Wall time:** ~27 s (earlier run).

## Single-arity row (`--skip-baseline --r-single r`)

| r | XOR splits | min_d | dp_sec (approx) | Notes |
|---|------------|-------|-----------------|-------|
| 2 | 78 | 7 | 1356 | |
| 3 | 286 | 5 | 3645 | |
| 4 | 715 | 4 | 459 | |
| 5 | 1287 | 3 | 42 | |
| 6 | 1716 | 3 | 10 | |
| 7 | 1716 | 3 | 6 | |
| 8 | 1287 | 4 | 2071 | |
| 9 | 715 | 3 | 14 | |
| 10 | 286 | 4 | 23 | |
| 11 | 78 | 3 | 0.04 | |
| 12 | 13 | 2 | 0.002 | |

**Canonical row `min_d(r)` for `r=2..12`:** `7,5,4,3,3,3,4,3,4,3,2`.

## Unions (`--skip-baseline --union-rs`)

| RS | total XOR splits | min_d | dp_sec (approx) |
|----|------------------|-------|-----------------|
| 2,3,4 | 1079 | 4 | 1532 |
| 2,3,4,5 | 2366 | 3 | 484 |
| 2..12 (all) | 8177 | 2 | 0.06 |

## Comparison to n=12 `{6,7}`

- n=12 `min_d(r)` for `r=2..11`: `6,4,3,4,2,4,3,4,3,2`.
- n=13 row is **not** prefix-monotone in `r` (e.g. `7→5→4→3` then `3,3,4,3,4,3,2`) — same qualitative behavior as n=12 (local non-monotonicity).
- **Unions:** n=12 had `r∈{2,3,4}→3`, `r∈{2..5}→3`, `r∈{2..11}→2`. Here `r∈{2,3,4}→4`, `r∈{2..5}→3`, `r∈{2..12}→2`.

## Hypothesis verdict

- **H1:** PASS.
- **H2:** PASS (full finite row; smallest `min_d` among single-arity is **2** at `r=12`).

## Operational note

Chaining several heavy shards in **one** shell loop caused **MemoryError** once (after `r=11,10,9` before `r=8`). **Re-running `r=8` alone** succeeded. Prefer **one `python` process per `r`** on large split counts.
