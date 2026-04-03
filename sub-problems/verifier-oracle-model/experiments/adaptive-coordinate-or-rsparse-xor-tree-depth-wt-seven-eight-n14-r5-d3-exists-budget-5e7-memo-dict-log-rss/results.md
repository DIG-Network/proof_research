# Results

**Outcome:** INCONCLUSIVE (process **exit 247** — **SIGKILL** / **OOM** class on this host; not parent **PARTIAL** from **`max_exists_calls`**).

**Command:** `PYTHONUNBUFFERED=1 python3 -u sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-memo-dict-log-rss/script.py`

**Measured (progress every 2×10⁶ `exists_tree` invocations):**

| `exists_calls` | `memo_dict_size` | `VmRSS_kB` |
|-----------------|------------------|------------|
| 2×10⁶ | 1_202_997 | 1_185_624 |
| 4×10⁶ | 1_608_142 | 1_606_496 |
| 6×10⁶ | 2_796_134 | 2_719_256 |
| 8×10⁶ | 3_214_257 | 3_193_056 |
| 10×10⁶ | 4_376_847 | 4_282_056 |
| 12×10⁶ | 4_818_272 | 4_696_008 |
| 14×10⁶ | 5_959_741 | 5_928_992 |
| 16×10⁶ | 6_420_368 | 6_360_896 |
| 18×10⁶ | 7_535_656 | 7_405_544 |
| 20×10⁶ | 8_019_800 | 7_859_624 |
| 22×10⁶ | 9_109_931 | 8_880_776 |
| 24×10⁶ | 9_617_213 | 9_356_240 |
| 26×10⁶ | 10_683_971 | 10_355_480 |
| 28×10⁶ | 11_213_108 | 11_179_276 |
| 30×10⁶ | 12_256_531 | 12_156_604 |
| 32×10⁶ | 12_806_788 | 12_672_460 |
| 34×10⁶ | 13_827_483 | 13_628_140 |
| 36×10⁶ | 14_398_785 | 14_164_060 |
| 38×10⁶ | 15_397_596 | 15_084_100 |

**Wall time:** ~134 s until kill (no **`PARTIAL:`** line — kernel OOM before **5×10⁷** budget).

**Interpretation:** **`--memo-dict`** RSS scales roughly with distinct **`(bits, depth)`** keys; by **~3.8×10⁷** invocations resident memory is already **~15 GB** on this runner. Completing **5×10⁷** (or **10⁸**) on similar RAM without sharding / algorithm change is **not** viable here. The prior **3×10⁷** run finished in **~120 s** with **~12.3M** memo entries — consistent with the **30×10⁶** row above (~12.2M keys, ~12 GB RSS).

**Parent tooling added this session:** **`--log-rss`**, **`--progress-every K`** on `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`; wrapper uses **`python3 -u`** and **`PYTHONUNBUFFERED=1`** so progress lines appear under pipe/subprocess.
