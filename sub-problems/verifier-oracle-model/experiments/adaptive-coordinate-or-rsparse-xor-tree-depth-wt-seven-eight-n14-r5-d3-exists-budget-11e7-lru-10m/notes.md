# Notes

- **12M** LRU remains avoided; **10M** LRU + **1.1×10⁸** budget completes cleanly (**exit 2**, not OOM).
- Marginal cost **10e7→11e7** at **10M** LRU for **r=5** is **~154 s** — consistent with continued thrashing at full LRU.
- **Next:** larger **exists** budget steps, **sharded** XOR scans, or **binding**-track work per session-state.
