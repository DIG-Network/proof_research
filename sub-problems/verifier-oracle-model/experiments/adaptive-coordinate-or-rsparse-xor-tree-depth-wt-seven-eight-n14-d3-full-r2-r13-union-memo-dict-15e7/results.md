# Results

**Outcome:** PASS (journal) — **wrapper** `script.py` **exit** **0**

## What was run

- Parent: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`
- Flags: `--skip-baseline --full-r2-r13-union-only --d-min 3 --d-max 3 --memo-dict --lru-maxsize 0 --max-exists-calls 150000000 --progress-every 5000000 --log-rss`
- Language: coordinate splits on 14 bits **plus** the **union** of all `r`-sparse XOR partition menus for **`r = 2..13`** (**16368** XOR splits total).

## Measured outputs

| Quantity | Value |
|----------|-------|
| `min_d` | **3** |
| `d=3 feasible` | **True** |
| `dp_sec` (wall for the single `d=3` probe) | **~0.129** |
| `VmRSS_peak_kb` | **68408** |
| `exists_tree` invocations used | **well below** `1.5×10⁸` (no `PARTIAL`; no progress lines printed) |

## Interpretation

The **full** combined XOR menu (**all** arities **`r=2..13`**) is **strictly more expressive** than the **`r=5`** or **`r=9`** **single-arity** menus used in the long **`d=3`** shard / LRU studies. Under **`--memo-dict`**, the DP finds a **depth-3** refutation witness **immediately** for the **`{7,8}`** shell on **`n=14`**.

This **closes** the prior “**full-menu** **`d=3`** **still** **open**” item **in the sense of** the **union** language above; it does **not** contradict the **single-`r`** **`d=3 feasible=False`** **shard** **results** — those are **sub-languages**.
