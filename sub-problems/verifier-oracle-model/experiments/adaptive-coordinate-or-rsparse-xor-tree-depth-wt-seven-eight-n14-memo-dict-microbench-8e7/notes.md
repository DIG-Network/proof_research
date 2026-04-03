## Observations

- Budget counter matches **`lru_cache`**: increment **before** memo lookup so hits count as invocations (apples-to-apples with prior experiments).
- **Unbounded LRU** (`--lru-maxsize 0`) at **8M** budget: **~62 s**, **currsize 7999997** — same class as capped **10M** LRU for this cutoff (cache near full either way).

## Next steps

- Re-run **`r=5`**, **`d=3`**, **30e7** (or higher) with **`--memo-dict`** on a host with sufficient RAM; expect **much lower** wall per invocation than **10M** LRU **30e7** (~2616 s).
- Optionally mirror for **`r=9`** once **`r=5`** completes.
