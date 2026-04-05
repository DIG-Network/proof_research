# Results — diagonal complement biconditional (n=7 doubleton grid)

**Outcome:** PASS

**Grid:** `35 × 35 = 1225` cells (duplicate triple `T_i` on both `r=3` slots, all quartics `Q`).

**Counts:** `min_d=2` on exactly `35` cells; predicate `Q = [7] \ T_i` hits exactly `35`; `0` violations either direction.

**Timing:** `wall_sec ≈ 1.684`, LRU cap `4_000_000`.

**Conclusion:** The diagonal slice of the doubleton-triple + singleton-quartic language obeys the same **complement** certificate as the singleton-triple menu: depth `2` iff the quartic is the complement of the triple.
