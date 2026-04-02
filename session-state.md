# Session State

**Last updated:** 2026-04-02 ~15:15 UTC — **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-r9-d3-xor-step2-start1-1001-each-12e7-lru-8m`** **INCONCLUSIVE** (complementary **1001** XOR indices **`1,3,…,2001`**, **`r=5`** then **`r=9`**, **`12e7/8M`** each — both **PARTIAL** ~**976** s + ~**860** s DP, ~**30.6** min total; no `d=3` witness; coset swap does not unlock `d=3`).
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-r9-d3-xor-step2-start1-1001-each-12e7-lru-8m`
**Last outcome:** INCONCLUSIVE
**Current focus:** sub-problems/verifier-oracle-model (`n=14` **`{7,8}`** band — **`r=5`/`r=9`** **`d=3`** still **PARTIAL**; **both** parity **1001** XOR cosets **`0,2,…,2000`** and **`1,3,…,2001`** exhausted at **`12e7/8M`** without witness)
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** Increase **`exists_tree`** budget and/or LRU on a **larger** host, or change DP structure — **not** another XOR index coset at fixed **1001**/**12e7**/**8M**; **avoid** parallel **10M** LRU workers on memory-bounded agents.
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron session — optional)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled. Raw **`sqlite3`** on **`memory.db`** may lack **`vec0`** — use **`python3 tools/index_memory_db.py`**.
