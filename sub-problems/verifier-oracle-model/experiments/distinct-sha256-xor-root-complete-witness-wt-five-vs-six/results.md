# Results — injective fingerprints on XOR-root + 067-child family

## Outcome: **PASS**

## Repro

```text
python -u sub-problems/verifier-oracle-model/experiments/distinct-sha256-xor-root-complete-witness-wt-five-vs-six/script.py
```

Exit code: **0**.

## Measured quantities

| Quantity | Value |
|----------|--------|
| `feasible_xor_root_count` | **45** |
| `distinct_sha256_count` | **45** |
| `distinct_canonical_json_bytes_count` | **45** |

## Reasoning

For **every** **feasible** **pair-XOR** **root** **(** **i,j** **)** **at** **depth** **budget** **5,** **the** **nested** **JSON** **(** **`sort_keys=True`**, **compact** **separators** **)** **is** **byte-unique** **across** **roots;** **hence** **`sha256`** **is** **injective** **on** **this** **45-element** **family** **(** **trivially** **implies** **071’s** **unique** **minimum** **among** **those** **digests** **).**

## Wall clock

~**126** **s** **(** **same** **warm-cache** **regime** **as** **071** **).**
