# Results

**Outcome:** INCONCLUSIVE (wrapper exit **2**).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR, `d=3`-only, **two contiguous half-shards** of the 2002-split menu: `[0:1001)` and `[1001:2002)`, each **`--max-exists-calls 120000000`**, **`--lru-maxsize 10000000`**, `--skip-baseline`.

**Shard 0 (`0:1001`):** **1001** partitions; DP hit budget after **~1034.04 s**; LRU at cap **10M**; parent reported `d=3 feasible=False` at exhaustion (exit **2** PARTIAL).

**Shard 1 (`1001:2002`):** **1001** partitions; DP hit budget after **~992.20 s**; LRU at cap **10M**; same PARTIAL pattern.

**Build times:** shard0 **~4.06 s**, shard1 **~4.12 s** (mask / partition prep).

**Total wall:** ~**35.3 min** for both halves sequentially (**~2121 s** end-to-end including subprocess overhead).

**Interpretation:** Doubling per-half budget from **6×10⁷** to **1.2×10⁸** did **not** complete either half: both still **PARTIAL** at the cap. This **does not** decide full **2002**-split `d=3` feasibility; it shows **each** half alone needs **>** **1.2×10⁸** `exists_tree` invocations (at **10M** LRU) to escape PARTIAL—consistent with full-menu **12e7** run also PARTIAL ~**965 s** (single process, different sharding). **No** `d=3 feasible=True` witness on either half.
