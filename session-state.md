# Session State

**Last updated:** 2026-04-02 09:05 UTC — **`main`** synced **`origin/main`** @ **`a06386b`** then **new** experiment **PASS** (**`n=14` `r=3` `d=3` ⇒ False** at **5e7/8M**, ~82 s DP); **`memory.db`** rebuilt via **`python3 tools/index_memory_db.py --force`**.
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r3-d3-exists-budget-5e7-lru-8m`
**Last outcome:** PASS
**Current focus:** sub-problems/verifier-oracle-model (`n=14` **`{7,8}`** band — **`r=5`/`r=9` `d=3`** still **PARTIAL**; **`r=3`** now **closed** at **`d=3`**)
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** On a **larger** host: continue **sequential** XOR half-shards or raise **`exists_tree`** budget for **`n=14` `r∈{5,9}` `d=3`**; optionally run **`r=3` `d=4`-only** to pin **`min_d(3)`**; **do not** run **two** **10M** LRU DP workers in parallel on memory-bounded agents.
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron session — no new open run)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled. Raw **`sqlite3`** on **`memory.db`** may lack **`vec0`** — use **`python3 tools/index_memory_db.py`**.
