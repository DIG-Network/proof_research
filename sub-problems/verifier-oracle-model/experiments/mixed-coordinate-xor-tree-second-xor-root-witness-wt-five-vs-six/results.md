# Results — second feasible pair-XOR at root (wt {5,6}, depth 5)

## Outcome: **PASS**

## Repro

```text
python -u sub-problems/verifier-oracle-model/experiments/mixed-coordinate-xor-tree-second-xor-root-witness-wt-five-vs-six/script.py
```

Exit code: **0** (final line: `PASS`).

## Measured quantities

| Quantity | Value |
|----------|--------|
| `feasible_xor_root_count` | **45** |
| `second_xor_root_pair` (2nd lex feasible root) | **(0, 2)** |
| `witness_tree_depth` | **5** |
| `sha256_second_root` | `6e77edf57b33f7de70749e99764c8dfa5b1f4c3d7988492b0132917f74b6d299` |
| `sha256_default_067` | `be23dbf8e7b0314a497b90e703e12c3c74726dd4cc90070c7653bc2d3310ce41` |
| vs 067 witness | **`DIFFERS_FROM_DEFAULT_WITNESS`** |

Leaf-sum invariant **462** and depth **≤5** asserted by script (same checks as **067**).

## Reasoning

The hypothesis required **≥2** lex-feasible pair-XOR roots and a **non–byte-identical** nested JSON witness vs **`witness(full, 5)`** from **067**. Both hold: many feasible roots exist; forcing the **second** lex root **(0,2)** and completing children with **067**’s coord-first **`witness(S, d−1)`** yields a valid depth-5 tree with a **different** canonical JSON hash than **067**.

## Wall clock

Full run ~**2 minutes** on the machine used (heavy enumeration at root + subtree witness build).
