# 2026-03-31 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14`  
**Context:** verifier-oracle-model  
**Outcome:** INCONCLUSIVE

## Hypothesis tested

Scale **`n=14`**, **`|S|∈{7,8}`** (**6435** masks), same adaptive **coord + r-sparse XOR** DP as **`n=13`**. Expect baseline **coord `min_d=14`**, **full 14-XOR `min_d=1`**, and a full **`min_d(r)`** row comparable to **`n=13`**.

## Key finding

- **Baseline confirmed:** **coord-only `min_d=14`**, **coord + full 14-XOR `min_d=1`** (~137 s coord phase, **4M LRU**).
- **Partial interior row:** completed **`r ∈ {6,7,8,10,11,12,13}`** with documented **`min_d`**; **`r ∈ {2,3,4,5,9}`** and **union** probes **`{2,3,4}`**, **`{2..5}`** did **not** finish within **multi-hour** / **timeout** bounds (see **`results.md`** table).
- **Not** a disproof of the **`n=13`** pattern — **compute / memo** bottleneck on **low `r`** and **`r=9`** (LRU thrash observed on **`r=9`**).

## Implications

- Next session should **shard** **`r=2,3,4,5,9`** on a **high-RAM** host with **`--lru-maxsize 0`** (process-per-**`r`**) before claiming **`n=14`** scaling parity with **`n=13`**.

## Analogy pass summary

Direct structural extension of **`n=13 {7,8}`** and **global parity lemma** (full **`n`**-XOR splits adjacent shells).

## Pointer

**`results.md`** in the experiment folder.
