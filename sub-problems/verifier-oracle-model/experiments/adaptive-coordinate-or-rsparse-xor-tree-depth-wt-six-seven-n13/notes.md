# Notes

- **Convention correction:** For `n=13` and majority `t=7`, the adjacent-shell slice matching the n=12 `(t−1,t)` pattern is **`|S| ∈ {6,7}`**, not `{7,8}` (the latter pairs with `t=8`, e.g. `n=14`). A separate experiment folder covers `{7,8}` on n=13 (`wt-seven-eight-n13`).
- **Compute:** Baseline was **much** faster than n=12’s coord-only (~minutes there); here ~27 s — likely fewer DP nodes at each depth for this mask family despite `|domain|=3432` vs 1716.
- **r=2:** Pair-XOR library gives `min_d=7` with ~22.6 min DP time dominated by d=6 and d=7.
- **r≥3:** Expect **much** longer runs (`C(13,3)=286` splits vs 78 for r=2). The script only prints a depth line **after** that depth completes, so long gaps with no output are normal.
- A background `foreach (r in 2..12)` was started; **r=2** finished; **r=3** was still in progress after ~1 h wall — do **not** rely on that job; rerun shards explicitly with `python -u` for auditable logs.
