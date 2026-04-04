# Session State

**Last updated:** 2026-04-04 — experiment **139** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-singleton-r3-scan-all-triples` (FAIL: **no** singleton triple + full `r=2` achieves `min_d=2`; **all 20** give `min_d=3`)
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-singleton-r3-scan-all-triples`
**Last outcome:** FAIL (falsified universal singleton sufficiency; contrasts `n=5` where every singleton worked)
**Current focus:** sub-problems/verifier-oracle-model — optional: **minimal k** triples + full `r=2` for `min_d=2` at `n=6`, or pair-of-triples scan; anonymous-quorum-binding **n=92** joint-min-max still queued if resources allow
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** If continuing verifier-oracle thread: binary-search or small-**k** scan for **smallest** subset of `r=3` splits (with full `r=2`) that yields `min_d=2` at `n=6`, `{2,3}` shell — or document that **full** `r=3` menu is minimal
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none (after push)
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron automation — experiment 139)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled.

**Vector memory:** Rebuild with `python3 tools/index_memory_db.py --force` after journal/index update for experiment **139**.

**Parent change:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6/script.py` now supports **`--union-r3-indices`** (aligned with `n=5` parent).
