# Notes — n14 r=9 d=3 XOR eighth-shards 3e7×8

- **observation:** **`r=9`** build phase ~**4.0–4.1 s** per eighth vs **`r=5`** ~**2.6–3.4 s** — consistent with heavier XOR-9 menu construction.
- **observation:** LRU misses stay **~2.2–2.7M** per eighth — same “well under **8M** cap” regime as **`r=5`** eighths.
- **analogy:** **Dual** **2002** row (**`C(14,9)=C(14,5)`**) with **matched** sharding — outcome **parallel** (**all** **`False`**, **no** **PARTIAL**), reinforcing **parity-band** evidence without resolving **full-menu** **`d=3`**.
