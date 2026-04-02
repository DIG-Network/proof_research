# Session State

**Last updated:** 2026-04-02 ~11:15 UTC — **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-12e7-each-lru-8m`** **INCONCLUSIVE** (both XOR halves **PARTIAL** at **12e7/8M**, ~**974** s + ~**912** s DP, ~**32.6** min sequential). **Paired** **`r=5`** **12e7/8M** halves ~**1853** s aggregate; **`r=9`** ~**1886** s (**~2%** slower total despite **`r=9`** often faster on **full** 2002).
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-12e7-each-lru-8m`
**Last outcome:** INCONCLUSIVE
**Current focus:** sub-problems/verifier-oracle-model (`n=14` **`{7,8}`** band — **`r=5`/`r=9`** **`d=3`** still **PARTIAL** on full **2002** and on **12e7/8M** contiguous half-shards; **`r=3`** **closed** **`d=3`** **False**)
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** Try **non-contiguous** **1001**-wide XOR sub-menus for **`d=3`** witness hunt, or **raise** per-half **`exists_tree`** budget beyond **12e7** only if host memory allows; **avoid** parallel **10M** LRU workers on memory-bounded agents.
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron session — optional)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled. Raw **`sqlite3`** on **`memory.db`** may lack **`vec0`** — use **`python3 tools/index_memory_db.py`**.
