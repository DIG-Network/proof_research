# Session State

**Last updated:** 2026-04-03 — after **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-memo-dict-log-rss`** **INCONCLUSIVE** (**exit 247** **~134 s**, **~3.8×10⁷** **`exists_calls`**, **`VmRSS` ~15 GB**)
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-memo-dict-log-rss`
**Last outcome:** INCONCLUSIVE (exit **247** — OOM/SIGKILL before **5×10⁷** budget; progress table in **`results.md`**)
**Current focus:** sub-problems/verifier-oracle-model — **`n=14`**, **`{7,8}`**, **`r=5`**, **`d=3`** full **2002** menu; **dict** path needs **sharding** or **≥~20 GB** RAM for **5×10⁷+** invocations (RSS ~ tracks **`memo_dict_size`**)
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** Continue **`d=3`** line with **XOR half-shards** or **LRU-capped** budgets; for **`--memo-dict`** runs use **`--progress-every`** (and **`python3 -u`**) so OOM vs **PARTIAL** is obvious — avoid raw **5×10⁷–10⁸** dict on **~15 GB** hosts.
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron session)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled. Rebuild **`memory.db`** with **`python3 tools/index_memory_db.py --force`** after journal update.

**Parent tooling:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` now supports **`--log-rss`**, **`--progress-every K`**.
