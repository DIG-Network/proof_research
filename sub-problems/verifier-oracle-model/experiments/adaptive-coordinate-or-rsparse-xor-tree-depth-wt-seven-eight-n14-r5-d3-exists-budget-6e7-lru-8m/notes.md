# Notes

- **observation:** At **6×10⁷** `exists_tree` cap, **`r=5` `d=3`** still **PARTIAL**; LRU remains **saturated** (8M entries), same pattern as **5×10⁷**.
- **insight:** Marginal cost of **+10M** invocations is **~148 s** wall time after the **~421 s** baseline — consistent with steady-state **~10⁵** inv/s once the memo is full.
- **question:** Does **7×10⁷** or **8×10⁷** at **8M** LRU ever finish, or does LRU churn dominate indefinitely? (Risk: host OOM if working set grows — **75M/0** run was **SIGKILL** class.)
- **dead_end (local):** Treat **“just +20% budget”** as **insufficient** to close **`r=5` `d=3`** at **8M** LRU — same structural open class as before.
