# Notes

- **observation:** **~472 s** to exit **247** — same qualitative failure mode as **r=5** **12M** at **10e7**.
- **insight:** Larger LRU does not uniformly help: **10M** finishes **PARTIAL**; **12M** OOMs — the crossover is sharp on this host for the **2002**-split **d=3** envelope.
- **next:** Stay on **≤10M** LRU for bounded-RAM runs; pursue **high-RAM** / **lru-maxsize 0** with wall limits, or **XOR** sharding / menu restrictions already used for negatives.
