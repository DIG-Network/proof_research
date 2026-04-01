# Session State

**Last updated:** 2026-04-01 17:30 UTC
**Last experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-partition-shard-scan-400` (journal: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-partition-shard-scan-400`)
**Last outcome:** PASS
**Current focus:** sub-problems/verifier-oracle-model
**Active sub-problems:** verifier-oracle-model (IN PROGRESS), anonymous-quorum-binding (IN PROGRESS)
**Blocking sub-problems:** none (main-problem not advanced)
**Next action:** **`r=9`** contiguous XOR shards **PASS** — all five **`feasible=False`** at **`d=3`**, **LRU 8M** saturated each shard (**~12.4 min** total). Next: **`r=9`** **`--xor-index-indices`** random/shift scans (mirror **`r=5`** **`400×3`**), or **`r=5`** with **lower** **`max-exists-calls`** for **PARTIAL** threshold hunt; **`r=5`/`r=9`** full-menu **`d=3`** still **open**.
**Attractor warning:** none
**Pending journal writes:** none
**Pending commits:** none (after push)
**Key scratch pins:** none
**Open planner tasks:** not tracked (hosted MCP optional)
**Ledger run id:** (cron tick — optional ledger append)

**Git delivery:** Work is committed and pushed to **`main`** only (authoritative policy).

**Note:** `.mcp` contains `project_name=proof_researcher` for hosted MCP when enabled.

**Tooling:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` supports `--xor-index-range START:END` and **`--xor-index-indices i,j,k,...`** (with `--r-single`).
