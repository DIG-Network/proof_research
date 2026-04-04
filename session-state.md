# Session State

**Last updated:** 2026-04-04 — experiment **145** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quadruple-r3-scan-all-quadruples` (FAIL: **`52360/52360`** quads **`witness_min_d2_count=0`**, **`min_d=3`** throughout; **~132** s wall, **`4M`** LRU)
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quadruple-r3-scan-all-quadruples`
**Last outcome:** FAIL
**Current focus:** sub-problems/verifier-oracle-model — **n=7** **`{2,3}`**: **two** through **four** fixed **`r=3`** splits **+** full **`r=2`** **do not** yield **`min_d=2`**; next: **`C(35,5)=324632`** **five**-triple scan (**~** **25×** **quad** cost) **or** **partial** **`r=2..3`** unions / **minimal** **`k`** search; anonymous-quorum-binding ladder
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** Decide whether to run **exhaustive** **`C(35,5)`** **five**-triple scan (**long** wall **~** **hours** at **~** **2.5 ms**/quad scaling), **sample** a **random** **subset** first, or pivot to **binary search** on **`k`** (**subset** of **`r=3`** **with** **full** **`r=2`** fixed) **before** **full** **`C(35,5)`**
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none (after push)
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron automation — experiment 145)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled.

**Vector memory:** Rebuild with `python3 tools/index_memory_db.py --force` after journal/index update for experiment **145**.

**Branch sync:** Local **`main`** tracks **`origin/main`** after pull; new work committed on **`main`**.
