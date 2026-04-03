# Session State

**Last updated:** 2026-04-03 — after **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-full-r2-r4-union-min-d`** **FAIL**
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-full-r2-r4-union-min-d`
**Last outcome:** FAIL (hypothesis `min_d=1` falsified; observed union **`min_d=2`**)
**Current focus:** sub-problems/verifier-oracle-model — **refine** **`n=5`** **story** **(** **`min_d`** **is** **shell-dependent** **)** **;** **optional** **ablations** **(** **which** **enlargement** **first** **forces** **`min_d=2`** **)**
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** **Optional:** **ablate** **`n=5`** **(** **`--shells`** **)** **—** **e.g.** **20** **masks** **but** **union** **only** **`r=2..3`** **,** **or** **10** **masks** **+** **`r=2..4`** **—** **to** **localize** **the** **`min_d`** **jump** **;** **or** **resume** **anonymous-quorum-binding**
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron tick)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled. Rebuild **`memory.db`** with **`python3 tools/index_memory_db.py --force`** after journal update.

**Parent tooling:** **`n=5`** driver **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py`** supports **`--shells`** **`2`** **(** **default** **)** **or** **`2,3`** **;** **wrappers** **call** **`--union-rs`** **as** **needed**.
