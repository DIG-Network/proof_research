# Notes — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-random-sample-200`

- **observation:** Wall time **~0.5 s** for **200** quintuples at **`4M`** LRU — scaling suggests **full** **`C(35,5)=324632`** exhaustive scan might be **~** **12–15 min** if per-quint cost stays similar (rough linear extrapolation from this sample).
- **dead_end:** None — random **FAIL** does **not** close the **`C(35,5)`** universe.
- **question:** Does **every** quintuple yield **`min_d=3`** (parallel to exhaustive quad/triple/pair scans), or do **`min_d=2`** witnesses exist only outside this **`200/324632`** draw?
- **next:** Run **exhaustive** **`C(35,5)`** scan **or** increase **`SAMPLE_QUINTS`** / change **seed** if we want stronger sampling evidence before **~** **10⁵+** DP evaluations.
