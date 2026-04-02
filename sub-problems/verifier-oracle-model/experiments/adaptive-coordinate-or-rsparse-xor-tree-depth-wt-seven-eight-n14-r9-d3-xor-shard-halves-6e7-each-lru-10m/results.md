# Results

**Outcome:** INCONCLUSIVE (wrapper exit **2**).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR, `d=3`-only, **two contiguous half-shards** of the 2002-split menu: `[0:1001)` and `[1001:2002)`, each **`--max-exists-calls 60000000`**, **`--lru-maxsize 10000000`**, `--skip-baseline`.

**Shard 0 (`0:1001`):** **1001** partitions; DP hit budget after **~509.06 s**; LRU at cap **10M**; reported `d=3 feasible=False` at exhaustion (parent exit **2** PARTIAL).

**Shard 1 (`1001:2002`):** **1001** partitions; DP hit budget after **~478.77 s**; LRU at cap **10M**; same PARTIAL pattern.

**Total wall:** ~**16.3 min** for both halves sequentially.

**Interpretation:** Neither half produced a **`d=3 feasible=True`** witness under **6×10⁷** `exists_tree` per half. This does **not** decide the full **2002**-split `d=3` question; it only shows these **50%** sub-menus did not resolve within this per-shard budget (compare full-menu **12e7** runs ~**965 s** for `r=9`).
