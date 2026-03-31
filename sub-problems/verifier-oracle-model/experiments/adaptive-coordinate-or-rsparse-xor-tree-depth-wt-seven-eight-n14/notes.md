# Notes — n=14 `{7,8}` sweep

- **6435 masks** (~2.14× **n=13** 3003). **Coord-only** to `d=14` is feasible in ~2.3 min; **full 14-XOR** still **`min_d=1`** (global parity lemma).
- **Heavy `r` first** (`r=13` down) was the right order: **`r=13→2`**, **`r=12→3`**, **`r=11→4`**, **`r=10→3`** quickly.
- **`r=9`** with **4M LRU** looked like **cache thrash** (high CPU, ~18+ min on a single `d` probe) — killed to free the slot.
- **`r=8`**, **`r=6`** each ~**400 s** DP; **`r=5`** did not finish in **40 min** on `d=3`.
- **`r=4`** stuck on **`d=3`** even with **unbounded LRU** for **15 min** — suggests **enormous** exact memo demand for that subproblem (not just LRU eviction).
- **Unions** **`{2,3,4}`** and **`{2..5}`** also hung on **`d=3`** with multi-hour timeouts — same “low-`r` menu blowup” as single **`r=2..4`**.
- **Hypothesis H2/H3** for the **full** row and **union** depths **not** adjudicated this session.
