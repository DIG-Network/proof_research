# Notes

- **Convention correction:** For `n=13` and majority `t=7`, the adjacent-shell slice matching the n=12 `(t−1,t)` pattern is **`|S| ∈ {6,7}`**, not `{7,8}` (the latter pairs with `t=8`, e.g. `n=14`). A separate experiment folder covers `{7,8}` on n=13 (`wt-seven-eight-n13`).
- **Shard order:** High **`r`** first (**`C(13,r)`** small) fills the table quickly; **`r=2`** and **`r=3`** dominate wall time (~23 min and ~61 min DP).
- **Memory:** A **PowerShell loop** running **`r=11,10,9,8`** in one session hit **MemoryError** entering **`r=8`**. **Isolated** **`r=8`** run (~35 min DP) completed — avoid long **back-to-back** heavy processes in one loop on this host, or run **`r=8+`** alone after a pause.
- **`python -u`** gives line-buffered per-depth progress (recommended).
