# Session State

**Last updated:** 2026-04-03 — after **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5-shell2-union-r2-r4-min-d`** **PASS**
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5-shell2-union-r2-r4-min-d`
**Last outcome:** PASS (**`n=5`**, **`{2}`** shell **10** masks, union **`r=2..4`** **25** splits → **`min_d=1`**; **`r=4`** alone does not explain **`min_d=2`** at **`{2,3}`** shell)
**Current focus:** sub-problems/verifier-oracle-model — **optional** **`{2,3}`** **+** **union** **`r=2..3`** **only** **(** **does** **weight-3** **force** **`min_d=2`** **without** **`r=4`** **?** **)**
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** **Optional:** run **`n=5`** parent **`--shells 2,3 --union-rs 2,3`** **(** **not** **`2,3,4`** **)** **with** **wrapper** **/** **journal** **if** **worth** **pinning** **;** **or** **resume** **anonymous-quorum-binding**
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron tick)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled. Rebuild **`memory.db`** with **`python3 tools/index_memory_db.py --force`** after journal update.

**Parent tooling:** **`n=5`** driver **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py`** supports **`--shells`** **`2`** **(** **default** **)** **or** **`2,3`** **;** **wrappers** **call** **`--union-rs`** **as** **needed**.
