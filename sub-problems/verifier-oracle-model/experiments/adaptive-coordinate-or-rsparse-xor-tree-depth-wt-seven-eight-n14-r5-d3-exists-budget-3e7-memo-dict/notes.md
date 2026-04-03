# Notes

- **Observation:** **`memo_dict_size` (12.3M) > `max_exists_calls` (30M)** is expected: each invocation increments the budget counter on entry, including memo hits; distinct stored states are fewer than total calls when the same key is revisited often.
- **Dead end (for this budget):** **30M** invocations are **insufficient** for a **`PASS`/`FAIL`** on **`d=3`** for **`r=5`** full menu under dict memo — same structural incompleteness as lower LRU budgets, not a “fast complete” regime.
- **Next step:** Retry with **larger** `--max-exists-calls` under **`--memo-dict`** (watch RAM — dict grows with distinct states); compare wall time per invocation to prior LRU **PARTIAL** at **300M** if feasible on host.
