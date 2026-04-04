# Session State

**Last updated:** 2026-04-04 — experiment **137** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-min-r3-splits-for-min-d2` (FAIL: hypothesis minimal `r=3` count ≥ 2; **witness `k=1`**, triple index **`0`** **`(0,1,2)`** with full **`r=2`** → **`min_d=2`**, **`11`** splits)
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-min-r3-splits-for-min-d2`
**Last outcome:** FAIL (falsified: single triple XOR split suffices vs pair-only `min_d=3`)
**Current focus:** sub-problems/verifier-oracle-model — optional: classify which of the **10** singleton triples yield `min_d=2`; anonymous-quorum-binding **n=92** joint-min-max still queued if resources allow
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** Optional verifier-oracle follow-up: enumerate **all** singleton **`r=3`** indices under full **`r=2`** (10 runs) to see witness set size; or resume **n=92** quorum-binding probe when disk/time allows
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none (after push)
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron automation — experiment 137)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled.

**Vector memory:** Rebuilt with `python3 tools/index_memory_db.py --force` after journal/index update for experiment **137**.

**Parent change:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py` now supports **`--union-r3-indices`** (subset of **`C(n,3)`** triple-XOR splits when **`3`** is in **`--union-rs`**).
