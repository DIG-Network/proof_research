# Notes — sextuple `r=3` scan at `n=7`

- **observation:** Wall time ~61 min for 1.62M DP runs at `lru_maxsize=4M`; ~2.25 ms per sextuple amortized (includes Python loop + `min_depth_for_language`).
- **dead_end:** For this language family (`coord` + full `r=2` + k distinct `r=3` triple parities), **k = 1..6** are now **fully** enumerated at `n=7` along the arity ladder; **no** `min_d=2` witness through **six** triple parities.
- **insight:** Union-style menus (`--union-rs` including full `r=4`) already gave `min_d=2` with 91 splits; sparse triple ladders are a **different** regime — extra triple parities do not substitute for higher-arity XOR menus at this slice.
- **question:** Does **any** arity-7 subset of triple parities (`C(35,7)` ≈ 6.7M) ever hit `min_d=2`, or is the obstruction already complete at six? (Cost scales ~4× this run.)
