# Notes

- **observation:** Second half was **~30 s** faster to exhaust **6e7** calls (**478.8** vs **509.1** s), suggesting unequal hardness across XOR index order (or cache effects from fresh processes).
- **dead_end (local):** **6e7/half** is **insufficient** to escape PARTIAL on either contiguous half; no shortcut witness found at this budget tier.
- **question:** Would **non-contiguous** shards (e.g. stride or random **400×3** style already PASS elsewhere) behave differently for `d=3` **existence** vs these contiguous blocks?
- **next:** Process-level **parallel** two **10e7** half runs if wall-clock allows; or raise per-shard budget toward **12e7** to match prior full-menu cap; or pivot to **anonymous-quorum-binding** per session-state.
