# Notes

- Mirrors `…-n14-r5-d3-xor-partition-shard-scan-400` with `--r-single 9` only; XOR menu size still 2002.

- Prior `r=9` full-menu `5e7`/`8M` run: PARTIAL ~542 s (LRU at cap). This scan uses slightly higher per-shard exists cap (55M) like `r=5` shards to avoid PARTIAL within a slice.

- **Observation:** Every shard printed `exists_tree_cache_misses_after_d=3: 8000000` — LRU fully utilized per slice, same qualitative pattern as `r=5` shards.

- **Dead end (local):** Contiguous XOR sharding does not surface a `d=3` positive certificate for `r=9`; negatives still do not imply full-menu infeasibility.
