# 2026-03-31 — disk-memo-microbench-exists-tree-n12

**Context:** `verifier-oracle-model` — follow-up to `(12,{6,7})` experiment where standalone `r=5` / `r=7` hit OOM and disk-backed `exists_tree` prototypes were impractically slow.

**Hypothesis tested:** Disk-backed memo (`dbm` / SQLite) can substitute for `lru_cache` and complete the heavy DP on memory-capped hosts.

**Outcome:** FAIL

**Finding:** On 50k insert+lookup cycles with 27-byte keys, `dbm.ndbm` and SQLite are **~22–24×** slower than an in-RAM `dict` even under **sequential reuse** (optimistic locality). Full `exists_tree` prototypes with per-state SQLite/`dbm` showed **no completion** for `r=2` within multi-minute windows, consistent with millions of scattered memo ops. Naive disk memo does not rescue `r=5`/`r=7` OOM without algorithmic change.

**Implications:**

- Next steps for missing `min_d(5),min_d(7)` rows: more RAM, symmetry/state compression, or a different verification model — not a drop-in disk LRU.

**Analogy pass:** See `hypothesis.md` in the experiment folder.

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/disk-memo-microbench-exists-tree-n12/`
