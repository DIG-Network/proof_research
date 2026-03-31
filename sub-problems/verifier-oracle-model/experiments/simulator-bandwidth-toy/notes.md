# Notes

- Subset-sum collisions in **real** discrete-log groups under **random** keys are statistically unlikely for small `n`; **malicious** key registration could try to force `U ≪ W` (related to **rogue-key** themes in multisignature literature) — not modeled cryptographically here.
- A **UC** proof would need a full **interface** (who sees what, when) and computational assumptions; this folder only blocks a **wrong** impossibility argument (“`W` is huge therefore `|π|` huge”) that confuses **anonymity** with **injective encoding**.
