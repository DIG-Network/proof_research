# 2026-03-30 — distinct-sha256-xor-root-complete-witness-wt-five-vs-six

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/distinct-sha256-xor-root-complete-witness-wt-five-vs-six/`
- **Context:** verifier-oracle-model (**follow** **070** **/** **071** **—** **injectivity** **of** **fingerprints** **).

## Hypothesis tested

**The** **45** **feasible** **XOR-root+067-child** **trees** **at** **d≤5** **yield** **pairwise** **distinct** **`sha256(canonical** **JSON)`** **(** **equivalently** **45** **distinct** **JSON** **byte** **strings** **).**

## Outcome: **PASS**

**`distinct_sha256_count`** **=** **`distinct_canonical_json_bytes_count`** **=** **45** **=** **`|F|`.**

## Key finding

**Each** **feasible** **root** **choice** **is** **separated** **by** **both** **raw** **canonical** **JSON** **and** **SHA256** **on** **this** **toy** **—** **the** **multiplicity** **in** **070** **is** **45** **genuinely** **different** **`π_tree`** **bytes,** **not** **aliases** **under** **the** **chosen** **encoding.**

## Implications

- **Min-hash** **(** **071** **)** **and** **any** **injective** **ID** **of** **root** **are** **consistent** **with** **full** **separation** **here.**
- **Does** **not** **extend** **to** **larger** **witness** **families** **without** **retest.**

## Analogy pass summary

**Normal-form** **injectivity** **/** **dedup** **fingerprints** **—** **empirically** **all** **distinct** **on** **stated** **family.**
