# Notes

- **Asymmetric LRU effect:** **`r=9`** **8M→10M** **increased** DP time (**~850→957** s) while **`r=5`** **8M→10M** **decreased** it (**~917→838** s) at **10e7** — suggests different reuse/thrash structure between the two **2002** menus under larger cache.
- **Still PARTIAL:** no **d=3** completion within **10⁸** at **10M** LRU for either arity.
- **Next:** unbounded/sharded memo on high-RAM host, algorithmic change, or **anonymous-quorum-binding**; **12M** LRU still **OOM**-risky here per digest.
