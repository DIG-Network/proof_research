# Notes

- **observation:** Marginal time per +10M `exists_tree` calls between **6e7** and **7e7** (~74 s) is **lower** than between **5e7** and **6e7** (~148 s), consistent with deeper memo reuse but still **LRU-capped**.
- **dead_end:** At this host envelope, **7e7/8M** is **not** sufficient to finish the **r=5** `d=3` root probe; hypothesis H1 falsified.
- **question:** Does **8e7** or higher cross completion, or does the search remain LRU-throttled indefinitely?
- **insight:** Session-state suggested **7e7+** as next lever; this run executes **7e7** explicitly for **r=5** so the timeline is pinned.
