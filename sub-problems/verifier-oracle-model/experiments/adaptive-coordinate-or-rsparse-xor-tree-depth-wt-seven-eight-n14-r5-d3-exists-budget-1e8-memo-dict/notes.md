# Notes

- Pre-run: extrapolated DP wall from **3×10⁷** **~112.5 s** × **(10⁸/3×10⁷) ≈ 3.33** → **~375 s** order-of-magnitude if per-call cost stable; actual may differ as dict grows.
- **Dead end (host):** Full-menu **`10⁸`** **`--memo-dict`** run **SIGKILL** (**exit 247**) after **~3.35 h** with **no** **`PARTIAL:`** — same failure class as prior heavy-memo probes; do **not** repeat **10⁸** dict on this envelope without more RAM or sharding.
- **Observation:** **`3×10⁷`** dict (**~12.26M** entries) completed in **~112 s**; **10⁸** did not complete — memory growth outran the budget window here.
