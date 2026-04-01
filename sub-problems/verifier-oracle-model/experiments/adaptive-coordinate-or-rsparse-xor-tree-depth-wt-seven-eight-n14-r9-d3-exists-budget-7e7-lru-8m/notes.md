# Notes

- **observation:** At **7e7/8M**, **`r=9`** used **~595 s** vs **`r=5`** **~644 s** for the same budget — split-menu cardinality matches (**2002**) but DP geometry differs.
- **dead_end:** **7e7/8M** does **not** certify **`r=9` `d=3`** either; H1 falsified.
- **insight:** **`r=9`** marginal **6e7→7e7** wall delta **~33 s** (595 vs ~562) is **smaller** than **`r=5`** **~74 s** (644 vs ~569) — both paths show diminishing marginal cost for the extra 10M calls but remain LRU-capped.
