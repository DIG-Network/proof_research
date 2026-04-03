# Notes

- **observation:** Baseline `coord_only` hits `min_d=5` on the 20-mask shell (all five coordinates needed before pure subsets appear), while `coord+full_5xor` collapses to `min_d=1` immediately.
- **insight:** The jump from **`min_d=1`** (10 masks, `r=2..3` union) to **`min_d=2`** (20 masks, `r=2..4` union) isolates **shell cardinality / mixed weights** as the trigger, not `n` alone.
- **question:** Is there a **minimal** superset of the 10 weight-2 masks for which the `r=2..3` union already forces `min_d=2`, or does one need weight-3 (or `r=4`) to see the jump?
- **dead_end:** Treating “`n=5` always has `min_d=1` for natural XOR unions” as a global statement — **ruled out** by this run.
