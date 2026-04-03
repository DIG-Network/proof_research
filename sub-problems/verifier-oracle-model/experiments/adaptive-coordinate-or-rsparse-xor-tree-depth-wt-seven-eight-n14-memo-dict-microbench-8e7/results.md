# Results

**Outcome:** PASS

**What was measured:** Two back-to-back runs of the parent `n=14` driver: **`r=5`**, **`d=3`-only**, **`--max-exists-calls 8000000`**, **`--lru-maxsize 10000000`**. Run A default memo (**`lru_cache`** at **10M**). Run B **`--memo-dict`**.

**Observed (this run, `script.py` microbench):**

- Run A (**`lru_cache`**, **10M** cap): exit **2**, wall **65.4541 s**.
- Run B (**`--memo-dict`**): exit **2**, wall **26.1314 s**, **`memo_dict_size=3214257`** at cutoff.

**Speedup:** **2.505×** wall time at the **same** **8×10⁷** invocation budget — consistent with **LRU eviction thrashing** on this search; dict memo retains distinct **`(bits, depth)`** states without eviction.

**Implication:** Full-menu **`r=5`**, **`d=3`** probes that previously used **10M** LRU (**24e7–30e7** class) should be re-run with **`--memo-dict`** (and **RAM** headroom) before increasing budgets further; **disk memo** remains disfavored per **`disk-memo-microbench-exists-tree-n12`**.

**Note:** A **30×10⁷** **memo-dict** full run was started in this session but **not** carried to completion here (long wall time / environment limits); the microbench is the reproducible artifact.
