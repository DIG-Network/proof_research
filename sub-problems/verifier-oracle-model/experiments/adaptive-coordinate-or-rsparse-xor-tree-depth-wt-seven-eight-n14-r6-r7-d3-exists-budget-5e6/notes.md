# Notes

- **Non-monotonicity:** `r=7` uses **more** partition masks than `r=6` yet the DP finishes orders of magnitude faster—structure of feasible shallow trees matters more than raw split count.
- **Comparison to r=5 shard:** Same 5M cap; `r=5` and `r=6` behave alike; `r=7` diverges.
- **Next:** If chasing `r=5`/`r=6` **`d=3`**, still need **unbounded memo**, **sharding**, or **new pruning**—this experiment does not resolve that, only maps **which `r`** are **easy vs hard** under a fixed budget.
