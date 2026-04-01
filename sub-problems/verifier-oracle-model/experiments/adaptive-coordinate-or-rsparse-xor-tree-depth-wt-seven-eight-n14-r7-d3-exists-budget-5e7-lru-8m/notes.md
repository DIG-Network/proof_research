# Notes

- **Observation:** **`r=7`** **DP** **~0.54 s** for **3432** splits — orders of magnitude below **`r=6`/`r=8`** (**~435–510 s**) at the **same** **5e7/8M** envelope despite **larger** menu than **3003**.
- **Insight:** **Binomial duality** **`r↔14−r`** does **not** predict **runtime** (**`r=4`** vs **`r=10`** already showed this); here **`r=7`** (**self-dual**) is an **easy** **island** between **harder** neighbors **`r=6`/`r=8`**.
- **Dead end (for this probe):** Treating **`C(14,r)`** as a **single** **hardness** **predictor** — **3432** **PASS**es **instantly** while **2002** **PARTIAL** and **1001** **mixed** (**`r=10`** fast, **`r=4`** slow).
- **Next:** If a **unified** **story** is needed, focus on **parity / mask shell** **interaction** per **`r`** (not **menu size** alone); optional **stress** **r=7** with **smaller** budget to find a **PARTIAL** threshold (likely far below **5e7**).
