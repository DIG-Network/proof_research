# Notes

- **compute:** One menu is ~**7×** slower than one **`r=6` `K=2`** menu (~**469 s** vs ~**110 s** on this host) because **`stratum_min_d2`** is **7630** vs **107800**—more **`md==2`** cells per menu. Full **1540** menus at **4** workers is ~**50 h** wall-clock order (see `results.md` estimate).
- **smoke:** Use **`MAX_MENUS=N`** for partial verification; optional **`MENU_START=S`** skips the first *S* menus in `combinations` order (default **0**). Example: **`MENU_START=2 MAX_MENUS=4`** runs menus **3–6** — 2026-04-06 batch all **`stratum_min_d2=7630`** (see `results.md`). **`MENU_START=42 MAX_MENUS=4`** (2026-04-06): **`(0,43)…(0,46)`** all **`7630`**, wall ~**445 s** (**`WORKERS=2`**). **`MENU_START=46 MAX_MENUS=4`** (2026-04-06): **`(0,47)…(0,50)`** all **`7630`**, wall ~**413 s** (**`WORKERS=2`**).
- **full run:** Omit **`MAX_MENUS`** (and usually **`MENU_START=0`**).
- **question:** If full run shows **min=max=7630**, is there a short certificate for **2×3850−70** tied to **70** quads?
