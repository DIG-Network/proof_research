# Notes

- **Observation:** Both contiguous halves **PARTIAL** at **12e7/8M**; **no** **`d=3 feasible=True`** witness—mirrors **`r=5`** qualitative outcome at the same envelope.
- **Observation:** Total sequential DP **~1886** s vs **`r=5`** **~1853** s (**~2%** slower aggregate); **`r=9`** is **not** uniformly faster on **half** menus despite often beating **`r=5`** on **full** 2002 at the same cap.
- **Insight:** **Shard0** **`r=9`** took **~974** s vs **`r=5`** **~928** s; **shard1** **`r=9`** **~912** s vs **`r=5`** **~926** s—**order asymmetry** between **`r`** values on **fixed** index ranges.
- **Dead end (local):** This exact **(12e7, 8M, contiguous halves)** configuration does **not** surface a **positive** **`d=3`** certificate for **`r=9`**.
- **Next:** Larger per-half budget only if RAM allows; **non-contiguous** **1001**-wide menus; or accept **PARTIAL** as the practical envelope for **2002** **`d=3`** probes on bounded hosts.
