# Results — min SHA256 among XOR-root + 067-subtree witnesses

## Outcome: **PASS** (hypothesis: unique minimizer)

## Repro

```text
python -u sub-problems/verifier-oracle-model/experiments/min-sha256-xor-root-complete-witness-wt-five-vs-six/script.py
```

Exit code: **0**.

## Measured quantities

| Quantity | Value |
|----------|--------|
| `feasible_xor_root_count` | **45** (same family as **070**) |
| `min_sha256` | `00ce7493c647da1d5a82fcec0234b4feb50755f31122812e6f05e365a79f01f4` |
| `minimizer_count` | **1** |
| unique minimizer **(i, j)** | **(6, 7)** |
| `sha256_067_default` | `be23dbf8e7b0314a497b90e703e12c3c74726dd4cc90070c7653bc2d3310ce41` |
| vs **067** | **`MIN_DIFFERS_FROM_067_DEFAULT`** |

## Reasoning

For every feasible pair-XOR root, the script builds the tree **root = X(i,j)** with **067** **`witness(S, 4)`** on each non-empty child, canonicalizes JSON (**`sort_keys=True`**, compact separators), and takes **SHA256**. Among **45** candidates, **exactly one** pair achieves the minimum digest under lexicographic order on the hex string (equivalently byte order of the 32-byte digest). So the **falsifiable uniqueness** claim in **`hypothesis.md`** holds on this instance.

**Secondary:** The **min-hash** witness is **not** the **067** default tree (**first** successful split in **`witness(full,5)`**), which uses root **(0,1)** in the all-XOR pattern documented earlier. A verifier that pins **`π_tree`** by **“min SHA256 in this family”** would **not** agree with **“067 construction order”** without an explicit mapping.

## Wall clock

~**125 s** (warm **`lru_cache`** on **`exists_tree`** / **`witness`**; **45** root constructions).
