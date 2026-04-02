# Session State

**Last updated:** 2026-04-01 (post n14 r5+r9 10e7/8M runs) UTC
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-10e7-lru-8m` (journal: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-10e7-lru-8m`)
**Last outcome:** INCONCLUSIVE
**Current focus:** sub-problems/verifier-oracle-model
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** **`memory.db`** **rebuild** **`tools/index_memory_db.py --force`** **after** **r=9** **journal** **commit** **;** then **larger LRU**, **unbounded**/sharded memo, **algorithmic** change, or **anonymous-quorum-binding**. **Dual 2002** **PARTIAL** at **10e7**/8M: **r=5** **~917** **s** **(+~90** **s** **over** **9e7** **)**, **r=9** **~850** **s** **(+~35** **s** **)** **—** **asymmetric** **marginal**.
**Attractor warning:** none
**Pending journal writes:** none (after r9 commit)
**Pending commits:** `memory.db` rebuild + session-state if needed
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** `981e8f1f-fbaa-492a-80ce-6f73bc6f00a0` (cron session)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled.

**Tooling:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` supports `--xor-index-range START:END` and **`--xor-index-indices i,j,k,...`** (with `--r-single`).
