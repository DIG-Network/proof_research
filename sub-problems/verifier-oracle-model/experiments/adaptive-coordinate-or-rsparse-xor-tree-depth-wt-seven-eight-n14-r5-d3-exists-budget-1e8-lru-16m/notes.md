# Notes

- **Exit 247** is **not** the parent’s **exit 2** (**PARTIAL**); treat as **environment** **limit**, **not** a **mathematical** **FAIL**.
- **Contrast:** **(5e7, 8M)** hit **`max_exists_calls`** in **~421 s** with **clear** **PARTIAL** **line**; **(1e8, 16M)** **neither** **finished** **nor** **printed** **PARTIAL** **in** **~95 min** **here** — **suggests** **16M** **LRU** **state** **is** **expensive** **and** **/ or** **invocation** **rate** **dropped**.
- **Hypothesis** **for** **follow-up:** **Unbounded** **LRU** **may** **finish** **faster** **than** **very** **large** **capped** **LRU** **if** **distinct** **memo** **keys** **stay** **below** **RAM** **(** **fewer** **eviction** **overheads** **)** — **matches** **prior** **two-hour** **`lru-maxsize 0`** **attempts** **that** **ran** **hours** **without** **deciding** **(** **different** **tradeoff** **)**.
- **Parent** **lineage** **for** **memory** **/** **journal:** **extends** **…-r5-d3-exists-budget-5e7-lru-8m** **(** **same** **`r,d`,** **scaled** **caps** **)**.
