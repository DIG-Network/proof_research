# Notes

- **Exit 247 / -9:** Treat as **SIGKILL** path — **not** a falsification of **`d=3`** **feasibility**; **resource** **limit** **not** **logic** **result**.
- **Contrast 1e8/16M:** That run survived **~95 min** before **247**; **12M** **LRU** **here** **dies** **~8** **min** — **non-monotone** **in** **wall** **time** **vs** **cache** **size** **likely** **due** **to** **peak** **RSS** **(** **12M** **entries** **+** **frontier** **)** **vs** **16M** **run** **possibly** **different** **host** **or** **allocator** **behavior** **;** **main** **takeaway:** **this** **host** **cannot** **carry** **12M** **LRU** **for** **this** **shard** **to** **completion** **of** **budget** **or** **root** **decision**.
- **Hypothesis** **(clean** **PARTIAL** **in** **~1** **h)** **:** **Falsified** **for** **this** **environment** **—** **no** **PARTIAL** **line** **observed**.
