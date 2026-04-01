# Hypothesis

**Claim:** A **30-minute** wall-clock cap on **`coord + r=5` sparse XOR**, **`d=3`-only** for **`n=14`**, **`{7,8}`** with **`--lru-maxsize 0`** is enough to finish the **`exists_tree`** probe and emit **`d=3 feasible=true/false`**, resolving whether the prior **3-minute** timeout was only a **short-budget** artifact.

**Falsification:** **`timeout` exit 124** with **no** **`feasible=`** line — same **stuck-at-`probing d=3`** pattern as **180 s** and **`r=9` `d=3`** long probes.

## Analogy pass

1. **Abstract structure:** DP over **6435** masks; **2002** splits for **5-sparse XOR**; memo keyed by **`(bits, depth)`** can still explore a **wide** reachable front at fixed **`d=3`**.

2. **Analogous domains:** (a) **BFS with pruning** — depth cap does not cap **breadth**; (b) **Dynamic programming table fill** — one column can be huge; (c) **Empirical complexity** — scaling only visible by **wall-clock**.

3. **Machinery:** **Probing** with **scaled** time budgets; **compare** to **shorter** and **longer** probes on **sibling** shards.

4. **Transfer seed:** If **30×** the **3-minute** budget still **times out**, treat **`r=5` `d=3`** as **structurally** in the **multi-hour** class (like **`r=9` `d=3`**), not a **quick** shard.
