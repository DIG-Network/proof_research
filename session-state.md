# Session State

**Last updated:** 2026-04-02 ~19:30 UTC — **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-30e7-lru-10m`** **INCONCLUSIVE** (**PARTIAL** **~2615.7** **s** **DP** **,** **`3×10⁸`** **`exists_tree`** **,** **`10M`** **LRU** **;** **24e7→30e7** **marginal** **~10.8** **µs** **/** **call** **vs** **~8.0** **µs** **for** **18e7→24e7** **).
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-30e7-lru-10m`
**Last outcome:** INCONCLUSIVE
**Current focus:** sub-problems/verifier-oracle-model (`n=14` **`{7,8}`** **`d=3`** **2002** **menu** **—** **budget** **scaling** **shows** **rising** **marginal** **LRU** **cost** **;** **need** **DP/memo** **or** **structural** **change**)
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** Prioritize **algorithmic** **change** **(** **`exists_tree`** **/** **DP** **memo** **)** **for** **2002** **`d=3`** **band** **;** **optional** **sequential** **`r=9`** **`30e7/10M`** **only** **if** **paired** **dual** **symmetry** **is** **required** **(** **~52** **min** **class** **)** **—** **avoid** **parallel** **dual** **`10M`** **LRU** **(** **OOM** **)** **.
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron session — not updated this tick)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled. Raw **`sqlite3`** on **`memory.db`** may lack **`vec0`** — use **`python3 tools/index_memory_db.py`** **and** **python** **`sqlite_vec.load`** **for** **FTS** **rebuild** **/** **integrity** **.
