# Notes

- **LRU helps time, not verdict:** **8M→10M** at **10e7** cut **`r=5`** DP time **~916.6→837.5 s** (**~8.6%** faster) but **still** **PARTIAL** at cap — **not** a completion lever at this budget.
- **Host note:** **10M** completed cleanly (**no** **OOM**); **12M** remains risky per prior **75e6/12m** SIGKILL class.
- **Dual 2002:** pair with **`r=9`** **10e7/10m** for asymmetry check (**r=9** **8M** was **faster** than **r=5** **8M**).
