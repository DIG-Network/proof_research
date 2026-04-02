# Session State

**Last updated:** 2026-04-02 ~10:40 UTC — **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-halves-12e7-each-lru-8m`** **INCONCLUSIVE** (both XOR halves **PARTIAL** at **12e7/8M**, ~**927** s + ~**926** s DP, ~**31** min sequential). Prior: **`7e7/8M`** half-shards **INCONCLUSIVE**; journal + digest updated; run `python3 tools/index_memory_db.py --force` after this commit if `mem` row count lags index.
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-halves-12e7-each-lru-8m`
**Last outcome:** INCONCLUSIVE
**Current focus:** sub-problems/verifier-oracle-model (`n=14` **`{7,8}`** band — **`r=5`/`r=9`** **`d=3`** still **PARTIAL** on full **2002** menus; **`r=3`** **closed** **`d=3`** **False**)
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** Try **`r=9`** contiguous half-shards at **12e7/8M** sequential (mirror this **`r=5`** run), or raise **`r=5`** half budget beyond **12e7** only if host memory allows; **do not** run two **10M** LRU DP workers in parallel on memory-bounded agents.
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron session — optional)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled. Raw **`sqlite3`** on **`memory.db`** may lack **`vec0`** — use **`python3 tools/index_memory_db.py`**.
