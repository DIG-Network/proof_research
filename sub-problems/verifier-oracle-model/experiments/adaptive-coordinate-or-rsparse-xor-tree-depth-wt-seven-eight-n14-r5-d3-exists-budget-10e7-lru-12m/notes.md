# Notes

- **observation:** Exit **247** with only `probing d=3 …` matches prior **12M** LRU **OOM** signature (**75e6/12m** journal entry).
- **dead_end (host-local):** **12M** LRU is not a safe knob on this environment for **r=5** **d=3** at **10e7** — use **≤10M** LRU, unbounded memo on larger RAM, sharding, or algorithmic change.
- **question:** Does **r=9** show the same **12M** kill? (paired experiment folder.)
