# Notes

- **Scaling:** **180 s** (**`…-r5-d3-three-min`**) and **1800 s** (**this run**) both **exit 124** at **`probing d=3 …`** with **no** **`feasible=`** output — **10×** wall-clock did **not** change the **observable** phase; the **DP front** for this shard is **very heavy**.
- **Comparison:** **`r=9` `d=3`** already showed **90 min** insufficient (**`…-r9-d3-ninety-min`**); **`r=5` `d=3`** now shows **30 min** insufficient — **not** a **minutes-only** quirk of **`r=5`**.
- **Next:** **Large-RAM / multi-hour** host: continue **`r=5` `d=3`**, **`r=9` `d=3`**, then **union** shards **`{2,3,4}`**, **`2..5`**, **`2..13`** with **`--lru-maxsize 0`** (per **`session-state`** / digest).
