# Hypothesis

**Claim:** A **2-hour** (**7200 s**) wall-clock cap on the **`n=14`**, **`{7,8}`**, **`coord + r=5` sparse XOR**, **`d=3`-only** probe (**`--lru-maxsize 0`**) is enough to finish **`exists_tree(full, 3)`** and emit **`d=3 feasible=true/false`**, resolving the shard that remained **open** after **3 min** and **30 min** timeouts.

**Falsification:** **`timeout` exit 124** with no **`feasible=`** line — same stuck pattern as **30 min** ⇒ treat **`r=5` `d=3`** as **multi-hour+** class (needs larger host or algorithmic change).

## Analogy pass

1. **Abstract structure:** Monotone **`exists_tree`** DP with **unbounded** memo; fixing **`d=3`** fixes **depth** but not **reachable memo width** — wall-clock can scale superlinearly in **mask domain** × **split menu** (**2002** **5-XOR** splits).

2. **Analogous domains:** (a) **Exhaustive game-tree search** — fixed depth, enormous branching; (b) **Memoized CFG reachability** — one nonterminal can still fan out; (c) **Empirical complexity** — only wall-clock distinguishes **“minutes”** vs **“hours”** plateaus.

3. **Machinery:** **Scaling probes** at **3 min → 30 min → 2 h** — standard way to bracket **practical** complexity before committing **overnight** runs.

4. **Transfer seed:** If **2 h** still times out, the **next** bracket is **overnight / OOM-safe sharding**, not another **small** multiplier on the same host.
