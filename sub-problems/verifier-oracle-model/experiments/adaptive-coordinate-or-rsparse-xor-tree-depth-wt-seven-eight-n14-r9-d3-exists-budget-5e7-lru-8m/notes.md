# Notes

- **Observation:** **`d=3 feasible=False`** printed after the internal partial path is an **artifact of truncation** (same pattern as **`r=5`** 5e7 run) — **not** a proof of infeasibility for the full **`coord+9xor`** menu.
- **Insight:** **`C(14,5)=C(14,9)=2002`** gives **equal menu size** but **different** DP geometry; **`r=9`** lands with **`r=5`** (PARTIAL at 5e7+8M), not **`r=6`** (PASS).
- **Next:** Larger budget / off-host RAM, **`r=8`/`r=10`** at same envelope, **union** menus, or continue **random XOR submenus** for **`r=9`** if hunting a **feasible=True** shard (one-way certificate only).
