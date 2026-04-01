# Experiment entry

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-two-hour`

**Context:** verifier-oracle-model

**Hypothesis tested:** A **2-hour** (**7200 s**) wall-clock cap suffices to finish **`exists_tree`** for **`n=14`**, **`{7,8}`**, **`coord + r=5` XOR**, **`d=3`-only** with **unbounded** memo and print **`feasible=`**.

**Outcome:** INCONCLUSIVE

**Finding:** **`timeout 7200`** produced **exit 124** with stdout stuck at **`probing d=3 …`**—same pattern as **180 s** and **1800 s** probes. **No** **`d=3 feasible=`** line. Scaling **30 min → 2 h** does **not** cross the completion threshold on this host class.

**Implications:**

- Treat **`r=5` `d=3`** as **strictly harder** than **“tens of minutes”**; plan **overnight** or **sharded** runs if a boolean answer is required.
- **Unbounded LRU** + **2002** **5-sparse** splits at **`d=3`** remains the bottleneck; **OOM-safe** defaults (**`lru-maxsize`**) are unsuitable for **this** decision probe (per prior **`lru-memo`** FAIL).

**Analogy pass summary:** **Wall-clock bracketing** (minutes → tens of minutes → hours) to map **practical** complexity of a **fixed-depth** memoized DP; **4×** step still on the **flat** timeout plateau.

**Space-definition:** none
