# Notes

- **LRU 8M** filled to cap (reported `currsize=8000000`) at budget cut — same pattern as 5e6 runs hitting ~5M states.
- **Wall time** ~**421 s** for **5×10⁷** invocations ⇒ ~**1.19×10⁵** inv/s (higher than ~7.7×10⁴ on the 5e6 run — less overhead per call once hot, or host variance).
- Still **no** trustworthy `d=3 feasible=` outcome; the `feasible=False` line in the partial branch is **not** a certified impossibility — it is the log row appended on budget exhaustion.
- **r=6** should be probed at the same **(5e7, LRU 8M)** bracket next for symmetry with **r=5**.
