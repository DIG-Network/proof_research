# Notes

- **dead_end (host):** Running **two** parent DP processes each with **10M** LRU in parallel on this environment risks **OOM** (**SIGKILL** on one worker) and **~6×** slowdown on the other vs sequential — **parallel half-shards at 10M LRU are not viable** here without more RAM or smaller LRU per process.
- **Sequential baseline:** Prior sequential **12e7×2** run: shard0 **~1034 s** DP, shard1 **~992 s** DP, **~35 min** total — both PARTIAL, no SIGKILL.
- **Next:** If parallel wall-clock is ever retried: lower **per-process** memory (**smaller LRU**) or **disjoint machines**; otherwise stay **sequential** or **raise single-process budget** on a larger host.
