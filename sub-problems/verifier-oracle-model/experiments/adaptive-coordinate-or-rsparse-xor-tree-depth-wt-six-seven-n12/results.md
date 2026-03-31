# Results: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12

**Outcome:** **PASS** — **full** **single-arity** **`min_d(r)`** **for** **`r=2..11`** **completed** **2026-03-31** **via** **fresh-process** **`--r-single r --skip-baseline`** **shards** **(** **peak** **RSS** **per** **shard** **only** **)** **.**

**Setup:** `n=12`, masks with **wt ∈ {6,7}** (**1716** **masks**). Majority **t=7**.

**Coord-only:** `min_d = 12` (`--baseline-only`).

**Coord + full 12-XOR:** `min_d = 1`.

**Single-arity** (`coord +` all **C(12,r)** **r-sparse** **XOR** **splits**), **timings** **from** **this** **host:**

| r | C(12,r) | min_d | dp_sec (approx) |
|---|---------|-------|-----------------|
| 2 | 66 | **6** | 126 |
| 3 | 220 | **4** | 70 |
| 4 | 495 | **3** | 5 |
| 5 | 792 | **4** | 393 |
| 6 | 924 | **2** | 0.03 |
| 7 | 792 | **4** | 313 |
| 8 | 495 | **3** | 4 |
| 9 | 220 | **4** | 8 |
| 10 | 66 | **3** | 0.01 |
| 11 | 12 | **2** | 0.001 |

**`min_d(r)`** **is** **not** **monotone** **:** **interior** **bumps** **at** **`r=5`** **(** **3→4** **)** **,** **`r=7`** **(** **2→4** **)** **,** **`r=9`** **(** **3→4** **)** **.** **Sharp** **drop** **at** **`r=6`** **(** **`min_d=2`** **,** **same** **as** **093** **pentuple** **spirit** **on** **`(10,{5,6})`** **)** **.**

**Unions** (`--union-rs`):

| Language | total splits | min_d |
|----------|--------------|-------|
| `r ∈ {2,3,4}` | 781 | **3** |
| `r ∈ {2,3,4,5}` | 1573 | **3** |
| `r ∈ {2,…,11}` | 4082 | **2** |

**Earlier** **OOM** **note** **(** **single** **process** **holding** **multiple** **large** **memos** **)** **:** **Standalone** **`r=5`** **/** **`r=7`** **still** **heavy** **(** **~6–7** **min** **DP** **each** **)** **but** **complete** **when** **run** **alone** **.** **Journal** **:** **partial** **PASS** **in** **`entries/2026-03-31-adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12.md`** **;** **completion** **in** **`entries/2026-03-31-adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12-r5-r7-resolved.md`** **.**

**Repro:** `python script.py --baseline-only`; then for each `r`: `python script.py --skip-baseline --r-single r`. Unions: `python script.py --skip-baseline --union-rs "2,3,4"` etc.
