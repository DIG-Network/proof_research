# Notes

- **2026-04-01 (automation):** **`--lru-maxsize 0`**, **`--skip-baseline`**, **`--d-min 2 --d-max 2`** for **`r=2,3,4`** completes in **sub-second** to **few seconds** per **`r`** — prior **timeouts** were from **full** **`min_d`** scans probing **deeper** **`d`**, not from **`d=2`** in isolation.
- **Comparison to `n=13`:** Canonical row has **`min_d(2)=7`**, **`min_d(3)=5`**, **`min_d(4)=4`** — all **`>2`**; **`n=14`** **`r∈{2,3,4}`** **`d=2`** **false** is **consistent** with that pattern.
- **Next:** Heavy **`r=5` `d=3`**, **`r=9` `d=3`**, and **union** probes remain for a **large-RAM / long-wall** host; a **5 min** **`r=5` `d=3`** attempt here **timed out** (no feasibility line).
