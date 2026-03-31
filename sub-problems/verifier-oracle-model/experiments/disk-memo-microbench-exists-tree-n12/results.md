# Results: disk-memo-microbench-exists-tree-n12

**Outcome:** FAIL (for the **hypothesis** that naive disk memo is a practical drop-in for `exists_tree` on this host)

**Setup:** `N_OPS=50_000`, keys of length 27 bytes (same byte width as a 1716-bit mask plus one depth byte). Compare sequential insert+lookup of the same key list for `dict`, `dbm.ndbm`, and SQLite (single transaction, `synchronous=OFF`).

**Observed (automation host, `python3 script.py`):**

- `dict_sec≈0.007` for 50k inserts + 50k lookups.
- `ndbm_sec≈0.17`, **~24×** `dict`.
- `sqlite_sec≈0.15`, **~22×** `dict`.

**Additional empirical signal:** A prototype that stored each `exists_tree` result in SQLite with **one transaction per depth** still made **no visible progress** on `r=2` within hundreds of seconds (aborted). A `dbm` variant similarly failed to finish `r=2` within **200s** wall clock. That is consistent with **per-state** disk round-trips on a recursion whose hot set is far larger than RAM for `r∈{5,7}`.

**Reasoning:** The microbench is **optimistic** (same keys reused immediately after insert — best-case locality). The real DP uses **scattered** keys and **orders of magnitude more** operations than 50k. A **20×+** base penalty therefore **rules out** “swap LRU for disk” as the fix for OOM on `r=5`/`r=7` without a **new algorithm** (fewer distinct states, symmetry breaking, frontier batching, or more RAM).

**Implications:**

- Keep reporting standalone `r=5` / `r=7` as **OOM on low-RAM hosts** unless the DP is restructured.
- Future disk-backed attempts need **coarser granularity** than one DB row per `(bits, depth)` state.
