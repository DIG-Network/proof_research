# Notes

- **compute:** One menu is ~**7×** slower than one **`r=6` `K=2`** menu (~**469 s** vs ~**110 s** on this host) because **`stratum_min_d2`** is **7630** vs **107800**—more **`md==2`** cells per menu. Full **1540** menus at **4** workers is ~**50 h** wall-clock order (see `results.md` estimate).
- **smoke:** Use **`MAX_MENUS=N`** for partial verification; full run omits **`MAX_MENUS`**.
- **question:** If full run shows **min=max=7630**, is there a short certificate for **2×3850−70** tied to **70** quads?
