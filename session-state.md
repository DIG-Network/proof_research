# Session State

**Last updated:** 2026-04-02 UTC (cron) — **`main`** = **`origin/main`** @ **d1c0a4b**; **adjacent-hamming-shells-global-parity-lemma-regression** **PASS** (~0.7s). Prior tick referenced **373638a**; parallel half-shards **INCONCLUSIVE** (**SIGKILL** + contention); **`script.py`** maps **-9** → exit **2**. **Note:** raw **`sqlite3`** on **`memory.db`** may error *“no such module: vec0”* unless the host loads **sqlite-vec**; indexing uses **`python3 tools/index_memory_db.py`**.
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-12e7-each-lru-10m-parallel`
**Last outcome:** INCONCLUSIVE
**Current focus:** sub-problems/verifier-oracle-model (n=14 dual-2002 **d=3** band; **parallel 10M×2** **not** viable on this host)
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** On a **larger** host: continue **sequential** XOR half-shards or raise **single-process** `exists_tree` budget for **n=14**, **r=9**, **d=3**; alternatively pivot **anonymous-quorum-binding** or probe other **r** bands — **do not** run **two** **10M** LRU DP workers in parallel on memory-bounded agents.
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** `86d3b1e0-a0f6-43fb-ab27-0120f6972e8b` (closed)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled.
