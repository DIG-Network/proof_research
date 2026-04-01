# Notes

- The counter is implemented by incrementing **before** the body of `exists_tree` (wrapped in `lru_cache`), so it counts **every recursive call attempt**, including cache hits — a convenient proxy for “DP work units” when diagnosing blow-up.
- **LRU currsize ≈ K−3** at cutoff suggests almost all calls are **misses** near the exploration frontier for this budget (hits are rare once the cache is large).
- For cross-host comparison, prefer reporting **K / wall_seconds** rather than raw time alone when comparing partial runs.
- Next steps unchanged from `session-state`: full `d=3` decision still needs **overnight / large-RAM / sharding** or a **different** search structure — this experiment only **quantifies** how tiny **5×10⁶** is relative to that need.
