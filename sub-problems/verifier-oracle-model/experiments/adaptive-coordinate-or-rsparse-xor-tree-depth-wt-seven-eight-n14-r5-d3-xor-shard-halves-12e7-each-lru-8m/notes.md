# Notes

- **Observation:** **12e7** per contiguous half at **8M** LRU still **PARTIAL**; no **`d=3`** witness on either **`[0:1001)`** or **`[1001:2002)`**.
- **Observation:** Wall time per half **~927 s** vs **~540 s** at **7e7**—extra **5e7** calls cost **~387 s** per half with **LRU at cap** throughout.
- **Insight:** **8M** LRU remains a practical cap for **long** **`r=5`** half-menu runs on memory-bounded hosts; **12e7** is reachable **sequentially** without parallel **10M** workers.
- **Question:** Does **non-contiguous** sharding or **random** sub-menus of size **1001** ever yield a **positive** **`d=3`** witness while full **2002** stays PARTIAL? (Prior random **400×3** probes were all **`feasible=False`**, not witnesses.)
- **Next step:** **`r=9`** pressure with **8M** LRU half-shards or higher per-half budget if host allows; avoid **two** **10M** LRU processes in parallel on this environment.
