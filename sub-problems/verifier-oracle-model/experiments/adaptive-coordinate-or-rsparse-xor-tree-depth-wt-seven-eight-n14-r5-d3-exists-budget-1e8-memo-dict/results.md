# Results

**Outcome:** INCONCLUSIVE (subprocess exit **247** — host **SIGKILL** / OOM class; **no** `PARTIAL:` line and **no** `feasible=` line).

**Command:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-1e8-memo-dict/script.py`

**Measured:**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` | 100_000_000 |
| Memo | `--memo-dict` (unbounded dict) |
| Wall time (observed) | ~12_086 s (~3.35 h) from shell session metadata |
| Terminal exit | **247** |
| `PARTIAL:` / `memo_dict_size` | **not** emitted — process killed mid-`d=3` probe |

**Interpretation:** **`10⁸`** **`exists_tree`** under **`--memo-dict`** is **not** a safe next step on this host: the run was terminated before the parent could print its budget-exhaustion **`PARTIAL:`** footer, matching prior **OOM/SIGKILL** class outcomes for heavy memo on this track (e.g. digest rows for **`10e7/12M` LRU** and **`1e8/16M` LRU**). The **3×10⁷** dict run (**~12.3M** entries, **~112 s** DP) remains the largest **completed** **`--memo-dict`** datapoint for this menu.

**Next:** Prefer **smaller** dict budgets with **external** timing/RSS sampling, or **3×10⁷**-scale shards / algorithmic changes — not a blind **10⁸** full-menu dict push without more RAM.
