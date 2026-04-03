# Notes

- **Implementation:** The **`n=13`** parent has no **`--full-r2-r(n-1)-union-only`** flag; **`--union-rs`** with **`2..12`** is the direct equivalent of the **`n=14`** full union probe.
- **Cost:** Almost all wall time is the default baseline **`coord_only`** scan to **`d=13`** (~35+ s); the union DP itself is **<0.1 s** at **`8177`** splits with **`4M`** LRU.
- **Next:** Same **`min_d`** check for **`n=12`** **`{6,7}`** (or other shells) if we want a second continuation point; or return to **`anonymous-quorum-binding`**.
