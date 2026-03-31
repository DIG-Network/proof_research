# Results: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12

**Outcome:** PASS (full **single-arity** table **partial** — see **OOM** note for **r∈{5,7}**; **union** languages **complete**)

**Setup:** `n=12`, domain = masks with Hamming weight in `{6,7}` (`C(12,6)+C(12,7)=1716`). Majority `t=7`: weight 6 = one below quorum, weight 7 = quorum (same *shell roles* as `(11,{5,6})` and `(10,{5,6})`, larger ambient `n`).

**Coord-only:** `min_d = 12` (from `--baseline-only`).

**Coord + full 12-bit XOR (global Hamming parity):** `min_d = 1` (adjacent-shell lemma, same pattern as **092**/**094**).

**Single-arity r-sparse XOR** (`coord + all C(12,r)` splits), **standalone** runs (`--skip-baseline --r-single r`):

| r | C(12,r) | min_d | Notes |
|---|---------|-------|--------|
| 2 | 66 | **6** | |
| 3 | 220 | **4** | |
| 4 | 495 | **3** | |
| 5 | 792 | **(OOM)** | Python process **killed** (exit 137) after ~3 min — DP memo footprint too large for this host |
| 6 | 924 | **2** | |
| 7 | 792 | **(OOM)** | Same as r=5 |
| 8 | 495 | **3** | |
| 9 | 220 | **4** | |
| 10 | 66 | **3** | |
| 11 | 12 | **2** | |

**`min_d(r)`** is **not monotone** in `r` (e.g. **r=11** gives **2** while **r=10** gives **3**; **r=8** beats **r=9**). **Unlike `(10,{5,6})` (099)** we did **not** observe a clean **`min_d(6),min_d(7) > min_d(5)`** **regression** in the **available** rows — **r=6** is already **2** (compare **099:** **`r=5→2`**, **`r=6,7→3`**).

**Unions** (`--skip-baseline --union-rs`, one DP per invocation — **avoids** retaining **multiple** huge single-arity memos):

| Language | total splits | min_d |
|----------|--------------|-------|
| `r ∈ {2,3,4}` | 781 | **3** |
| `r ∈ {2,3,4,5}` | 1573 | **3** |
| `r ∈ {5,6}` | 1716 | **2** |
| `r ∈ {6,7}` | 1716 | **2** |
| `r ∈ {2,3,4,6,8,9,10,11}` (all except **5,7**) | 2498 | **2** |
| `r ∈ {2,…,11}` (full) | 4082 | **2** |

**Interpretation:** Even without **standalone** **r=5**/**r=7** **certificates**, **coord + union of all nontrivial sparse parities** still reaches **`min_d = 2`** on this **1716-mask** domain (same **union** **depth** as **`n=11`** **`{5,6}`** **row**).

**Script:** `script.py`. **Modes:** full sweep; `--baseline-only`; `--r-single R`; `--union-rs "2,3,4"`; `--skip-baseline` for shard runs.

**Repro:** Baseline: `python3 script.py --baseline-only`. Shard single-arity: e.g. `python3 script.py --skip-baseline --r-single 6`. Full sweep **without** sharding **OOM**’d on this environment (prior run killed after ~400 s).

**Follow-up (2026-03-31, automation host):** Re-ran `python3 script.py --skip-baseline --r-single 5` and `--r-single 7` in fresh processes. Both were **killed (exit 137)** after **~200–210 s** wall time — **no change** to the **OOM** conclusion for standalone **`r=5`** / **`r=7`** on this cgroup. Journal: `research-journal/entries/2026-03-31-adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12-rerun-r5-r7.md`.
