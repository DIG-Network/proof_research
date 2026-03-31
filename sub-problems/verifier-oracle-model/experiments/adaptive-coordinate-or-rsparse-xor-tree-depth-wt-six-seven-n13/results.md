# Outcome: INCONCLUSIVE (partial single-arity row)

## Baseline (`--baseline-only`): PASS

- **Domain:** `n=13`, `|S| ∈ {6,7}`, `|masks| = C(13,6)+C(13,7) = 3432`, majority `t=7`.
- **coord-only:** `min_d = 13` (needs full depth `d_max=n`).
- **coord + full 13-XOR:** `min_d = 1`.
- **Wall time (one run):** ~27 s total for baseline (coord sweep + full XOR).

## Single-arity shards (`--skip-baseline --r-single r`)

| r | XOR splits | min_d | dp_sec (total) | Status |
|---|------------|-------|----------------|--------|
| 2 | 78 | 7 | 1355.55 | DONE |
| 3..12 | — | — | — | Not finished this session |

**r=2 per-depth times (sec):** d1 0.0003, d2 0.014, d3 0.42, d4 6.10, d5 67.26, d6 585.32, d7 692.50.

## Comparison to n=12 same slice

- n=12 `{6,7}`: `min_d(2)=6`; here `min_d(2)=7` (consistent with larger `n` / deeper coord-only barrier).
- Full `min_d(r)` row for n=12: `6,4,3,4,2,4,3,4,3,2` for r=2..11.

## Hypothesis verdict

- **H1 (baseline):** PASS.
- **H2 (existence of cheap r):** Partially supported (`r=2` gives finite `min_d=7`); full row **not** computed.

## Next steps

- Finish `r=3..12` in **separate processes** (same pattern as n=12):  
  `python -u script.py --skip-baseline --r-single R`  
  (`-u` recommended so each **d** line appears as soon as that depth finishes.)
- Then run union probes (`--union-rs`) if the full row completes.
