# Notes

- **Sharding:** **`python3 -u script.py --skip-baseline --r-single R`** per **`R`**; heaviest wall time varies by host and **`--lru-maxsize`** (unbounded vs LRU 4M).
- **Structural:** **`min_d(r)`** row and **union** depths **coincide** with **`(n=13,{6,7})`** (**`…-six-seven-n13-resolved`**) even though **`|domain|`** differs (**3003** vs **3432**).
- **OOM / SIGKILL:** Unbounded **`lru_cache`** on **`r=2`** hit **exit 137** on one constrained host; **default** **`--lru-maxsize 4_000_000`** completes but **`r=2` / `r=3`** can take **order hours** of DP wall time there.
- **Script:** optional **`--lru-maxsize`**, per-depth **`probing d=…`**, and **`flush=True`** on prints for long-run visibility.
