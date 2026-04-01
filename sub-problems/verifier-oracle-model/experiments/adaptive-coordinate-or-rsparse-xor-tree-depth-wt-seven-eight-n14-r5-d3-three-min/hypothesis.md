# Hypothesis

**Claim:** On a typical automation host, a **3-minute** wall-clock cap on **`coord + r=5` sparse XOR**, **`d=3`-only** probe for **`n=14`**, **`{7,8}`** is enough to either finish **`exists_tree`** and print **`feasible=true/false`**, or to show the run is **trivially fast** (so longer budgets are unnecessary for this shard).

**Falsification:** The run **times out** before any **`d=3 feasible=`** line appears (**`timeout` exit 124**), matching the **heavy** **`d=3`** behavior seen for **`r=9`** and prior **`r=5`** mentions.

## Analogy pass

1. **Abstract structure:** Exact **`exists_tree`** DP over **6435** masks with **unbounded** **`(bits, depth)`** memo; **5-sparse XOR** menu size **C(14,5)=2002** splits — state space can grow superlinearly in wall-clock even when **`d`** is fixed to probe one layer.

2. **Analogous domains:** (a) **Dynamic programming fill** — one layer can still touch a huge reachable set; (b) **Graph search with memo** — frontier can remain large; (c) **SAT/CSP** — fixing "depth" does not bound **width** of the search.

3. **Machinery:** **Reachability** / **memo hit rate** analysis; here **empirical timeout** as a **budget probe**.

4. **Transfer seed:** Treat **short wall-clock** as a **cheap** **phase-transition** detector: if **`d=3`** does not finish in **minutes**, treat **`r=5` `d=3`** as **same class** as **`r=9` `d=3`** (**multi-hour** / **large-RAM** host).
