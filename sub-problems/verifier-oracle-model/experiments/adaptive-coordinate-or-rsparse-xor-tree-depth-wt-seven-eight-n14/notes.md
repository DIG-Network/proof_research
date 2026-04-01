# Notes — n=14 `{7,8}` sweep

- **6435 masks** (~2.14× **n=13** 3003). **Coord-only** to `d=14` is feasible in ~2.3 min; **full 14-XOR** still **`min_d=1`** (global parity lemma).
- **Heavy `r` first** (`r=13` down) was the right order: **`r=13→2`**, **`r=12→3`**, **`r=11→4`**, **`r=10→3`** quickly.
- **`r=9`:** **4M LRU** looked like **cache thrash** (high CPU, ~18+ min on **`d=3`**) — killed earlier. **Follow-up** on **~15 GiB** with **`--lru-maxsize 0`:** **`timeout 1200`** still **stuck on `d=3`**. **Narrow probe** **`--d-min 3 --d-max 3`** (**skip** recomputing **`d=1,2`**) + **`timeout 5400` (90 min)** — still **no** **`d=3`** line (**exit 124**). **Script** now supports **`--d-min` / `--d-max`** for these shards (**baseline** still always probes **`d=1..n`**).
- **`r=8`**, **`r=6`** each ~**400 s** DP; **`r=5`:** **`d=2`** **ruled out** in **~17 s** (**`--d-min 2 --d-max 2`**, **`lru-maxsize 0`**, 2026-04-01) — **`d=3`** still **hit** **40 min** **timeout** in **earlier** run.
- **`r=4`** stuck on **`d=3`** even with **unbounded LRU** for **15 min** — suggests **enormous** exact memo demand for that subproblem (not just LRU eviction).
- **Unions** **`{2,3,4}`** and **`{2..5}`** also hung on **`d=3`** with multi-hour timeouts — same “low-`r` menu blowup” as single **`r=2..4`**.
- **Hypothesis H2/H3** for the **full** row and **union** depths **not** adjudicated this session.
