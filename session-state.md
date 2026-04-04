# Session State

**Last updated:** 2026-04-04 — experiment **144** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-triple-r3-scan-all-triples` (FAIL: **`6545/6545`** triples **`witness_min_d2_count=0`**, **`min_d=3`** throughout; **~18** s wall, **`4M`** LRU)
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-triple-r3-scan-all-triples`
**Last outcome:** FAIL
**Current focus:** sub-problems/verifier-oracle-model — **n=7** **`{2,3}`**: **two** and **three** fixed **`r=3`** splits **+** full **`r=2`** **do not** yield **`min_d=2`**; next: **four** triples **`C(35,4)=52360`**, **minimal** **`k`** for **`min_d=2`**, or **partial** **`r=2..3`** unions; anonymous-quorum-binding ladder
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** Either **sample** or **shard** **`C(35,4)`** four-triple scan for **`min_d=2`** witnesses, or run **binary search** on **`k`** (**subset** of **`r=3`** splits) with full **`r=2`** fixed to find **smallest** **`k`** achieving **`min_d=2`** at **n=7** (if any **< 35**)
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none (after push)
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron automation — experiment 144)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled.

**Vector memory:** Rebuild with `python3 tools/index_memory_db.py --force` after journal/index update for experiment **144**.

**Branch sync:** Local **`main`** tracks **`origin/main`** after pull; new work committed on **`main`**.
